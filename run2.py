import cv2
import matplotlib.pyplot as plt


# haarcascade = 'assets/haarcascade_licence_plate_rus_16stages.xml'
haarcascade = 'assets/haarcascade_russian_plate_number.xml'
classificador = cv2.CascadeClassifier(haarcascade)
rect = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
elip = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (8, 8))


img_placa = cv2.imread(f'assets/imagens_originais/1.png')
img_cinza = cv2.cvtColor(img_placa, cv2.COLOR_BGR2GRAY)

# aplica classificador na imagem
placas_detectadas = classificador.detectMultiScale(
    img_cinza,
    scaleFactor=1.01,
    minNeighbors=15,
    minSize=(30, 50)
)

if len(placas_detectadas) > 0:
    # loop pelas placas detectadas na imagem
    corte_x, corte_y, corte_a, corte_l = 0, 0, 0, 0
    for (x, y, l, a) in placas_detectadas:
        # define variáveis do corte com os valores do loop atual
        corte_x, corte_y = x, y
        corte_l, corte_a = l, a

    # corta area detectada
    img_cortada = img_cinza[
        corte_y:corte_y+corte_a,
        corte_x:corte_x+corte_l
    ]

    # diminui tamanho da imagem
    img_pequena = cv2.resize(img_cortada, (600, 200))

    plt.imshow(img_pequena)
    plt.show()
