class rectangle:
    def __init__(self,length,width):
        self.width = width
        self.length = length


class square(rectangle):
    def __init__(self,length,width):
        super().__init__(width,length)
    def area(self):
        return self.length*self.width


class cube(rectangle):
    def __init__(self,length,width,height):
        self.height = height
        super().__init__(length,width)
    def volume(self):
        return self.length*self.width*self.height


square1 = square(4,6)
cube1 = cube(4,5,2)        
print(square1.area())
print(cube1.volume())