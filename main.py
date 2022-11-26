from functions import *

link = "https://www.paulus.com.br/portal/liturgia-diaria/#.YzxZEtLMLJ-"

def main():
    acessarSite(link)
    infoLiturgias = obterLegendas()
    for liturgia in infoLiturgias:
        criarImagens(liturgia)

    #fecharBrowser()

main()