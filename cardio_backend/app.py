from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Voluntario, Model
from logger import logger
from schemas import *
from flask_cors import CORS
import pickle

information = Info(title="API para o app Cardio_Desease - Diagnóstico de Doença Cardiovascular", version="1.0.0")
app = OpenAPI(__name__, info=information)
CORS(app)

# definição das tags
home_tag = Tag(name="Documentação", description="Seleção de tipo de documentação Swagger")
voluntario_tag = Tag(name="Voluntario", description="Inserção, visualização e remoção na base de dados de voluntários e seus diagnosticos")

# Rota para home
@app.get('/', tags=[home_tag])
def home():
    """
        Redireciona para a documentação Swagger, com a qual pode-se interagir com o banco de dados
    """
    return redirect('/openapi/swagger')

# Rota para a listagem de registros no banco de dados
@app.get('/voluntarios', tags=[voluntario_tag], responses={"200": ListagemVoluntariosSchema, "404": ErrorSchema})
def get_voluntarios():
    """
        Responsável por popular a visualização de cadastrados no "front end".
        Faz a varredura da base de dados.
        Retorna uma lista com todos os pacientes cadastrados na base de dados.
    """
    # Cria conexão com a base de dados
    session = Session()

    # Realiza a varredura
    voluntarios = session.query(Voluntario).all()

    # Caso não haja resgistros cadastrados ...
    if not voluntarios:
        logger.warning("Base de dados vazia :/")
        return {"message": "[Nenhum resgistro cadastrado :/]"}, 404
    else:
        logger.debug(f"%d resgistros encontrados" % len(voluntarios))
        # retorna os dados de todos os registros para exibição no frontend
        return apresenta_voluntarios(voluntarios), 200

