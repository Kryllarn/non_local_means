#!/usr/bin/env python
# -*- coding:Utf-8 -*-

from PIL import Image


class Denoiser:

    def __init__(self, filename):
        self.noised_image = Image.open(filename)
        self.prepare_image()
        self.denoised_image = Image.new("""L""", (self.noised_image.size[0], self.noised_image.size[1]))
        self.denoised_image.save("""pictures/output.png""")
    # end def

    @staticmethod
    def display_image_details(image):
        print("""{ Format :""", image.format,
              """; Mode :""", image.mode,
              """; Size :""", image.size, """}""")
    # end def

    def prepare_image(self):
        if (self.noised_image.mode == """RGBA""") or (self.noised_image.mode == """RGB"""):
            # Convert to a greyscale system
            self.noised_image = self.noised_image.convert("""L""")
        # end if
    # end def

# end class



def init_tab_patch(image, sizePatch):
    tab_patch = [[]]
    for x in range(image.width()):
        for y in range(image.height()):
            tab_patch[x][y] = Patch((x, y), sizePatch, image)

    return tab_patch


def dist_max(tab_patch):
    ind = 0
    max = tab_patch[0][2]
    for i in range(tab_patch.__sizeof__):
        if max < tab_patch[i][2]:
            ind = i
    return ind


def run_denoiser(image, sizePatch, sizeWindow):
    tab_patch = init_tab_patch(image, sizePatch)
    closest_patch = []
    NB_CLOSEST = 5  # definition du nombre de patchs minimum
    res_image = PIL.Image.new(L, image.size(), color=0)
    # parcours de l'image
    for x in range(image.width()):
        for y in range(image.height()):
            # parcours de la fenetre
            for u in range(sizeWindow):
                for t in range(sizeWindow):
                    if (x + u - ((sizeWindow - 1) / 2) >= 0 and
                            y + t - ((sizeWindow - 1) / 2) >= 0 and
                            x + u + ((sizeWindow - 1) / 2) < image.width() and
                            y + t + ((sizeWindow - 1) / 2) < image.height()):
                        tmp = tab_patch[x][y].compare_grid(tab_patch[u][t])
                        if len(closest_patch) < NB_CLOSEST:
                            closest_patch[len(closest_patch)] = (u, t, tmp)
                        else:
                            closest_patch[dist_max(closest_patch)] = (u, t, tmp)
                        #end if/else
                # end for
            #end for

            dist_total = 0
            for i in closest_patch:
                dist_total += i[2]
            pixel = 0
            for i in closest_patch:
                pixel += image.getPixel((i[0], i[1])) * dist_total / i[2]
            res_image.putpixel((x,y),pixel)
        # end for
    # end for

    return res_image


if __name__ == """__main__""":
    denoiser = \
        Denoiser("""pictures/input.png""")
    denoiser.display_image_details(denoiser.noised_image)
    denoiser.display_image_details(denoiser.denoised_image)
# end if
