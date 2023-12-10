# Projeto: Diagnóstico de Doenças Cardiovasculares
## Utiliza tecnicas e ferramentas de Machiine Learning (ML)
### *MVP-4 do Curso de Engenharia de Software da PUC Rio, 2023*
### Aluno: Nelson Gomes da Silveira

Este projeto é o resultado final (**MVP-4**) da aplicação dos conhecimentos obtidos ao cursar a disciplina **Qualidade de Software, Segurança e Sistemas Inteligentes** do Curso de Engenharia de Software da PUC Rio, ano de 2023.

O objetivo do projeto é demonstrar a utilização de técnicas e parâmetros de "Machine Learning-ML" para, a partir dos dados coletados na aplicação *frontend*, diagnosticar se uma pessoa apresenta doença cardiovascular.

Esses dados coletados, além de serem persistidos em uma base de dados SQLite3 para futuras refeências, serão submetidos a um modelo de classificação com parâmetros de treinamento existentes na aplicação *backend* do projeto, que fará o processamento desses dados comparando-os com um *Dataset* de dados semelhantes coletados de uma amostra relevante obtida de um repositório do Kaggle, neste link: **[Kaggle](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset/data)**

Esse *Dataset* foi utilizado para gerar o modelo de classificação utilizando ML em um *Notebook* do **Google Collab**, no qual foi utilizado para treinar e testar comparativamente em quatro modelos de referência (KNN, CART, NB e SVM). Depois de rodarem os processos de classificação e teste originais nos quatro modelos citados, os dados foram ainda submetidos a duas rodadas adicionais de testes comparativos, utilizando parâmetros de dados padronizados e normalizados. Os resultados desses testes podem ser vistos no próprio arquivo de Notebook do Google Colab, que se encontra no repositório Github do projeto, descrito neste documento.

