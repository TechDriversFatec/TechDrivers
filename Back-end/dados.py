import requests
from bs4 import BeautifulSoup
import csv
from git import Repo

youtube_lista, githubs = [], []

url = "https://fatecsjc-prd.azurewebsites.net/api/"
url_semestres = "https://fatecsjc-prd.azurewebsites.net/api/turmas.php"
html_content = requests.get(url_semestres).text
soup = BeautifulSoup(html_content, "html5lib")
semestres = soup.find_all("a")

#  Iterando pelo Primeiro Semestre
link_sem1 = url + semestres[0].get("href")
html = requests.get(link_sem1).text
soup = BeautifulSoup(html, "html5lib")
turmas = soup.find_all("a")
for turma in turmas:
    u = url + '2020-1/' + turma.get("href")
    html = requests.get(u).text
    sopa = BeautifulSoup(html, "html5lib")
    equipes = sopa.findAll('a')
    for equipe in equipes:
        yt = equipe.get("href")
        youtube_lista.append(yt)

#  Iterando pelo Segundo e Terceiro Semestre
for s in semestres[1:]:
    site = url + s.attrs['href']
    html = requests.get(site).text
    sopa = BeautifulSoup(html, 'html.parser')
    links = sopa.findAll('a')
    for link in links:
        yt = link.attrs['href']
        youtube_lista.append(yt)

#  Links github
for git in youtube_lista:
    html = requests.get(git).text
    gith = html.find(r"https://github.com")
    if gith != -1:
        fim = gith
        while html[fim] != '\\' and html[fim] != '"':
            fim = fim + 1
        github = html[gith:fim]
        githubs.append(github)

# Links gitlab
for gitlab in youtube_lista:
    html = requests.get(gitlab).text
    gitl = html.find(r"https://gitlab.com")
    if gitl != -1:
        fim = gitl
        while html[fim] != '\\' and html[fim] != '"':
            fim = fim + 1
        gitlab = html[gitl:fim]
        githubs.append(gitlab)

#  Começando a clonagem
for clone in githubs:
    try:
        nome = clone.split('/')[-1]
        Repo.clone_from(clone, nome)
        print('clonando ' + clone)
    except Exception as e:
        print(e)
        continue
