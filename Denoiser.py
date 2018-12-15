#!/usr/bin/env python
# -*- coding:Utf-8 -*-

from Patch import *
from PIL import Image


class Denoiser:

    def __init__(self, filename):
        self.noised_image = Image.open(filename)
        self.prepare_image()
        self.denoised_image = Image.new("""L""", (self.noised_image.size[0], self.noised_image.size[1]))
        self.denoised_image.save("""pictures/output.png""")
        self.patchs_array = [[]]
        self.closest_patchs_array = []
        self.closest_patchs_array_current_size = 0
        self.closest_patchs_array_maximum_size = 5
    # end def

    @staticmethod
    def display_image_details(image):
        print("""{ Format :""", image.format,
              """; Mode :""", image.mode,
              """; Size :""", image.size, """}""")
    # end def

    def get_index_of_maximal_distance(self):
        index = 0
        maximum = self.patchs_array[0][2]
        for i in range(self.patchs_array.__sizeof__()):
            if maximum < self.patchs_array[i][2]:
                index = i
            # end if
        # end for
        return index
    # end def

    def init_patchs_array(self, size):
        self.patchs_array = [[-1] * self.denoised_image.height] * self.denoised_image.width
        # self.patchs_array = [[Patch((x, y), size, self.noised_image)
        # for y in range(self.denoised_image.height)]
        # for x in range(self.denoised_image.width)]
        for x in range(self.denoised_image.width):
            for y in range(self.denoised_image.height):
                self.patchs_array[x][y] = Patch((x, y), size, self.noised_image)
            # end for
        # end for
    # end def

    def prepare_image(self):
        if (self.noised_image.mode == """RGBA""") or (self.noised_image.mode == """RGB"""):
            # Convert to a greyscale system
            self.noised_image = self.noised_image.convert("""L""")
        # end if
    # end def

    def run(self, patch_size, window_size):
        self.init_patchs_array(patch_size)
        closest_patch = []

        # Image width
        for x in range(self.denoised_image.width):
            # Image height
            for y in range(self.denoised_image.height):
                # Window width
                for u in range(window_size):
                    # Window height
                    for t in range(window_size):
                        if (
                            x + u - ((window_size - 1) / 2) >= 0
                            and y + t - ((window_size - 1) / 2) >= 0
                            and x + u + ((window_size - 1) / 2) < self.denoised_image.width
                            and y + t + ((window_size - 1) / 2) < self.denoised_image.height
                        ):
                            tmp = self.patchs_array[x][y].compare_grid(self.patchs_array[u][t])

                            if self.closest_patchs_array_current_size < self.closest_patchs_array_maximum_size:
                                self.closest_patchs_array[self.closest_patchs_array_current_size] = (u, t, tmp)
                                self.closest_patchs_array_current_size += 1
                            # end if
                            else:
                                if self.get_index_of_maximal_distance() > tmp:
                                    self.closest_patchs_array[self.get_index_of_maximal_distance()] = (u, t, tmp)
                                # end if
                            # end else
                        # end if
                    # end for
                # end for

                dist_total = 0
                for i in closest_patch:
                    dist_total += i[2]
                pixel = 0
                for i in closest_patch:
                    pixel += self.noised_image.getPixel((i[0], i[1])) * dist_total / i[2]
                self.denoised_image.putpixel((x, y), pixel)
            # end for
        # end for
    # end def

    def show(self, choice):
        if choice == """input""":
            self.noised_image.show()
        elif choice == """output""":
            self.denoised_image.show()
        else:
            print("""Invalid parameter "choice" for Denoiser.show(choice)""")
    # end def

# end class


if __name__ == """__main__""":
    denoiser = Denoiser("""pictures/input.png""")
    denoiser.init_patchs_array(1)
    print(denoiser.patchs_array)
    denoiser.run(1, 10)
    denoiser.show("""input""")
    denoiser.show("""output""")
# end if
