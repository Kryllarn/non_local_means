# -*- coding: utf-8 -*-

from PIL import Image as img
import multiprocessing as mp
import numpy as np

# Lecture de l'image initiale
PIL_image = img.open("""noising_input.png""")

# Caracteristiques de l'image
print("""{ Format :""", PIL_image.format,
      """; Mode :""", PIL_image.mode,
      """; Size :""", PIL_image.size, """}""")

if PIL_image.mode == """RGBA""":
    # Changement du mode de l'image, L <=> greyscale
    PIL_image = PIL_image.convert("""L""")

# Caracteristiques materielles
cores = mp.cpu_count()
print("""{ Cores :""", cores, """}""")

# Affichage de l'image
PIL_image.show()

n = PIL_image.size[0]
half_patch_width = 7
patch_width = half_patch_width * 2 + 1

# Transformation de l'image en tableau manipulable par numpy
image = np.asarray(PIL_image)

# Tranformation d'un tableau en image
PIL_image = img.fromarray(image)

# Affichage de l'image
PIL_image.show()

# Sauvegarde de l'image traitee
PIL_image.save("""output.png""", format="""png""")

# PIL_image = PIL_image.resize((256, 256))                # Redimentionnement de l'image
# PIL_image = PIL_image.rotate(360)                       # Rotation de l'image
# PIL_image = PIL_image.transpose(Image.FLIP_LEFT_RIGHT)  # Transposition de l'image
# PIL_image.show()                                        # Affichage de l'image

# PIL_image.getpixel((0, 0))                              # Get la valeur d'un pixel
# PIL_image.putpixel((0, 0), 0)                           # Set la valeur d'un pixel

# for i in range(PIL_image.size[0]):
#     for j in range(PIL_image.size[1]):
#         if j%2 == 1:
#             PIL_image.putpixel((i, j), 0)
#         elif i%4 == i%2:
#            PIL_image.putpixel((i, j), 255)


# data = PIL_image.getdata()
# print(list(data))
