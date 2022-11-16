from PIL import Image, ImageFont, ImageDraw
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import html5lib
from selenium.webdriver.common.keys import Keys
import os.path


browser = webdriver.Chrome()

def acessarSite(link):
    browser.get(link)

def obterLegendas():
    diaSemana = obterDiaSemana() 
    diaLiturgia = obterDiaLiturgia(diaSemana)
    print(diaLiturgia)
    controle = True
    mesLiturgias = []
    #while diaLiturgia != 1 or controle:
    while controle:
        tempoLiturgico = obterTempoLiturgico()
        print(tempoLiturgico)
        liturgias = obterLiturgias()
        print(liturgias)
        liturgias.insert(0,tempoLiturgico[1])
        liturgias.insert(0,tempoLiturgico[0])
        liturgias.insert(0,diaSemana)
        mesLiturgias.append(liturgias)
        print(mesLiturgias)
        controle = False
    
def obterDiaSemana():
    tituloHTML = browser.find_element("xpath",'//*[@id="interno"]/div[2]')
    titulouterHTML = tituloHTML.get_attribute('outerHTML')
    tituloParse = BeautifulSoup(titulouterHTML,'html.parser')
    return tituloParse.get_text(strip=True)

def obterDiaLiturgia(tituloLiturgia):
    dia = ''
    for letra in tituloLiturgia:
        if letra.isdigit():
            dia = dia+letra
    return int(dia)

def obterTempoLiturgico():
    tempoLiturgicoHTML = browser.find_element("id",'texto')
    tempoLiturgicoOuterHTML = tempoLiturgicoHTML.get_attribute('outerHTML')
    tempoLiturgicoParse = BeautifulSoup(tempoLiturgicoOuterHTML,'html.parser')
    p = tempoLiturgicoParse.findAll('p')
    tempoLiturgico = p[0].text
    corTempoLiturgico = p[1].text
    return tempoLiturgico, corTempoLiturgico

def obterLiturgias():
    liturgiasHTML = browser.find_element("tag name",'body')
    liturgiasOuterHTML = liturgiasHTML.get_attribute('outerHTML')
    liturgiasParse = BeautifulSoup(liturgiasOuterHTML,'html.parser')
    liturgias = liturgiasParse.findAll("div", {"class": "subtitulo-liturgia"})
    respostaSalmo = obterRespostaSalmo(liturgias) 
    liturgias.append(respostaSalmo)
    i = 0; 
    for liturgia in liturgias:
        liturgias[i] = liturgia.text
        i = i + 1
    return liturgias

def obterRespostaSalmo(liturgias):
    i = 0
    for liturgia in liturgias:
        if "Salmo" in liturgia.text or "Sl" in liturgia.text:
            next = liturgias[i].next_sibling
            next = next.next_sibling
            respostaSalmo = next.next_sibling
            return respostaSalmo
        i = i + 1

def fecharBrowser():
    browser.close()