import turtle
import random

class Trutleracer:
    def __init__(self, kleur, index):
        self.kleur = kleur
        self.index = index
        self.turtle = turtle.Turtle()
        self.turtle.shape('turtle')
        self.turtle.color(self.kleur)
        self.turtle.penup()
        self.turtle.goto(x=-200, y=-200 - (index * 30))
        self.turtle.pendown()

    def race(self):
        random_stap = random.randint(1,25)
        self.turtle.forward(random_stap)

racers = [
    Trutleracer("red", 1),
    Trutleracer("blue", 2),
    Trutleracer("green", 3)
    ]

for i in range(25):
    for racer in racers:
        racer.race()

turtle.done()