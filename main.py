from functions import *

link = "https://www.paulus.com.br/portal/liturgia-diaria/#.YzxZEtLMLJ-"

def main():
    acessarSite(link)
    obterLegendas()
    

    fecharBrowser()

main()