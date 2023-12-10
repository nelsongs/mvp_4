import numpy as np
import pickle

class Model:
  
    def carrega_modelo(self, path):
        """
            Carrega o modelo .pkl
        """
        model = pickle.load(open(path, 'rb'))

        return model
        
    
    def preditor(model, form):
        """
            Realiza a predição de um voluntario com base no modelo treinado
        """
        X_input = np.array([form.idade, 
                            form.sexo, 
                            form.altura, 
                            form.peso, 
                            form.sistolica, 
                            form.diastolica, 
                            form.colesterol, 
                            form.glicemia,
                            form.fumante,
                            form.alcoolico,
                            form.atividade
                        ])
        # Fazendo o reshape para que o modelo entenda que está sendo passado
        diagnosis = model.predict(X_input.reshape(1, -1))
        return int(diagnosis[0])