class complex:
    def __init__(self,real ,image):
        self.real = real
        self.image = image 

    def add(self,n):
        real = self.real + n.real
        image = self.image + n.image
        result = complex(real,image)
        return result    

n1 = complex(2,6)
n2 = complex(2,6)
result = n1.add(n2)
print(result.real)
print(result.image)