from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area():
        pass        
class Rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("Area of Rectangle :",(self.l*self.b))
class Cirlce(shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print("Area of the circle :",3.14*(self.r**2))
r1=Rectangle(2,2)
r1.area()
c1=Cirlce(2)
c1.area()