
import os
import numpy as np
import cv2
import natsort
import xlwt
from skimage import exposure

from sceneRadianceCLAHE import RecoverCLAHE
from sceneRadianceHE import RecoverHE

from matplotlib import pyplot as plt

np.seterr(over='ignore')
if __name__ == '__main__':
    pass
folder = r"\\cylog.local\rede\Usuarios\Documentos\Luiz\Documents\PROJETO_DIP"
# folder = "C:/Users/Administrator/Desktop/Databases/Dataset"

path = folder + "/InputImages"
files = os.listdir(path)
files =  natsort.natsorted(files)

for i in range(len(files)):
    file = files[i]
    filepath = path + "/" + file
    prefix = file.split('.')[0]
    if os.path.isfile(filepath):
        print('********    file   ********',file)
        # img = cv2.imread('InputImages/' + file)
        img = cv2.imread(folder + '/InputImages/' + file)
        sceneRadiance = RecoverHE(img)
        cv2.imwrite('HE.jpg', sceneRadiance)
        plt.subplot(111),plt.imshow(sceneRadiance)
        plt.show()
