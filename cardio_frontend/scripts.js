/*
  ----------------------------------------------------------------------------------------
  Obter a lista de registros de voluntários existentes na base de dados via requisição GET
  ----------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/voluntarios';
  fetch(url, {
    method: 'get'
  })
    .then((response) => response.json())
    .then((data) => {
      data.voluntarios.forEach(item => insertList(item.nome, item.idade, item.sexo, item.altura, item.peso, item.sistolica, item.diastolica,
        item.colesterol, item.glicemia, item.fumante, item.alcoolico, item.atividade, item.diagnostico))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList()

/*
  --------------------------------------------------------------------------------------
  Inserir um registro de voluntario na base de dados via requisição POST
  --------------------------------------------------------------------------------------
*/
const postItem = async (nome, idade, sexo, altura, peso, sistolica, diastolica, colesterol, glicemia, fumante, alcoolico, atividade) => {
  const formData = new FormData();
  formData.append('nome', nome);
  formData.append('idade', idade);
  formData.append('sexo', sexo);
  formData.append('altura', altura);
  formData.append('peso', peso);
  formData.append('sistolica', sistolica);
  formData.append('diastolica', diastolica);
  formData.append('colesterol', colesterol);
  formData.append('glicemia', glicemia);
  formData.append('fumante', fumante);
  formData.append('alcoolico', alcoolico);
  formData.append('ativo', atividade);

  let url = 'http://127.0.0.1:5000/voluntario';
  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });

    window.location.reload(true); 
   
}


/*
  --------------------------------------------------------------------------------------
  Cria um botão "close" para cada item da lista
  --------------------------------------------------------------------------------------
*/
const insertDeleteButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u24CD");
  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}


/*
  --------------------------------------------------------------------------------------
  Remover um item da lista ao clicar no botão "close"
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");
  let i;
  for (i = 0; i < close.length; i++) {
    close[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nome = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Tem certeza?")) {
        div.remove()
        deleteItem(nome)
        alert("Removido!")
      }
    }
  }
}


/*
  --------------------------------------------------------------------------------------
  Deletar um voluntario da base de dados via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (nome) => {
  console.log(nome)
  let url = 'http://127.0.0.1:5000/voluntario?nome=' + nome;
  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    })
}


/*
  ---------------------------------------------------------------------------------------
  Adicionar um registro de voluntário com todos os dados solicitados 
  ---------------------------------------------------------------------------------------
*/
const newPerson = () => {
  let nome = document.getElementById("input-nome").value;
  let idade = document.getElementById("input-idade").value;
  let sexo = document.getElementById("input-sexo").value;
  let altura = document.getElementById("input-altura").value;
  let peso = document.getElementById("input-peso").value;
  let sistolica = document.getElementById("input-sistolica").value;
  let diastolica = document.getElementById("input-diastolica").value;
  let colesterol = document.getElementById("input-colesterol").value;
  let glicemia = document.getElementById("input-glicemia").value;
  let fumante = document.getElementById("input-fumante").value;
  let alcoolico = document.getElementById("input-alcoolico").value;
  let atividade = document.getElementById("input-atividade").value;

  // Verifica se o voluntário já se encontra cadastrado, antes de tentar adicionar
  const checkExistente = 'http://127.0.0.1:5000/voluntarios?nome=' + nome;
  fetch(checkExistente, {
    method: 'get'
  })
  .then((response) => response.json())
  .then((data) => {
    if (data.voluntarios && data.voluntarios.some(item => item.nome === nome)) {
      alert("O voluntário já se encontra cadastrado na base de dados.");
    } else if (!nome) {
      alert("Informe o nome do voluntário!");
    } else if (isNaN(idade) || isNaN(sexo) || isNaN(altura) || isNaN(peso) || isNaN(sistolica) || isNaN(diastolica) || isNaN(colesterol) || isNaN(glicemia)
      || isNaN(fumante) || isNaN(alcoolico) || isNaN(atividade)) {
      alert("Esse(s) campo(s) precisam ser números!");
    } else {
      // Insere os dados do voluntário na lista que será uapresentada no frontend
      insertList(nome, idade, sexo, altura, peso, sistolica, diastolica, colesterol, glicemia, fumante, alcoolico, atividade);
      // Envia esses mesmos dados para ser gravado na base de dados
      postItem(nome, idade, sexo, altura, peso, sistolica, diastolica, colesterol, glicemia, fumante, alcoolico, atividade);
      alert("Registro adicionado");
    }
  })
  .catch((error) => {
    console.error('Error:', error);
  });
  
}

/*
  --------------------------------------------------------------------------------------
  Insere items na lista e a apresenta
  --------------------------------------------------------------------------------------
*/

const insertList = (nome, idade, sexo, altura, peso, sistolica, diastolica, colesterol, glicemia, fumante, alcoolico, atividade, diagnostico) => {
  var voluntario = [nome, idade, sexo, altura, peso, sistolica, diastolica, colesterol, glicemia, fumante, alcoolico, atividade, diagnostico];

  var table = document.getElementById('cardiodata-table');
  var row = table.insertRow();

  for (var i = 0; i < voluntario.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = voluntario[i];
  }

  // Inserir um botão ao lado do registro inserido na lista, para possibilitar remover esse registro
  insertDeleteButton(row.insertCell(-1));

  // limpar elementos do formulário de entrada de dados
  document.querySelector('form').reset();
  // Coloca o foco no primeiro item do formulário de entrada de dados
  document.getElementById("input-nome").focus(); 

  // Caso o botão de remoção seja clicado, remove esse elemento da lista
  removeElement();

}


/*
  ---------------------------------------------------------------------------------------
  Fechar a aplicação 
  ---------------------------------------------------------------------------------------
*/
function closeApp () {
  if (confirm("Deseja encerrar a aplicação?")) {
    window.close();
  }
  
}
