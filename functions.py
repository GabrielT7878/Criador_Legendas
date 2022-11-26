from PIL import Image, ImageFont, ImageDraw
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import html5lib
from selenium.webdriver.common.keys import Keys
import os.path
from criarImagens import *


browser = webdriver.Chrome()

def acessarSite(link):
    browser.get(link)

def obterLegendas():
    tituloDiaSemana = obterTituloDiaSemana() 
    diaLiturgia = obterDiaLiturgia(tituloDiaSemana)
    controle = 0
    infoLiturgias = []
    litugia = []
    quarta_feira = str("QUARTA-FEIRA")
    domingo = str("DOMINGO")
    while controle < 31: #diaLiturgia != 1 or  
        if quarta_feira in (tituloDiaSemana.upper)() or domingo in (tituloDiaSemana.upper)():
            tempoLiturgico = obterTempoLiturgico()
            liturgia = obterLiturgia()
            liturgia.insert(0,tempoLiturgico[1])
            liturgia.insert(0,tempoLiturgico[0])
            liturgia.insert(0,tituloDiaSemana)
            infoLiturgias.append(liturgia)
            
        linkProximaPagina = proximaPagina()
        browser.get(linkProximaPagina)
        tituloDiaSemana = obterTituloDiaSemana() 
        diaLiturgia = obterDiaLiturgia(tituloDiaSemana)
        controle = controle + 1
    return infoLiturgias

def obterTituloDiaSemana():
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
    i = 0
    while not str('(') in p[i].text:
        i = i + 1
        if i == len(p)+1:
            break 
    corTempoLiturgico = p[i].text
    return tempoLiturgico, corTempoLiturgico

def obterLiturgia():
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
    j = 0 
    for i in liturgias:
        if i == "Reflexão:":
            liturgias.pop(j)
        j = j + 1
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

def proximaPagina():
    botaoProximaPaginaHTML = browser.find_element('id','nextpost')
    botaoProximaPaginaOuterHTML = botaoProximaPaginaHTML.get_attribute('outerHTML')
    botaoProximaPaginaParse = BeautifulSoup(botaoProximaPaginaOuterHTML,'html.parser')
    linkProximaPagina = botaoProximaPaginaParse.find('a')
    return linkProximaPagina['href']



def fecharBrowser():
    browser.close()