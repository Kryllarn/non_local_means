class Patch:

    def __init__(self, center):
        self.center = center  # center as a tuple(2) where center[0] is x, and center[1] is y
        self.half_size = 3  # default half size
        self.size = self.half_size * 2 + 1  # compute full size
        self.init_matrix(self)  # initialize patch content

    # end default __init__

    def __init__(self, center, half_size):
        self.center = center  # center as a tuple(2) where center[0] is x, and center[1] is y
        self.half_size = half_size  # default half size
        self.size = half_size * 2 + 1  # compute full size
        self.init_matrix(self)  # initialize patch content

    # end custom __init__

    def init_matrix(self):
        for i in range(self.size):
            [0] * self.size
        # end for
    # end init_matrix

# end class
