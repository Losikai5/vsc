class polygon:
    def __init__(self,a,b,c,d):
        self.a = a 
        self.b = b 
        self.c = c 
        self.d = d 
      

    #def display_info(self):
     #   print("A POLYGON IS A 2 DIMESIONAL SHAPE WITH STRAIGHT LINES")

              
    def peremeter(self):
        p = [self.a,self.b,self.c,self.d]
        add = sum(p)
        return add
class Square(polygon):  
    pass
class Triangle(polygon):
    pass      

   

     
    

Square1 = Square(2,8,9,6)
print(Square1.peremeter())



t1 = Triangle(6,5,7,0)
print(t1.peremeter())





