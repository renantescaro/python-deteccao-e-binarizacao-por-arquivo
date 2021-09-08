import cv2
import os
import numpy
from PIL import Image
from binarizacao import Binarizacao


# haarcascade    = 'haarcascade_licence_plate_rus_16stages.xml'
haarcascade    = 'haarcascade_russian_plate_number.xml'
classificador  = cv2.CascadeClassifier(haarcascade)

imagens = []
for p, _, files in os.walk(os.path.abspath('assets/imagens_originais')):
    for file in files:
        imagens.append(file)


# loop imagem por imagem
for imagem_atual in imagens:
    img_placa = cv2.imread('assets/imagens_originais/'+str(imagem_atual))
    print(imagem_atual)

    # transforma imagem em preta e branca
    img_cinza = cv2.cvtColor(img_placa, cv2.COLOR_BGR2GRAY)

    # aplica classificador na imagem
    placas_detectadas = classificador.detectMultiScale(
        img_cinza,
        scaleFactor=1.01,
        minNeighbors=15,
        minSize=(30,50) )

    # se detectou a placa, corta a imagem
    if len(placas_detectadas) > 0:
        # loop pelas placas detectadas na imagem
        corte_x, corte_y, corte_a, corte_l = 0, 0, 0, 0
        for (x, y, l, a) in placas_detectadas:
            # define variáveis do corte com os valores do loop atual
            corte_x, corte_y = x+20, y+10
            corte_l, corte_a = l-25, a-15

            # desenha retangulo na imagem detectada
            cv2.rectangle(
                img_cinza,
                (x, y),     # ponto 1
                (x+l, y+a), # ponto 2
                (0, 0, 0),  # cor RGB
                2 )

        # corta area detectada
        img_cortada = img_cinza[
            corte_y+5:corte_y+corte_a-5,
            corte_x+5:corte_x+corte_l-5]

        # diminui tamanho da imagem para 200 x 100
        img_pequena = cv2.resize(img_cortada, (200, 100))

        # converte imagem de CV2 para PIL
        img_plp = Image.fromarray(cv2.cvtColor(img_pequena,cv2.COLOR_BGR2RGB))  

        # binariza a imagem
        img_binarizada = Binarizacao(img_plp, 80).processar()

        # converte imagem de PIL para CV2
        img_mat = cv2.cvtColor(numpy.asarray(img_binarizada), cv2.COLOR_RGB2BGR)

        # salva imagem detectada
        cv2.imwrite('assets/placas_detectadas/'+str(imagem_atual), img_mat)