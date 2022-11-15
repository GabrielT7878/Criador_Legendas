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

def criarLegendas():
    tituloLiturgia = obterTituloLitugia() 
    diaLiturgia = obterDiaLiturgia(tituloLiturgia)
    print(diaLiturgia)
    #while diaLiturgia != 1:
    tempoLiturgico = obterTempoLiturgico()
    print(tempoLiturgico)
    
def obterTituloLitugia():
    tituloHTML = browser.find_element("xpath",'//*[@id="interno"]/div[2]')
    titulouterHTML = tituloHTML.get_attribute('outerHTML')
    tituloParse = BeautifulSoup(titulouterHTML,'html.parser')
    return tituloParse.text

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


def fecharBrowser():
    browser.close()