import requests
from bs4 import BeautifulSoup
import csv

youtube_primeiro = []
github_primeiro_semestre = []
youtube_segundo = []
github_segundo_semestre = []
youtube_terceiro = []
github_terceiro_semestre = []

url = "https://fatecsjc-prd.azurewebsites.net/api/"
f = csv.writer(open("bd-dos-dados.csv", "w"))
f.writerow(["Semestre", "Turma", "Equipe", "Github"])

url_semestres = "https://fatecsjc-prd.azurewebsites.net/api/turmas.php"
html_content = requests.get(url_semestres).text
soup = BeautifulSoup(html_content, "html5lib")
semestres = soup.find_all("a")

#  Iterando pelo Primeiro Semestre
link_sem1 = url + semestres[0].get("href")
txt_sem1 = semestres[0].text
html = requests.get(link_sem1).text
soup = BeautifulSoup(html, "html5lib")
turmas = soup.find_all("a")
for turma in turmas:
    u = url + '2020-1/' + turma.get("href")
    texto_turma = turma.text
    html = requests.get(u).text
    sopa = BeautifulSoup(html, "html5lib")
    equipes = sopa.findAll('a')
    for equipe in equipes:
        yt = equipe.get("href")
        texto = equipe.text
        youtube_primeiro.append(yt)
        f.writerow([txt_sem1, texto_turma, texto])
#  Reservando os links do primeiro semestre
for yt in youtube_primeiro:
    html = requests.get(yt).text
    ini = html.find(r"https://github.com")
    if ini != -1:
        fim = ini
        while html[fim] != '\\' and html[fim] != '"':
            fim = fim + 1
        github = html[ini:fim]
        github_primeiro_semestre.append(github)

#  Iterando pelo Segundo Semestre
link_segundo_semestre = url + semestres[1].get("href")
html = requests.get(link_segundo_semestre).text
sopa = BeautifulSoup(html, "html5lib")
links = sopa.findAll('a')
for link in links:
    yt = link.get("href")
    youtube_segundo.append(yt)
#  Reservando os links do segundo semestre
for yt in youtube_segundo:
    html = requests.get(yt).text
    ini = html.find(r"https://github.com")
    if ini != -1:
        fim = ini
        while html[fim] != '\\' and html[fim] != '"':
            fim = fim + 1
        github = html[ini:fim]
        github_segundo_semestre.append(github)

#  Iterando pelo Terceiro Semestre
link_terceiro_semestre = url + semestres[2].get("href")
html = requests.get(link_terceiro_semestre).text
sopa = BeautifulSoup(html, "html5lib")
links = sopa.findAll('a')
for link in links:
    yt = link.get("href")
    youtube_terceiro.append(yt)
#  Reservando os links do terceiro semestre
for yt in youtube_terceiro:
    html = requests.get(yt).text
    ini = html.find(r"https://github.com")
    if ini != -1:
        fim = ini
        while html[fim] != '\\' and html[fim] != '"':
            fim = fim + 1
        github = html[ini:fim]
        github_terceiro_semestre.append(github)
