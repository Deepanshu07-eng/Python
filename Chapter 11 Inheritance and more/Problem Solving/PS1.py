'''
Q1-> Create a class (2-D vector) and use it to create another class representing a 
     3-D Vector.
     
'''

class TwoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is  {self.i}i + {self.j}j")


class ThreeDvector(TwoDvector):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The vector is  {self.i}i + {self.j}j + {self.k}k")


a = TwoDvector(21,41)
a.show()
b = ThreeDvector(42,53,81)
b.show()