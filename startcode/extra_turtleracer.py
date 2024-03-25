import turtle
import random

class TurtleRacer:
    def __init__(self, color, start_nummer):
        self.turtle = turtle.Turtle()
        self.turtle.shape("turtle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.goto((-200, 200-(start_nummer*30)))
        self.turtle.pendown()
        self.afstand = 0

    def race(self):
        random_afstand = random.randint(1, 25)
        self.afstand += random_afstand
        self.turtle.forward(random_afstand)

    def dans(self):
        self.turtle.left(360)
        self.turtle.right(360)


racers = [
    TurtleRacer("red", 1),
    TurtleRacer("blue", 2),
    TurtleRacer("green", 3)
]

# Start de race
for _ in range(25):
    for racer in racers:
        racer.race()

# Vind de winnaar
winnaar = None
max_afstand = 0
for racer in racers:
    if racer.afstand > max_afstand:
        max_afstand = racer.afstand
        winnaar = racer
winnaar.dans()


turtle.done()