# Rota para inserção de voluntário na base de dados
@app.post('/voluntario', tags=[voluntario_tag], responses={"200": VoluntarioViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def diagnostico(form: VoluntarioSchema):
    """
        Adiciona os dados de um novo voluntario à base de dados, acrescentando um campo com o seu diagnóstico
        Retorna os dados do voluntario, com o seu diagnóstico

        Argumentos de entrada:
            nome (str): nome do voluntário
            idade (int): idade do voluntario. 
            sexo (int): sexo do voluntário. Será mapeado como 1 para feminino e 2 para masculino
            altura (int): a altura deve ser inserida em cm. Exemplo: 1.70 m deverá ser inserido como 170 
            peso (float): o peso deverá ser inserido em formato float. Exemplo: 68 kg deverá ser inserido como 68.0
            sistolica (int): valor da pressão sanguínea sistólica, fornecida em mmHg. Exemplo: 120
            diastolica (int): valor da pressão sanguínea diastólica, fornecida em mmHg. Exemplo: 80
            colesterol (int): mapeado para 0:Nornal, 1:Acima do normal e 2: Muito acima do normal
            glicemia (int): mapeado para 0:Nornal, 1:Acima do normal e 2: Muito acima do normal
            fumante (int): valuntário fuma? mapeado para 0:Não e 1:Sim
            alcoolico (int): voluntário ingere bebida alcóolica regularmente? mapeado para 0:Não e 1:Sim
            atividade (int): voluntário mpratica atividade física? mapeado para 0:Não e 1:Sim

        Retorno:
            diagnostico (int): Mapeia o diagnóstico do voluntário. 0: negativo, 1: positivo.
    """
    # Carregamento do modelo de ML treinado e que servirá para avaliar a condição cardiovascular do voluntário
    ml_path = 'ml_model/final_classifier.pkl'
    
    modelo = pickle.load(open(ml_path, 'rb')) 
    
    voluntario = Voluntario(
        nome=form.nome.strip(),
        idade=form.idade, 
        sexo=form.sexo, 
        altura=form.altura, 
        peso=form.peso, 
        sistolica=form.sistolica, 
        diastolica=form.diastolica, 
        colesterol=form.colesterol, 
        glicemia=form.glicemia,
        fumante=form.fumante,
        alcoolico=form.alcoolico,
        atividade=form.atividade,
        diagnostico=Model.preditor(modelo, form)
    )
    
    logger.debug(f"Adicionando registro de nome: '{voluntario.nome}'")
    try:
        # cria conexão com a base de dados
        session = Session()
        # Verifica se o voluntário já foi cadastrado anteriormente na base de dados
        """
        if session.query(Voluntario).filter(Voluntario.nome == form.nome).first():
            error_msg = "Voluntário já cadastrado na base de dados :/"
            logger.warning(f"Erro ao adicionar voluntário '{voluntario.nome}', {error_msg}")
            return {"message": error_msg}, 409
        """
        # adiciona voluntário
        session.add(voluntario)
        # efetiva o comando de inserção do novo voluntário do banco de dados
        session.commit()
        # finalizando inserção de voluntário
        logger.debug(f"Adicionado voluntário de nome: '{voluntario.nome}'")
        return apresenta_voluntario(voluntario), 200
    # Caso haja occorências de erro na inserção de dados...
    except IntegrityError as e:
        # Duplicidade de voluntario
        error_msg = "Voluntário já existente :/"
        logger.warning(f"Erro ao adicionar voluntário '{voluntario.nome}', {error_msg}")
        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Não foi possível adicionar o voluntário :/"
        logger.warning(f"Erro ao adicionar voluntário '{voluntario.nome}', {error_msg}")
        return {"message": error_msg}, 400

# Rota para buscar um voluntário na base de dados identificado por seu nome
@app.get('/voluntario', tags=[voluntario_tag], responses={"200": VoluntarioViewSchema, "404": ErrorSchema})
def get_voluntario(query: VoluntarioBuscaSchema):
    """
        Busca um voluntário na base de dados a partir de seu nome
        Retorna os dados do voluntário
    """
    voluntario_nome = query.nome
    logger.debug(f"Coletando dados sobre o voluntário #{voluntario_nome}")
    # cria a conexão com a base
    session = Session()
    # faz a busca
    voluntario = session.query(Voluntario).filter(Voluntario.nome == voluntario_nome).first()

    # se o voluntário não foi encontrado
    if not voluntario:
        error_msg = f"Voluntário {voluntario_nome} não encontrado na base de dados :/"
        logger.warning(f"Erro ao buscar voluntário '{voluntario_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        logger.debug(f"Voluntário econtrado: '{voluntario.nome}'")
        # retorna os dados do voluntário
        return apresenta_voluntario(voluntario), 200

# Rota para a remoção de voluntário da base de dados
@app.delete('/voluntario', tags=[voluntario_tag], responses={"200": VoluntarioDelSchema, "404": ErrorSchema})
def del_voluntario(query: VoluntarioBuscaSchema):
    """
        Deleta um voluntário a partir do nome informado
        Retorna uma mensagem de confirmação da remoção
    """
    voluntario_nome = unquote(unquote(query.nome))
    logger.debug(f"Deletando dados sobre voluntário #{voluntario_nome}")
    # cria conexão com a base
    session = Session()
    # faz a remoção
    count = session.query(Voluntario).filter(Voluntario.nome == voluntario_nome).delete()
    session.commit()

    if count:
        # retorna a mensagem de confirmação
        logger.debug(f"Deletado voluntário {voluntario_nome}")
        return {"message": "Voluntário removido", "nome": voluntario_nome}
    else:
        # se o voluntário não foi encontrado
        error_msg = "Registro não encontrado na base de dados :/"
        logger.warning(f"Erro ao deletar voluntário '{voluntario_nome}', {error_msg}")
        return {"message": error_msg}, 404

    """
    # Busca o voluntário
    voluntario = session.query(Voluntario).filter(Voluntario.nome == voluntario_nome).first()
    if not voluntario:
        error_msg = "Voluntário não encontrado na base :/"
        logger.warning(f"Erro ao deletar voluntário '{voluntario_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(voluntario)
        session.commit()
        logger.debug(f"Deletado voluntário #{voluntario_nome}")
        return {"message": f"Voluntário {voluntario_nome} removido com sucesso!"}, 200
    """