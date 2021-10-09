
<div align="center">
  <h1>Sprint 2 - Inicio dia 20/09/2021 entrega dia 10/10/2021</h1>
</div>

<br id="topo">  
  
#### Navegador
* <a href="#objetivo">Objetivo da Sprint 2</a>
* <a href="#requisitos">Levantamento de requisitos</a>
* <a href="#raspagem">Raspagem automática com Python</a>
* <a href="#site">Site em HTML</a>
* <a href="#burndown">Burndown</a>

<span id="objetivo">

# 📌 Objetivo da Sprint 2 
  
<p align="justify">Para a segunda sprint nosso objetivo foi o de dar continuidade para o que foi desenvolvido na sprint anterior.
Dessa vez nós focamos em desenvolver coisas mais concretas, então nossa equipe de front-end deu início a nossa visão do protótipo que havíamos desenvolvido na primeira sprint e finalizou a página “Home”.</p>
<p align="justify">A equipe responsável pelo back-end desenvolveu um código, em python, que automaticamente faz a raspagem dos dados da página da Fatec e armazena-os.</p>

<div align="justify">
Nossos objetivos podem ser divididos, para essa segunda sprint, em três pontos de extrema importância:
  
* Desenvolvimento das páginas HTML e finalização da página HOME.
  
* Criação de código para a raspagem dos dados do site da FATEC.
  
* Armazenamento dos dados para serem utilizados nas futuras sprints e serem feitos o banco de dados e a clonagem dos repositórios.

</div>

→ [Voltar ao topo](#topo)
  
<span id="requisitos">

# 📝Levantamento de Requisitos 
  
<p align="justify">Os requisitos para essa Sprint foram fáceis de se definir, mas trabalhosos de se conseguir atingir.
Nós focamos principalmente na parte de estudos para essa sprint, como nosso conhecimento na área não é tão vasto nós definimos que os requisitos seriam os estudos das partes que envolvem o “HTML” e o “CSS”, para o desenvolvimento das páginas do nosso projeto. O estudo da parte sobre “Web Scrapping”, “Beautiful Soup” e “Python” foram feitos para que conseguíssemos desenvolver um código para que seja automatizada a raspagem dos dados da página da FATEC.</p>
  
→ [Voltar ao topo](#topo)
  
<span id="raspagem">

# Raspagem automática com Python
    
<p align="justify">Para o código da raspagem dos dados foram utilizadas algumas bibliotecas do Python, usamos a “requests” e a “Beautiful Soup”.
A requests permite que sejam enviadas solicitações em Python para a página HTTP, e com ela nós solicitamos o código do HTML das páginas da FATEC.
O Beautiful Soup foi usado para filtrar os dados da página e facilitar o armazenamento deles para serem usados no banco de dados e nas sprints futuras.
O código desenvolvido faz toda a raspagem automaticamente, percorrendo os sites e pegando os links dos Githubs dos projetos direto do youtube.</p>

> Para a visualização do código em Python [Clique aqui](/Back-end/url.py)

→ [Voltar ao topo](#topo) 
  
<span id="site">

# Site em HTML
  
<p align="justify">Após ter construído um protótipo navegável, a 2ª sprint foi dedicada ao processo de codificação das páginas anteriormente idealizadas. Nesse momento, os designs construídos no Figma foram transformados em arquivos HTML e CSS, responsáveis pelas marcações e estilos das páginas.<br>
A partir dessa codificação, o usuário irá conseguir interagir com a página web, acionando os menus e as páginas de cada curso, além de conseguir filtrar as pesquisas dos projetos por curso, ano, semestre e turma, respectivamente, conforme mostrado a seguir:</p>
  

https://user-images.githubusercontent.com/89143350/136669734-a8acdeec-aa2c-4674-82a1-e26cda718baf.mov

  

<p align="justify">Esses resultados podem ser reproduzidos com a ferramenta Visual Studio Code, por meio da extensão “Live Server”. Assim, clonando este repositório, abra os arquivos com extensão “.html” e digite o comando “ctrl” + “shift” + “p”, selecionando a opção "Open with Live Server". Esses comandos farão o projeto ser iniciado localmente.</p>
  
> Para a visualização dos códigos [Clique aqui](/Front-end)
  
→ [Voltar ao topo](#topo) 
 
<span id="burndown">
  
# 📉 Burndown
  
<p align="justify">O gráfico de Burndown é um método de visualização do andamento da sprint muito comum nos métodos ágeis. Ele possui a vantagem de permitir a rápida visualização, por todo o time de desenvolvimento, do andamento das atividades, sem necessariamente entrar nas histórias de usuário como no backlog da sprint.
No nosso gráfico de Burndown está a nossa divisão de duas equipes que ficaram responsáveis por duas partes do projeto (Front-end e Back-end). <br>A equipe responsável pela parte de front-end, ficou encarregada de estudar a utilização do HTML E CSS para a criação da página web funcional e criar a página home funcional . 
A equipe responsável pela parte de back-end, ficou encarregada dos estudos de Python sobre web scrapping e a biblioteca BeautifulSoup, além de realizar a automatização da raspagem (web scrapping)em python.<br>
Para além das atividades divididas entre as equipe, ficou de responsabilidade de todos os membros da equipe o realização de estudos sobre banco de dados, para que seja iniciado na terceira sprint.</p>
  
![burndown2](https://user-images.githubusercontent.com/89143350/136667774-d9115eff-b64c-4bdc-be30-e15d167c5fad.jpeg)
  
![tarefaburndown2](https://user-images.githubusercontent.com/89143350/136667796-2ec6bb96-86db-416d-bdcb-7f13db1332de.jpeg)

→ [Voltar ao topo](#topo)
