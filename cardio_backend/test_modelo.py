from model.avaliador import Avaliador
from model.carregador import Carregador
from model.modelo import Model

# Para rodar o teste no modelo, execute no Terminal: pytest -v test_modelo.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados = "database/cardio_train.csv"
colunas = ['idade', 'sexo', 'altura', 'peso', 'sistolica', 'diastolica', 'colestoral', 'glicose', 'fumante', 'alcoolico', 'atividade', 'diagnostico']

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]
    
# Método para testar o modelo de Classificação a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
def test_modelo_class():  
    # Importando o modelo de classificação
    modelo_path = 'ml_model/final_classifier.pkl'
    modelo_teste = modelo.carrega_modelo(modelo_path)

    # Obtendo as métricas da Classificação
    # acuracia_lr, recall_lr, precisao_lr, f1_lr = avaliador.avaliar(modelo_lr, X, Y)
    acuracia, recall, precisao, f1 = avaliador.avaliar(modelo_teste, X, Y)
    
    # Testando as métricas da Classificação 
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia >= 0.40 
    assert recall >= 0.3 
    assert precisao >= 0.3 
    assert f1 >= 0.3 
 