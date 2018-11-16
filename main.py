# -*- coding: utf-8 -*-

from PIL import Image
import numpy as np

# Lecture de l'image

PIL_image = Image.open("""picture.png""")   # Recuperation de l'image PIL a partir du fichier
image = np.asarray(PIL_image)               # Transformation de l'image en tableau manipulable par numpy

# Affichage de l'image

image.show()
print(image)
