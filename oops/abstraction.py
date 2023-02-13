from abc import ABC,abstractmethod
#abstract class
class polygen(ABC):
    #abstract methodd
    @abstractmethod
    def sides(self):
        pass
    def display(self):
        print("non abstract method")
class Triangle(polygen):
    def sides(self):
        print("triangle has 3 sides")
ob=Triangle()
ob.sides()
ob.display()