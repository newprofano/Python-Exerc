import cv2
import numpy as np
from PIL import Image
import math

arquive = 'm.jpeg'

def convertAndSave(array, name):
    img = Image.fromarray(array)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.save('{}.png'.format(name))

image = cv2.imread(arquive, cv2.IMREAD_GRAYSCALE)
imgOri = Image.fromarray(image)
imgOri.save('GreyScale.png')

tons = 256
n = len(image[0]) * len(image)
b = 0.5
c = 255 / math.log(256)
soma = 0
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
hist = hist.astype(int)
histAcul = []
pk = []
KLinha = []
imageEqual = []

equal_img = np.zeros(image.shape)
negat_img = np.zeros(image.shape)
logarit_img = np.zeros(image.shape)
poten_img = np.zeros(image.shape)

for a in range(len(hist)):
    soma = soma + hist[a]
    histAcul.append(soma)
    pk.append(histAcul[a]/n)
    KLinha.append(np.around((tons-1)*pk[a]))

KLinha = np.array(KLinha)
KLinha = KLinha.astype(int)

for idx_linha, val_linha in enumerate(image):
    for index, coluna in enumerate(val_linha):
        equal_img[idx_linha][index] = KLinha[coluna]
        negat_img[idx_linha][index] = (tons-1) - image[idx_linha][index]
        logarit_img[idx_linha][index] = c * \
            math.log(1 + image[idx_linha][index])
        poten_img[idx_linha][index] = (c * image[idx_linha][index]) ** b


convertAndSave(equal_img, 'Equalize')
convertAndSave(negat_img, 'Negative')
convertAndSave(logarit_img, 'Logarit')
convertAndSave(poten_img, 'Potenc')