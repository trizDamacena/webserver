const id = document.getElementById("filme")
const button = document.getElementById("botaoDeletar")

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