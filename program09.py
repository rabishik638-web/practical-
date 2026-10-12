class complex:

    def __init__(self, x=0.0, y=0.0):

        self.real = x
        self.img = y

    def __add__(self, c2):

        c3 = complex(0)

        c3.real = self.real + c2.real
        c3.img = self.img + c2.img

        return c3

    def __Sub__(self, c2):

        c3 = complex(0)

        c3.real = self.real - c2.real
        c3.img = self.img - c2.img

        return c3

    def display(self):

        print(self.real, "+", self.img, "i")


c1 = complex(120, 70)
c2 = complex(5.0, 6.0)

c3 = c1 + c2

print("Complex number addition result:")

print("c1 =", end=" ")
c1.display()

print("\nc2 =", end=" ")
c2.display()

print("c3 =", end=" ")
c3.display()

c4 = c1.__Sub__(c2)

print("\nComplex number subtraction result:")
c4.display()