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
                if (
                    center[0] + x - self.half_size >= 0
                    and center[1] + y - self.half_size >= 0
                    and center[0] + x - self.half_size < image.width
                    and center[1] + y - self.half_size < image.height
                ):
                    self.grid[x][y] = image.getpixel((center[0] + x - self.half_size, center[1] + y - self.half_size))
                 # end if
        # end for
    # end def

    def compare_grid(self, grid):
        distance = 0
        for x in range(self.abscissa_size):
            for y in range(self.ordinate_size):
                if (
                    type(grid) is Patch
                    and grid.grid[x][y] != -1
                    and self.grid[x][y] != -1
                ):
                    distance += abs(grid.grid[x][y] - self.grid[x][y]) ** 2
                # end if
            # end for
        # end for
        return distance
    # end def

# end class
