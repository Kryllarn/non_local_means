# -*- coding: utf-8 -*-

from PIL import Image
import multiprocessing
import numpy as np

PIL_image = Image.open("""input.png""")                 # Recuperation de l'image PIL a partir du fichier
PIL_image.show()                                        # Affichage de l'image

# Caracteristiques de l'image
print("""{ Format :""", PIL_image.format,
      """; Mode :""", PIL_image.mode,
      """; Size :""", PIL_image.size, """}""")

PIL_image = PIL_image.resize((256, 256))                # Redimentionnement de l'image
PIL_image = PIL_image.convert("""L""")                  # Changement du mode de l'image, L <=> greyscale
PIL_image = PIL_image.rotate(180)                       # Rotation de l'image
PIL_image = PIL_image.transpose(Image.FLIP_LEFT_RIGHT)  # Transposition de l'image
# PIL_image.show()                                        # Affichage de l'image

PIL_image.getpixel((0, 0))                              # Get la valeur d'un pixel
PIL_image.putpixel((0, 0), 0)                           # Set la valeur d'un pixel

cores = multiprocessing.cpu_count()


for i in range(PIL_image.size[0]):
    for j in range(PIL_image.size[1]):
        if j%2 == 1:
            PIL_image.putpixel((i, j), 0)
        elif i%4 == i%2:
            PIL_image.putpixel((i, j), 255)
PIL_image.show()                                        # Affichage de l'image

PIL_image.save("""output.png""", format="""png""")     # Sauvegarde dans le fichier specifie

data = PIL_image.getdata()
print(list(data))

image = np.asarray(PIL_image)                           # Transformation de l'image en tableau manipulable par numpy
PIL_image = Image.fromarray(image)                      # Tranformation d'un tableau en image
