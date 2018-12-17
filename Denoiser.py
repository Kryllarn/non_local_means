#!/usr/bin/env python
# -*- coding:Utf-8 -*-


from math import exp
from Patch import *
from PIL import Image


class Denoiser:

	def __init__(self, filename):
		self.window_size = 5
		self.patch_size = 1
		self.noised_image = Image.open(filename)
		self.prepare_image()
		self.denoised_image = Image.new("""L""", (self.noised_image.size[0], self.noised_image.size[1]))
		self.patchs_array = [[]]
		self.closest_patchs_array = []
		self.closest_patchs_array_current_size = 0
		self.closest_patchs_array_maximum_size = 5
	# end def

	def compare_pictures(self):
		original_picture = Image.open("""pictures/original.png""")
		comparison = Image.new("""L""", (original_picture.size[0], original_picture.size[1]))

		for x in range(original_picture.width):
			for y in range(original_picture.height):
				pixel_o = original_picture.getpixel((x, y))
				pixel_d = self.denoised_image.getpixel((x, y))
				comparison.putpixel((x, y), abs(pixel_o[0] - pixel_d))
			# end for
		#end for

		comparison.save("""pictures/comparison.png""", """PNG""")
	# end def


	@staticmethod
	def display_image_details(image):
		print("""{ Format :""", image.format,
			  """; Mode :""", image.mode,
			  """; Size :""", image.size, """}""")

	# end def

	def get_index_of_maximal_distance(self, tab):
		index = 0
		maximum = tab[0][2]
		for i in range(1, len(tab)):
			if maximum < tab[i][2]:
				index = i
				maximum = tab[i][2]
			# end if
		# end for
		return index

	# end def

	def init_patchs_array(self, size):
		self.patchs_array = [[Patch((0, 0), 0,
									self.noised_image)] * self.denoised_image.height] * self.denoised_image.width

		for x in range(self.denoised_image.width):
			for y in range(self.denoised_image.height):
				self.patchs_array[x][y] = Patch((x, y), size, self.noised_image)
			# end for
		# end for

	# end def

	def prepare_image(self):
		if self.noised_image.mode != """L""":
			# Convert to a greyscale system
			self.noised_image = self.noised_image.convert("""L""")
		# end if

	# end def

	def denoise(self, x):
		for y in range(self.denoised_image.height):
			# Window width
			closest_patchs_array = []
			closest_patchs_array_current_size = self.closest_patchs_array_current_size
			closest_patchs_array_maximum_size = self.closest_patchs_array_maximum_size
			sum_weight = 0
			h = 100
			h = h ** 2
			for u in range(self.window_size):
				# Window height
				for t in range(self.window_size):
					if (
							x + u - ((self.window_size - 1) / 2) >= 0
							and y + t - ((self.window_size - 1) / 2) >= 0
							and x + u - ((self.window_size - 1) / 2) < self.denoised_image.width
							and y + t - ((self.window_size - 1) / 2) < self.denoised_image.height
					):
						tmp = self.patchs_array[x][y].compare_grid(
							self.patchs_array[x + u - int((self.window_size - 1) / 2)]
							[y + t - int((self.window_size - 1) / 2)]
						)

						if closest_patchs_array_current_size < closest_patchs_array_maximum_size:
							closest_patchs_array.append([x + u - int((self.window_size - 1) / 2),
														 y + t - int((self.window_size - 1) / 2),
														 exp(-tmp / h)])
							closest_patchs_array_current_size += 1
						# end if
						else:
							closest_patchs_array[self.get_index_of_maximal_distance(closest_patchs_array)] = [
								x + u - int((self.window_size - 1) / 2),
								y + t - int((self.window_size - 1) / 2), exp(-tmp / h)]
						# end else
					# end if
				# end for

			for n in closest_patchs_array:
				sum_weight += n[2]
			# end for

			pixel = 0

			for n in closest_patchs_array:
				weight = n[2] / sum_weight
				pixel += weight * self.noised_image.getpixel((n[0], n[1]))
			# end for

			pixel = (pixel + self.noised_image.getpixel((x, y))) / 2
			self.denoised_image.putpixel((x, y), int(pixel))

	def run(self, patch_size, window_size):

		self.init_patchs_array(patch_size)
		self.closest_patchs_array = []
		self.patch_size = patch_size
		self.window_size = window_size

		for x in range(self.denoised_image.width):
			self.denoise(x)
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
	denoiser.compare_pictures()
	denoiser.run(5, 9)
	denoiser.denoised_image.save("pictures/output.png", "PNG")
	denoiser.show("""input""")
	denoiser.show("""output""")
# end if
