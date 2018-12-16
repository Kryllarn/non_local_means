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

    # def dist_max(tab_patch):
    #     ind = 0
    #     max = tab_patch[0][2]
    #     for i in range(tab_patch.__sizeof__):
    #         if max < tab_patch[i][2]:
    #             ind = i
    #     return ind

    def get_index_of_maximal_distance(self):
        index = 0
        maximum = self.closest_patchs_array[0][2]
        for i in range(self.closest_patchs_array_maximum_size):
            if maximum < self.closest_patchs_array[i][2]:
                index = i
                maximum = self.closest_patchs_array[i][2]
            # end if
        # end for
        print("""maximum""", maximum, """index""", index)
        return index
    # end def

    def init_patchs_array(self, size):
        self.patchs_array = [[Patch((0,0), 0, self.noised_image)] * self.denoised_image.height] * self.denoised_image.width

        for x in range(self.denoised_image.width):
            for y in range(self.denoised_image.height):
                self.patchs_array[x][y] = Patch((x, y), size, self.noised_image)
                #print("grid :",self.patchs_array[x][y].grid[0][0])
            # end for
        # end for
    # end def

    def prepare_image(self):
        if self.noised_image.mode != """L""":
            # Convert to a greyscale system
            self.noised_image = self.noised_image.convert("""L""")
        # end if
    # end def

    def run(self, patch_size, window_size):
        distance = 0
        pixel = 0
        self.init_patchs_array(patch_size)
        self.closest_patchs_array = []

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
                            tmp = self.patchs_array[x][y].compare_grid(self.patchs_array[x + u- int((window_size - 1) / 2)][y + t- int((window_size - 1) / 2)])
                            print("patch : ", self.patchs_array[x][y].grid[2][2])
                            if self.closest_patchs_array_current_size < self.closest_patchs_array_maximum_size:
                                self.closest_patchs_array.append([u, t, tmp])
                                self.closest_patchs_array_current_size += 1
                            # end if
                            else:
                                self.closest_patchs_array[self.get_index_of_maximal_distance()] = [u, t, tmp]
                            # end else
                        # end if
                    # end for
                # end for

                for n in self.closest_patchs_array:
                    distance += n[2]
                # end for
                if distance == 0:
                    pixel = self.noised_image.getpixel((self.closest_patchs_array[0][0], self.closest_patchs_array[0][1]))
                else:
                    for n in self.closest_patchs_array:
                        pixel += self.noised_image.getpixel((n[0], n[1])) * n[2] / distance
                #print("Valeur pixel : ",pixel)
                # end for
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
    # for x in range(denoiser.noised_image.width):
    #     for y in range(denoiser.noised_image.height):
    #         print(denoiser.noised_image.getpixel((x, y)))
    #     # end for
    # # end for
    denoiser.init_patchs_array(1)
    denoiser.run(1, 3)
    denoiser.denoised_image.save("pictures/output.png", "PNG")
    denoiser.show("""input""")
    denoiser.show("""output""")
# end if
