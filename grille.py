from PIL import Image

def setGrille(i, j, img, tailleGrille):
    grille = [[]]
    for k in range(tailleGrille):
        for l in range(tailleGrille):
            grille[k][l] = -1

    for k in range(tailleGrille):
        for l in range(tailleGrille):
            if(i - k - (tailleGrille-1)/2 >= 0 and j - k - (tailleGrille-1)/2 >= 0 and i + k + (tailleGrille-1)/2 < img.width() and j + k + (tailleGrille-1)/2 < img.height()):
                grille[k][l] = img.getPixel((k - (tailleGrille-1)/2,l - (tailleGrille-1)/2))

    return grille
