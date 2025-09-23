'''

Q2: Write a class "calculator" capable of finding square, cube and squareroot of a number.
 # Adding static method.
''' 


class calculator :

    def __init__(self, n,):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareRoot(self):
        print(f"The square root is {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello there")
a = calculator(10)
a.hello()
a.square()
a.cube()
a.squareRoot()