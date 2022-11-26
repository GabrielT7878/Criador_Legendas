from PIL import Image, ImageFont, ImageDraw
import os



def criarImagens(infoLiturgia):
    os.mkdir(f'./{infoLiturgia[0]}')
    #create a file with the information
    f = open(f'./{infoLiturgia[0]}/informações.txt', 'w')
    for liturgia in infoLiturgia:
        f.write(f'{liturgia}\n')
    f.close()
    primeiraLeitura = infoLiturgia[3]
    salmo = infoLiturgia[4]
    respostaSalmo = infoLiturgia[len(infoLiturgia)-1]
    if str("DOMINGO") in infoLiturgia[0]:
        segundaLeitura = infoLiturgia[5]
        if  str(infoLiturgia[1][0]).isdigit():
            if str(infoLiturgia[1][1]).isdigit():
                infoLiturgia[1] = infoLiturgia[1][:3] + " DOMINGO" + infoLiturgia[1][3:]
            else:
                infoLiturgia[1] = infoLiturgia[1][:2] + " DOMINGO" + infoLiturgia[1][2:]
    else:
        segundaLeitura = ""
    evangelho = infoLiturgia[len(infoLiturgia)-2]
    tempoLiturgico = infoLiturgia[1].title()
    



    cor = ["branco","verde","vermelho","roxo","rosa","azul"]
    cor2 = ["white","green","red","purple","pink","blue"]
    i = 0
    color = "white"
    for i in range(0,6):
        if str(cor[i]) in infoLiturgia[2]:
            color = cor2[i]
        i = i + 1       
        
    if color == "white":
        colorText1 = "black"
        colorText2 = "black"
    else:
        colorText1 = "white"
        colorText2 = color
        
    cordLiturgia = (165,12)


    cordSalmo = (50,56)
    liturgia = [["Primeira Leitura",primeiraLeitura],["Salmo",salmo],["Segunda Leitura",segundaLeitura],["Evangelho",evangelho]]
    outrosCards = ["Canto de Entrada","Ato Penitencial","Glória a Deus","Rito do Ofertório","Canto da Comunhão","Preces da Assembleia"]


    cordTempoLiturgico = (145,62)


    caminho_fonte = "./Resources/Fontes/arial_bold.TTF"

    font = ImageFont.truetype(caminho_fonte, 20, encoding='utf-8')
    fontSalmo = ImageFont.truetype(caminho_fonte, 20, encoding='utf-8')

    for i in range (0,4):
        image = Image.open(f'Resources/Imagens/{color}.png')
        desenho = ImageDraw.Draw(image)
        desenho.text(cordLiturgia, liturgia[i][1], font=font, fill=colorText1)
        if liturgia[i][0] == "Salmo":
            if len(respostaSalmo) > 55:
                index = respostaSalmo[:55].rfind(" ")
                fontSalmo = ImageFont.truetype(caminho_fonte, 18, encoding='utf-8')
                cordSalmo = (50,52)
                Salmo = respostaSalmo
                respostaSalmo = respostaSalmo[:index]
                meio = 325
                test = len(respostaSalmo)
                meio = meio - (test * 5)
                desenho.text(cordSalmo, respostaSalmo, font=fontSalmo, fill=colorText2)
                meio = 325
                test = len(Salmo[index:])
                meio = meio - (test * 5)
                print(meio)
                cordSalmo2 = (meio,77)
                respostaSalmo = Salmo[index:]
                desenho.text(cordSalmo2, respostaSalmo, font=fontSalmo, fill=colorText2)
            else:
                meio = 325
                test = len(respostaSalmo)
                meio = meio - (test * 5)
                fontSalmo = ImageFont.truetype(caminho_fonte, 20, encoding='utf-8')
                cordSalmo = (meio,56)
                desenho.text(cordSalmo, respostaSalmo, font=fontSalmo, fill=colorText2)
        else:
            meio = 325
            test = len(tempoLiturgico)
            meio = meio - test * 5
            cordTempoLiturgico = (meio-20,62)    
            desenho.text(cordTempoLiturgico, tempoLiturgico, font=font, fill=colorText2)
        image.save(f'./{infoLiturgia[0]}/{liturgia[i][0]}.png')
        image.close()
    for i in range(0,len(outrosCards)):
        image = Image.open(f'Resources/Imagens/{color}.png')
        desenho = ImageDraw.Draw(image)
        desenho.text(cordLiturgia, outrosCards[i], font=font, fill=colorText1)
        desenho.text(cordTempoLiturgico, tempoLiturgico, font=font, fill=colorText2)
        image.save(f'./{infoLiturgia[0]}/{outrosCards[i]}.png')
        image.close()
        
print("Finalizado")

