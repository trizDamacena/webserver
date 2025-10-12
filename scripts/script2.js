const id = document.getElementById("filme")
const button = document.getElementById("botaoDeletar")
const lis = document.getElementById('meu-container')

fetch('http://localhost:8002/get_listinha')
.then(response => response.json())
.then(filmes => {
    console.log(filmes)
    filmes.forEach(filme =>{
        lis.innerHTML +=`
        <li>
            <strong>Nome do filme:</strong> ${filme.titulo} - </br>
            <strong>Orçamento: </strong>${filme.orcamento} - </br>
            <strong>Duração: </strong>${filme.duracao} </br> 
            <strong>Data de lançamento:</strong>${filme.ano} - </br>
            <img src="${filme.poster}" alt="Poster do filme ${filme.titulo}" style="max-width:200px; height:auto;" />
        </li>
        `
    })
})
.catch(error => console.error("Erro em: ", error))

function deletar(event){
    event.preventDefault();
    id_valor = id.value
    fetch(`http://localhost:8002/${id_valor}`, {
        method: 'DELETE'
    }).then(response => {
        if (response.status === 204){
            console.log("O arquivo foi deletado com sucesso")
        }else{
            console.log("Ocorreu um erro")
        }
    })
}

button.addEventListener('click', deletar)