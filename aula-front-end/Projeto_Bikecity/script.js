window.onload = function() {
    if (window.location.pathname.endsWith('index.html') || window.location.pathname === '/') {
        alert("Seja bem-vindo!");
    }
}

// array com as imagens do slideshow
  let images = ['img/image1.png', 'img/image2.png', 'img/image3.png']; 
  let currentImageIndex = 0;
  
  function updateImage() {
      let imgElement = document.getElementById('slideshowImage');
      imgElement.src = images[currentImageIndex];
  }
  function nextImage() {
      currentImageIndex = (currentImageIndex + 1) % images.length;
      updateImage();
  }
  function previousImage() {
      currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
      updateImage();
  }
  setInterval(nextImage, 3000); // muda a imagem a cada 3 segundos

  // validacao de login
function validar(){
    //declarando as variaveis
    let usuario = document.getElementById("usuario").value;
    let senha = document.getElementById("senha").value;
  
    if(usuario ==="Admin" && senha==="12345"){
        window.open("quiz.html");
    }
    else{
        alert("usuario/senha invalido")
    }
  }
// caminho para a pagina: quiz.html
window.onload = function() {
    if (window.location.pathname.endsWith('quiz.html')) {
        mostrarQuiz();
    }
}
// funcao para mostrar o quiz
function mostrarQuiz(){
    // Declarando variaveis
    let quiz1=prompt("1- Qual é o termo usado para descrever uma bicicleta que tem uma roda dianteira maior que a traseira?")
    let quiz2=prompt("2- Qual é a competição de ciclismo mais famosa do mundo?")
    let quiz3=prompt("3- Que parte de uma bicicleta é comumente referida como o ''cérebro'' da bicicleta?")
    let quiz4=prompt("4- Qual é o componente de uma bicicleta usado para frear, geralmente encontrado nos guidões?")
    let quiz5=prompt("5- Qual é a parte da bicicleta projetada para absorver impactos e proporcionar conforto ao ciclista?")
    let quiz6=prompt("6- Qual é o evento anual que encoraja as pessoas a andarem de bicicleta para o trabalho?")
    let quiz7=prompt("7- Qual é o nome da peça que protege a corrente da bicicleta?")
    let quiz8=prompt("8- O que você usa para encher os pneus da bicicleta?")
    let quiz9=prompt("9- O que você usa para segurar na bicicleta enquanto pedala?")
    let quiz10=prompt("10- Qual é o nome da peça que conecta o guidão à bicicleta e permite que você vire as rodas?")

    let mostrarQuizElement = document.getElementById("mostrarQuiz");

        mostrarQuizElement.innerHTML = `Na primeira pergunta, sua resposta foi: "${quiz1}" e a resposta é: bicicleta de roda grande ou "penny-farthing" <br> Na segunda pergunta, sua resposta foi: "${quiz2}" e a resposta é: "Tour de France" <br> Na terceira pergunta, sua resposta foi: "${quiz3}" e a resposta é: computador de bordo ou ciclomputador  <br> Na quarta pergunta, sua resposta foi: "${quiz4}" e a resposta é: alavanca ou manete de freio <br> Na quinta pergunta, sua resposta foi: "${quiz5}" e a resposta é: canote de selim ou selim <br> Na sexta pergunta, sua resposta foi: "${quiz6}" e a resposta é: "Dia Mundial do Ciclismo para o Trabalho" ou "Bike to Work Day" <br> Na sétima pergunta, sua resposta foi: "${quiz7}" e a resposta é:  "protetor de corrente" ou "cobertura de corrente" <br> Na oitava pergunta, sua resposta foi: "${quiz8}" e a resposta é: bomba de ar <br> Na nona pergunta, sua resposta foi: "${quiz9}" e a resposta é: guidão <br> Na décima pergunta, sua resposta foi: "${quiz10}" e a resposta é: mesa ou avanço <br><br>
         Veja abaixo os resultados com base no seu desempenho:<br> 1-2 acertos: Mais sorte na próxima vez <br> 3-4 acertos: Não tá nem bom e nem ruim, famoso na média <br> 5-6 acertos: Tá no caminho certo... <br> 7-8 acertos: Sabe muito do assunto! Parabéns <br> 9-10 acertos: Você é simplesmente o rei.`
    }