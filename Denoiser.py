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


if __name__ == """__main__""":
    denoiser = \
        Denoiser("""pictures/input.png""")
    denoiser.display_image_details(denoiser.noised_image)
    denoiser.display_image_details(denoiser.denoised_image)
# end if
