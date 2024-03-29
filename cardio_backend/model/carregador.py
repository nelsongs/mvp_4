import pandas as pd

class Carregador:

    def carregar_dados(self, url: str, atributos: list):
        """ 
            Carrega e retorna um DataFrame. 
        """
        
        return pd.read_csv(url, names=atributos,
                           skiprows=1, delimiter=';') 
    