from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importa as classes definidas em model
from model.base import Base
from model.voluntario import Voluntario
from model.modelo import Model

db_path = "database/"
# Se o diretorio não existir, é criado
if not os.path.exists(db_path):
   os.makedirs(db_path)

# url de acesso ao banco (sqlite local)
db_url = 'sqlite:///%s/voluntarios.sqlite3' % db_path

# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia uma variável para interfacear com o banco de dados 
Session = sessionmaker(bind=engine)

# cria o banco de dados, se não existir 
if not database_exists(engine.url):
    create_database(engine.url) 

# cria as tabelas do banco, se não existirem
Base.metadata.create_all(engine)
