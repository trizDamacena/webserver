const id = document.getElementById("filme")
const button = document.getElementById("botaoDeletar")
const lis = document.getElementById('meu-container')

fetch('http://localhost:8002/get_listinha').then((response) => {
    return response.json();
}).then((data) => {
    Object.values(data).map((listagem) => {
        console.log(listagem)
        lis.innerHTML +=`
        <li>
            <strong>Nome do filme:</strong> ${listagem.nome} - </br>
            <strong>Atores: </strong>${listagem.atores} - </br>
            <strong>Diretor: </strong>${listagem.diretor} </br> 
            <strong>Data de lançamento:</strong>${listagem.data_lancamento} - </br>
            <strong>Genero: </strong>${listagem.genero} - </br>
            <strong>Produtora: </strong>${listagem.produtora} - </br>
            <strong>Sinopse: </strong>${listagem.sinopse}
        </li>
        `
    })
})

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