O projeto consiste dos seguintes componentes (todos no repositório https://github.com/nelsongs/mvp_4):

1. O Dataset de nome **cardio_train.csv**, citado no terceiro parágrafo acima, que foi utilizado para treinar e gerar o modelo final que servirá para diagnosticar se o usuário da aplicação fullstack (backend e frontend) associada é portador ou não de doença cardiovascular. 

2. O arquivo **ML_Cardiovascular.ipynb**, é um Notebook do Google Colab no qual foram gerados e testados os modelos de *Machine Learning* citados no parágrafo 4 acima, utilizando o *Dataset* do item 1 como referência de dados comparativos. Ao final dos testes neste Notebook, foi gerado o arquivo modelo, de nome **final_classifier.pkl**, que é utilizado na aplicação fullstack para diagnosticar se a pessoa possui doença cardiovascular ou não. Esse arquivo modelo econtra-se na pasta ml_model, dentro da pasta cardio_backend.

3. Pasta **cardio_backend**, onde se encontra toda a infraestrutura de pastas e arquivos responsáveias pela aplicação *backend* do projeto.

4. Pasta **cardio_frontend**, onde se encontra toda a infraestrutura de pastas e arquivos responsáveis pela aplicação *frontend* do projeto.
 

Para replicar o que foi feito para testar e gerar o modelo de ML, o arquivo **ML_Cardiovascular.ipynb** pode ser baixado e aberto no Google Colab.

Em seguida serão comentados os passos para replicar a aplicação *fullstack* que aplica o modelo gerado a partir dos procedimentos no Notebook do Google Collab, para o dignóstico de doenças cardiovascular a partir de novos dados coletados de pessoas por meio da parte *frontend* da aplicação e processado pela parte *backend* da mesma.

A porção *fronend* é uma aplicação web simples, rodando em um navegador web, cuja finalidade é coletar dados de pessoas e enviá-las para serem tratadas pela porção *backend* que, além de utilizar o modelo de ML gerado e treinado para comparar os dados coletados e fornecer o diagnóstico de doença cardiovascular, mantém os dados dos usuários persistindo em uma base de dados SQLite3 embutida.

A porção *backend* é toda desenvolvida utilizando a linguagem de programação Python 3.

Além disso, na pasta onde residem os arquivos e subpastas da aplicação *backend* encontra-se também uma pequena rotina de teste do modelo de ML, utilizando a biblioteca **pytest**. Essa rotina chama-se test_modelo.py. O teste retorna se o modelo de classificação treinado passa nos critérios de acurácia fornecidos. Para executá-lo, basta abrir um terminal na pasta onde essa rotina reside e rodar o seguinte comando: **pytest test_modelo.py**. A saida no próprio terminal mostrará quantas instâncias forasm bem sucessidas, quantas falharam, bem como alguns avisos (warnings).

O script principal da aplicação *backend*, em Python, chama-se **app.py** e encapsula, por meio de bibliotecas, a API de documentação open source **Swagger**, que padroniza a integração dos processos de definir, criar e documentar a aplicação, possuindo recuros como *endpoints*, dados recebidos, dados retornados, código HTTP e métodos de autenticação, entre outros. Apenas funcionalidades mínimas do **Swagger** são utilizados nesta aplicação.



## Como executar 

Clone ou copie o conteúdo existente na pasta do projeto em https://github.com/nelsongs/mvp_4, onde estarão todo o conteúdo listado no parágrafo 5.

Ao acionar Ctrl-clicK no link acima, uma janela será aberta no seu navegador, no diretório público do projeto do GitHub. Logo acima, no canto superior direito, você visualiza o botão *<> Code* na cor verde. Clique em sua setinha e, na janela de diálogo que abre, clique naquele ícone com as duas janelinhas quadradas sobrepostas, ao final da linha com o endereço **https://github.com/nelsongs/mvp_4.git**. Isso copiará esse endereço para a memória. 

Em seguida, no seu VSCode ,clique em Clone Git Repository e dê um Ctrl-V na janelinha de endereço que abre no topo. Com o endereço no campo de entrada, pressione **Enter** no seu teclado. Uma janela de diálogo será aberta, na qual você escolherá a pasta onde deseja que esse repositório seja clonado. Clique então no botão ***Select as Repository Destination***. O repositório Git será clonado nessa sua pasta.

Uma alternativa a clonar o diretório é você clicar na última linha dessa caixa de diálogo, em arquivo Download ZIP. Isso baixará todo essa pasta em, formato comprimido .zip, para a pasta que você designar e onde você deverá descomrimir o seu conteúdo.

Em seguida, abra um Terminal ou Shell e vá para o diretório cardio_backend. Lá, crie um ambiente virtual Python para rodar essa aplicação, da seguinte forma:

---
- python -m venv env
---

Esse comando criará o ambiente virtual onde essa aplicação será executada, resolvendo problemas de conflito entre ambientes python distintos que você possa ter.

Após criado o ambiente virtual, será necessário ativá-lo. Para isso, dependendo do seu Sistema Operacional, você utilizará um dos *scripts* presentes no diretório **env/Scripts** (ou **env\Scripts** no Windows). Provavelmente nos sistemas Unix-like, como o Mac OSX e o Linux, o comando seria:

---
- env/Scripts/activate
---

Para o caso específico do Windows, no qual você normalmente usa o PowerShell, o comando é:

---
- env\Scripts\Activate.ps1
---

Pronto, o ambiente virtual python deverá estar rodando, o qual você poderá confirmar pela **(env)** no início da sua linha de comando.

Se precisar desativar o ambiente virtual por qualquer motivo, utilize o comando **env/deactivate ou env\deactivate** (Windows).

Em seguida, instale as bibliotecas listadas no arquivo `requirements.txt`, presente no mesmo diretório onde você se encontra com o Terminal/Shell aberto. As bibliotecas presentes nesse arquivo são dependências que a aplicação em python necessita. Instale-as por meio do seguinte comando:

---
- pip install -r requirements.txt
---

Na sequência, para executar a API que criará e gerenciará a base de dados, execute o seguinte comando:

---
- (env)$ flask run --host 0.0.0.0 --port 5000
---

Esse comando, além de criar uma instância vazia da base de dados SQLite3 na pasta *database*, fará com que a aplicação de *backend* espere requisições no endereço 127.0.0.1, na porta 5000. As requisições serão entregues por meio da aplicação de *frontend* e serão recebidas e tratadas pela aplicação de *backend*, interfaceando com a camada de base de dados da aplicação.

Portanto, para que essa aplicação de ***backend*** rode e fique esperando requisições por parte da porção cliente (***frontend***), é necessário abrir uma página no navegador, com o seguinte endereço:

---
- http://127.0.0.1:5000
---

Alternativamente você pode utilizar o endereço:

---
- http://localhost:5000
---

O navegador deve mostrar uma página inicial com o ***Swagger***. O ***Swagger*** serve para não apenas confirmar que a aplicação está executando satisfatoriamnmete, como pode ser usada para inserir e verificar o sucesso da inserção de dados na base de dados SQLite3.

Feito isso, você agora pode rodar a aplicação *frontend*, presente na pasta **cardio_frontend*. Para isso, execute (duplo clique) o arquivo index.html presente na raiz dessa pasta. Você poderá então verificar que, se inseriu dados pelo Swagger, esses aparecerão na interface web. A partir dai você poderá continuar cadstrando dados de pessoas diretamente na interface web. Após a confirmação da inserção dos dados, esses serão enviados à aplicação *backend*, onde serão tratados e o resultado do diagnóstico de doença cardiovascular será retornado e acrescido nos dados do usuário.

Se estiver com a janela do Terminal/Shell ainda aberta, você poderá acompanhar o retorno dos códigos de execução no Terminal/Shell e verificar os dados sendo inseridos/deletados etc., clicando no db.sqlite3 dentro do diretório database.

Para dar um *refreh* no banco de dados, clique no ícone de refresh do banco de dados, na parte superior esquerda da tela de visualização dos dados. 

Boa sorte!
