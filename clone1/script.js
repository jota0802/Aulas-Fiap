// Seleciona o botão e a sidebar
const toggleButton = document.getElementById('toggleButton');
const texto = document.getElementById('texto');

let funcaoAtiva = 1;

function mudarnav() {
    if (funcaoAtiva === 1) {
        primeiraFuncao();
        funcaoAtiva = 2;
    } else if (funcaoAtiva = 2) {
        segundaFuncao();
        funcaoAtiva = 1;
    }
}

function primeiraFuncao() {
    // Adiciona um evento de clique para alternar a classe 'open' na sidebar
    texto.classList.toggle('open');
}

function segundaFuncao() {
    texto.classList.toggle('close')
}
// Adiciona um evento de clique para alternar a classe 'open' na sidebar