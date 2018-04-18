import math
class Vektor():
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, ovek):
        return Vektor(self.x - ovek.x, self.y - ovek.y)
    
    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5
    
    def add(self, nvek):
        return Vektor(self.x + nvek.x , self.y + nvek.y)

    def negate(self):
        return Vektor(-self.x, -self.y)

    def sign(self):
        x = 0
        y = 0
        if(self.x > 0):
            x = 1
        if(self.x < 0):
            x = -1

        if(self.y > 0):
            y = 1
        if(self.y < 0):
            y = -1
        return Vektor(x,y)

    def isBeyond(self, limvek):
        return limvek.add(self.negate()).sign()

    def nicolesAngle(self, darkestVek, radius):
        dist = self.add(darkestVek.negate())
        sign = dist.sign().y
        return 90 - (sign * math.degrees(dist.magnitude() * (2.54 / 72)) * (1 / radius) )
