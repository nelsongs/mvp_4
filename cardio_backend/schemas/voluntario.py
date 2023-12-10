from pydantic import BaseModel
from typing import List 
from model.voluntario import Voluntario

class VoluntarioSchema(BaseModel):
    """ 
        Define os dados do voluntário a ser inserido na base de dados, com exemplos
    """
    nome: str = "Pedro de Oliveira"
    idade: int = 25         # Idade do voluntário
    sexo: int = 2           # Masculino
    altura: int = 172       # Em cm, logo altura de 1.72 m
    peso: float = 80.5      # em kg
    sistolica: int = 120    # pressão sanguínea sistólica, em mmHG
    diastolica: int = 80    # pressão sanguínea diastólica, em mmHG
    colesterol: int = 0     # Nível de colesterol no sangue. 0:Normal, 1:Acima do normal, 2:Muito acima do normal
    glicemia: int = 0       # Nível de açucar no sangue. 0:Normal, 1:Acima do normal, 2:Muito acima do normal
    fumante: int = 0        # 0:Não, 1:Sim
    alcoolico: int = 0      # Ingere bebida alcóolica? 0:Não, 1:Sim
    atividade: int = 1      # Pratica atividades físicas? # 0:Não, 1:Sim   
    
class VoluntarioViewSchema(BaseModel):
    """
        Como os dados de um voluntário são retornados
    """
    id: int = 1
    name: str = "Pedro de Oliveira"
    idade: int = 25                 # Idade do voluntário
    sexo: int = 2                   # Mapeia 1 para M(asculino)
    altura: int = 172               # Em cm, logo altura de 1.72 m
    peso: float = 80.5              # Em kg
    sistolica: int = 120            # pressão sanguínea sistólica, em mmHG
    diastolica: int = 80            # pressão sanguínea diastólica, em mmHG
    colesterol: int = 0             # Nível de colesterol no sangue. 0:Normal, 1:Acima do normal, 2:Muito acima do normal
    glicemia: int = 0               # Nível de açucar no sangue. 0:Normal, 1:Acima do normal, 2:Muito acima do normal
    fumante: int = 0                # 0:Não, 1:Sim
    alcoolico: int = 0              # Ingere bebida alcóolica? 0:Não, 1:Sim
    atividade: int = 1              # Pratica atividades físicas? # 0:Não, 1:Sim
    diagnostico: int = 1            # Dependerá da avaliação do modelo treinado de ML. 0:Não, 1:Sim
    
class VoluntarioBuscaSchema(BaseModel):
    """
        Busca à base de dados pelo nome do voluntário
    """
    nome: str = "Pedro de Oliveira"

class ListagemVoluntariosSchema(BaseModel):
    """
        Varre a base de dados, retornando uma lista com os dados de todos os voluntários registrados
    """
    valuntarios: List[VoluntarioSchema]
    
class VoluntarioDelSchema(BaseModel):
    """
        Realiza a deleção do voluntário da base de dados pelo seu nome.
        Retorna o nome do voluntário removido, exibingo uma mensagem
    """
    nome: str
    
# Apresenta apenas os dados de um paciente    
def apresenta_voluntario(voluntario: Voluntario):
    """ 
        Retorna os dados de um voluntário, conforme o schema VoluntarioViewSchema
    """
    return {
        "id": voluntario.id,
        "nome": voluntario.nome,
        "idade": voluntario.idade,
        "sexo": voluntario.sexo,
        "altura": voluntario.altura,
        "peso": voluntario.peso,
        "sistolica": voluntario.sistolica,
        "diastolica": voluntario.diastolica,
        "colesterol": voluntario.colesterol,
        "glicemia": voluntario.glicemia,
        "fumante": voluntario.fumante,
        "alcoolico": voluntario.alcoolico,
        "atividade": voluntario.atividade,
        "diagnostico": voluntario.diagnostico
    }
    
# Apresenta uma lista de voluntarios
def apresenta_voluntarios(voluntarios: List[Voluntario]):
    """ 
        Retorna a lista dos voluntarios registrados na base de dados, conforme o schema VoluntarioViewSchema.
    """
    result = []
    for voluntario in voluntarios:
        result.append({
        "id": voluntario.id,
        "nome": voluntario.nome,
        "idade": voluntario.idade,
        "sexo": voluntario.sexo,
        "altura": voluntario.altura,
        "peso": voluntario.peso,
        "sistolica": voluntario.sistolica,
        "diastolica": voluntario.diastolica,
        "colesterol": voluntario.colesterol,
        "glicemia": voluntario.glicemia,
        "fumante": voluntario.fumante,
        "alcoolico": voluntario.alcoolico,
        "atividade": voluntario.atividade,
        "diagnostico": voluntario.diagnostico
        })

    return {"voluntarios": result}
