from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Voluntario(Base):
    __tablename__ = 'voluntarios'
    
    id = Column(Integer, primary_key=True)
    nome= Column("Nome", String(40))
    idade = Column("Idade", Integer)
    sexo = Column("Sexo", Integer)
    altura = Column("Altura", Integer)
    peso = Column("Peso", Float)
    sistolica = Column("Sistolica", Integer)
    diastolica = Column("Diastolica", Integer)
    colesterol = Column("Colesterol", Integer)
    glicemia = Column("Glicemia", Integer)
    fumante = Column("Fumante", Integer)
    alcoolico = Column("Acoolico", Integer)
    atividade = Column("Atividade", Integer)
    diagnostico = Column("Diagnostico", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, nome:str, idade:int, sexo:int, altura:int, peso:float, sistolica:int, diastolica:int, 
                 colesterol:int, glicemia:int, fumante:int, alcoolico:int, atividade:int, diagnostico:int, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Voluntário e o registra na base de dados

        Argumentos:
            nome: nome do voluntário
            idade: idade do voluntário
            sexo: mapeado para 1:feminino e 2:masculino
            altura: altura do voluntário, em cm
            peso: peso do voluntário, em kg
            sistolica: medida da pressão sistólica sanguínea do voluntário, em mmHG
            diastolica: medida da pressão diastólica sanguínea do voluntário, em mmHG
            colesterol: nível de colesterol no sangue do voluntário, mapeada para 0:Normal, 1:Acima do nornal e 2:Muito acima do normal
            glicemia: nível de açucar no sangue do voluntário, mapeada para 0:Normal, 1:Acima do nornal e 2:Muito acima do normal
            fumante: se o voluntário é fumante ou não. Mapeado para 0:Não e 1:Sim
            alcoolico: se o voluntário consome ou não água que passarinho não bebe. Mapeado para 0:Não e 1:Sim (Pinguço)
            atividade: se o voluntário pratica ou não atividades físicas. Mapeado para 0:Não e 1:Sim (Marombeiro)
            diagnostico: baseado na interação com o modelo testado pela ML, o resultado será 0:Não ou 1:Sim para a doença cardiovascular
            data_insercao: data de inserção dos dados do voluntário na base de dados
        """
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura
        self.peso = peso
        self.sistolica = sistolica
        self.diastolica = diastolica
        self.colesterol = colesterol
        self.glicemia = glicemia
        self.fumante = fumante
        self.alcoolico = alcoolico
        self.atividade = atividade
        self.diagnostico = diagnostico
        # Utilizada data em que os dados foram registrados na base de dados
        if data_insercao:
            self.data_insercao = data_insercao