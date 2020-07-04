class Point(object):

    #__slots__ = ['x', 'y']
    def __init__(self, x, y):
        #self.x = x
        #self.y = y
        self.data = [x, y]

    def getX(self):
        #return self.x
        return self.data[0]

    def getY(self):
        #return self.y
        return self.data[1]

    def __getitem__(self, item):
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value

    @property
    def x(self):
        return self.data[0]

    @property
    def y(self):
        return self.data[1]

    @x.setter
    def x(self, value):
        self.data[0] = value

    @y.setter
    def y(self, value):
        self.data[1] = value

    # need to compare two lists of points