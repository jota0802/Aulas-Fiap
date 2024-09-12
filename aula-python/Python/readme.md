# Questionário de Afinidade com Equipes da Fórmula E

Este projeto é um questionário em Python que determina a afinidade do usuário com diferentes equipes da Fórmula E com base nas respostas fornecidas a uma série de perguntas.

## Estrutura do Código

O código é composto por várias partes principais:

### 1. Inicialização

O script começa com a definição de listas e variáveis que serão usadas ao longo do questionário:

- `lista_q`: Lista com os valores das questões.
- `Equipes`: Lista contendo as listas das equipes, onde serão armazenados os pontos atribuídos com base nas respostas.
- `EquipesNomes`: Lista com os nomes das equipes.
- `Pontos`: Lista para armazenar a pontuação total de cada equipe.
- `Valor`: Lista para auxiliar na soma das pontuações.

### 2. Loop do Questionário

O questionário é realizado dentro de um loop `while` que itera sobre uma série de perguntas (`Q1` a `Q10`). Cada pergunta é apresentada ao usuário, que deve responder com um número. Com base na resposta, pontos são atribuídos às equipes correspondentes:

- **Q1**: Atividades preferidas.
- **Q2**: Aspectos atrativos da Fórmula E.
- **Q3**: Estilo de vida.
- **Q4**: Modalidade esportiva preferida.
- **Q5**: Tipos de veículos elétricos preferidos.
- **Q6**: Preferência por equipes pioneiras ou novas.
- **Q7**: Tipo de patrocinadores reconhecíveis.
- **Q8**: Tipo de equipe apoiada.
- **Q9**: Visão de sucesso na Fórmula E.
- **Q10**: Estilo de música preferido.

### 3. Cálculo dos Pontos

Após a coleta das respostas, os pontos atribuídos a cada equipe são somados. A soma total dos pontos é usada para calcular a porcentagem de afinidade de cada equipe com o usuário.

### 4. Determinação da Equipe de Afinidade

O script determina qual equipe possui a maior pontuação e, consequentemente, com qual equipe o usuário tem mais afinidade. Uma mensagem personalizada é exibida ao usuário com base na equipe de afinidade.

## Executando o Código

Para executar o questionário, é necessário ter o Python instalado. De preferencia uma IDE como o VScode tambem. Com isso basta acessar o repositorio abaixo e baixar o arquivo em seu computador, assim você irá abri-lo e roda-lo pelo programa.

## Link repositório com o Arquivo: questionário_formula_e.py

- [questionário_formula_e.py](https://github.com/jota0802/Pyhton-Challenge)


## Integrantes 

## Desenvolvedores
| Dev | Avatar | RM |
| ------------- | ------ | -- |
| ![](https://img.shields.io/badge/DEV-João-blue?style=for-the-badge&logo=appveyor) | <a href="https://github.com/jota0802"><img src="https://avatars.githubusercontent.com/u/161319025?v=4" height="50" style="max-width: 100%;"></a> | RM556790 |
| ![](https://img.shields.io/badge/DEV-Yuri-blue?style=for-the-badge&logo=appveyor) | <a href="https://github.com/yurisilpess"><img src="https://avatars.githubusercontent.com/u/99032447?v=4" height="50" style="max-width: 100%;"></a> | RM557475 |
| ![](https://img.shields.io/badge/DEV-Gustavo-blue?style=for-the-badge&logo=appveyor) | <a href="https://github.com/gus7a2005"><img src="https://avatars.githubusercontent.com/u/161319479?v=4" height="50" style="max-width: 100%;"></a> | RM556289 |
| ![](https://img.shields.io/badge/DEV-Igor-blue?style=for-the-badge&logo=appveyor) | <a href="https://github.com/igor-soos"><img src="https://avatars.githubusercontent.com/u/164360059?v=4" height="50" style="max-width: 100%;"></a> | RM556010 |
| ![](https://img.shields.io/badge/DEV-Leonardo-blue?style=for-the-badge&logo=appveyor) | <a href="https://github.com/LeonBarbosa"><img src="https://avatars.githubusercontent.com/u/162709227?v=4" height="50" style="max-width: 100%;"></a> | RM555986 |
