# -*- coding: utf-8 -*-
"""
Created on Tue May 25 13:53:17 2021

@author: luiz
"""

import numpy as np
import cv2
import mahotas

def escreve(img, texto, cor=(255,0,0)):
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, texto, (10,20), fonte, 0.5, cor, 0,
        cv2.LINE_AA)

#FILTRO HE

folder = r"\\cylog.local\rede\Usuarios\Documentos\Luiz\Documents\PROJETO_DIP" #Determinar a pasta do projeto

filtro = '/MIP/' #Identificar o filtro no formato: /filtro/
jpg = 'MIP.jpg'  #Renomear para o nome do arquivo, formato: filtro.jpg

imgColorida = cv2.imread(folder + filtro + jpg) #Carregamento da imagem

img = cv2.cvtColor(imgColorida, cv2.COLOR_BGR2GRAY) #escala de cinza
suave = cv2.blur(img, (8, 8)) #suavização, parametro escolhidos = 5

T = mahotas.thresholding.otsu(suave) 
bin = suave.copy() 
bin[bin > T] = 255
bin[bin < 255] = 0
bin = cv2.bitwise_not(bin) # binarizaçao 

bordas = cv2.Canny(bin, 70, 150) # bordas

#cv2.RETR_EXTERNAL = conta apenas os contornos externos
(objetos, lx) = cv2.findContours(bordas.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

escreve(img, "Imagem em tons de cinza", 0)
escreve(suave, "Suavizacao com Blur", 0)
escreve(bin, "Binarizacao com Metodo Otsu", 255)
escreve(bordas, "Detector de bordas Canny", 255)
temp = np.vstack([
    np.hstack([img, suave]),     
    np.hstack([bin, bordas])
    ])
#cv2.imshow("Quantidade de objetos: "+str(len(objetos)), temp)


imgC2 = imgColorida.copy()
cv2.drawContours(imgC2, objetos, -1, (255, 0, 0), 2)
#escreve(imgC2, str(len(objetos))+" objetos encontrados!")

#SALVA APENAS:
cv2.imwrite('Resultado_' + jpg, imgC2)
cv2.imwrite('Bordas_' + jpg, bordas)
#todas as imagens utilizadas 
cv2.imshow(jpg, imgColorida)
cv2.imshow('img', img)
cv2.imshow('suave', suave)
cv2.imshow('bordas', bordas)
cv2.imshow('bin', bin)
cv2.imshow("Resultado", imgC2)
cv2.waitKey(0)
