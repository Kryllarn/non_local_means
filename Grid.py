class Grid:

    def __init__(self, abscissa_size, ordinate_size, center, image):
        self.abscissa_size = abscissa_size
        self.ordinate_size = ordinate_size
        self.grid = self.init_grid()
    # end def

    def init_grid(self):
        grid = [[]]
        for x in range(self.abscissa_size):
            for y in range(self.ordinate_size):
                grid[x][y] = -1
        return grid
    # end def

# end class
