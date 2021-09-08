import numpy as np
from PIL import Image


class Binarizacao:
    def __init__(self, imagem, limiar:int):
        self._limiar    = limiar
        self._imagem    = imagem
        self._linha     = np.size(imagem, 0)
        self._coluna    = np.size(imagem, 1)
        self._img_final = Image.new("RGB", (self._coluna, self._linha))


    def processar(self):
        # linha
        for i in range(self._linha):
            # coluna
            for j in range(self._coluna):
                rgb_imagem = self._imagem.convert('RGB')

                # pixel atual
                _, _, b = rgb_imagem.getpixel((j, i))

                # pixel branco
                cor = 0

                # se o pixel atual for maior que o limiar
                if int(b) > int(self._limiar):
                    # pixel preto
                    cor = 255

                # atualiza a cor do pixel
                self._img_final.putpixel((j, i), (cor, cor, cor))
        return self._img_final