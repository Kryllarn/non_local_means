import Grid


class Patch(Grid):

    def __init__(self, center, half_size, image):
        self.center = center                        # center as a tuple(2) where center[0] is x, and center[1] is y
        self.half_size = half_size                  # default half size
        self.abscissa_size = half_size * 2 + 1      # compute full size
        self.ordinate_size = half_size * 2 + 1      # compute full size
        self.grid = self.init_matrix()              # initialize patch content
        self.fill_grid(self.center, image)
    # end def

    def fill_grid(self, center, image):
        for x in range(self.abscissa_size):
            for y in range(self.ordinate_size):
                if (center[0] + x - self.half_size >= 0 and
                        center[1] + y - self.half_size >= 0 and
                        center[0] + x + self.half_size < image.width() and
                        center[1] + y + self.half_size < image.height()):
                    self.grid[x][y] = image.getPixel((x - self.half_size, y - self.half_size))
                # end if
            # end for
        # end for
    # end def

    def compare_grid(self, grid):
        distance = 0
        size = self.abscissa_size - 1
        for x in range(size):
            for z in range(size):
                if grid[x][z] != -1:
                    distance += abs(grid[x][z] - self.grid[x][z])
                # end if
            # end for
        # end for
        return distance
    # end def

# end class
