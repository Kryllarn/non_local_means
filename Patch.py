from Grid import *


class Patch(Grid):

    def __init__(self, center, half_size, image):
        Grid.__init__(self, half_size * 2 + 1, half_size * 2 + 1)
        self.center = center
        self.half_size = half_size
        self.fill_grid(self.center, image)
    # end def

    def fill_grid(self, center, image):
        for x in range(self.abscissa_size):
            for y in range(self.ordinate_size):
            #    print("""GRILLE""", """x""", x, """y""", y, """pixel""", self.grid[x][y])
             #   print("""IMAGE""", """x""", x, """y""", y, """pixel""", image.getpixel((x, y)))

                # if (
                #     center[0] - x - (self.abscissa_size - 1) / 2 >= 0
                #     and center[1] - y - (self.ordinate_size - 1) / 2 >= 0
                #     and center[0] + x + (self.abscissa_size - 1) / 2 < image.width
                #     and center[1] + y + (self.ordinate_size - 1) / 2 < image.height
                #):

                if (center[0] + x - self.half_size >= 0 and
                    center[1] + y - self.half_size >= 0 and
                    center[0] + x - self.half_size < image.width and
                    center[1] + y - self.half_size < image.height):
                    self.grid[x][y] = image.getpixel((center[0] + x - self.half_size, center[1] + y - self.half_size))
                    #print(self.grid[x][y])
                #print(self.grid[x][y],", ", self.grid[x][y])
                 #end if

                # print("""x""", x, """y""", y, """pixel""", self.grid[x][y])
                # if (
                #     # Check abscissa
                #         (center[0] - x >= 0)
                #     and (center[0] - x >= center[0] - self.half_size)
                #     and (center[0] + x < image.width)
                #     and (center[0] + x < center[0] + self.half_size)
                #     # Check ordinate
                #     and (center[1] - y >= 0)
                #     and (center[1] - y >= center[1] - self.half_size)
                #     and (center[1] + y < image.height)
                #     and (center[1] + y < center[1] + self.half_size)
                # ):
                #     self.grid[x][y] = image.getpixel((x, y))

                # if (center[0] + x - self.half_size >= 0 and
                #         center[1] + y - self.half_size >= 0 and
                #         center[0] + x + self.half_size < image.width and
                #         center[1] + y + self.half_size < image.height):
                #     self.grid[x][y] = image.getpixel((x - self.half_size, y - self.half_size))
                # # end if
            # end for
        # end for
    # end def

    def compare_grid(self, grid):
        distance = 0
        for x in range(self.abscissa_size):
            for y in range(self.ordinate_size):
                # if grid[x][y] != -1:
                if (
                    type(grid) is Patch
                    and grid.grid[x][y] != -1
                    and self.grid[x][y] != -1
                ):
                    # print("on passe dedans")
                    distance += abs(grid.grid[x][y] - self.grid[x][y])
                # end if
            # end for
        # end for
        return distance
    # end def

# end class
