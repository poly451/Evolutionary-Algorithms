"""
    ===================================
                 class Tile
    ===================================
"""

class Tile:
    def __init__(self, x, y, contents):
        # print("in tile, contents are of type: {}".format(type(contents)))
        if not isinstance(contents, str):
            print("contents ({}) are NOT of type string. They are of type: {}".format(contents), type(contents))
            pygame.quit()
            sys.exit("Error in class Tile. Contents were not of type str.")
        self._x = x
        self._y = y
        self._contents = contents
        self.neighbors = []

    @property
    def contents(self):
        temp = []
        temp.append(self._x)
        temp.append(self._y)
        temp.append(self._contents)
        return temp

    @contents.setter
    def contents(self, value):
        # I've changed my mind, there is no reason x or y should ever be changed.
        # read/accessed, sure, but not changed.
        # if not isinstance(value, list):
        #     print("value ({}) is NOT of type list. It is of type: {}".format(value), type(value))
        #     pygame.quit()
        #     sys.exit("Error in class Tile in def contents (property setter). Contents were not of type list.")
        # if not isinstance(value[0], int):
        #     raise ValueError("Contents ({}) are not of type int. They are of type ({}).".format(value[0], type(value[0])))
        # if not isinstance(value[1], int):
        #     raise ValueError("Contents ({}) are not of type int. They are of type ({}).".format(value[1], type(value[1])))
        if not isinstance(value, str):
            raise ValueError("Contents ({}) are not of type str. They are of type ({}).".format(value, type(value)))
        # self._x = value[0]
        # self._y = value[1]
        self._contents = value

    def drop_neighbors(self):
        self.neighbors = []

    def has_neighbors(self):
        if len(self.neighbors) > 0:
            return True
        return False

    # def get_nothing_tile(self):
    #     new_tile = Tile(-1, -1, "nothing")
    #     new_tile.neighbors = []
    #     return new_tile

    def debug_print(self):
        print_string = "{}-{}-{}-[{}] || ".format(self._x, self._y, self._contents, len(self.neighbors))
        # print_string = "{}-{}-{} || ".format(self._x, self._y, self._contents)
        print(print_string)

    def return_string(self):
        # print("{}-{}-{}".format(self._x, self._y, self._contents))
        return "{}-{}-{}-[{}] || ".format(self._x, self._y, self._contents, len(self.neighbors))
