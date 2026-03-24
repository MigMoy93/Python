from turtle import Turtle
import random

# Clase comida
class Food(Turtle):

    def __init__(self, color):
        super().__init__("circle")
        self.color(color)
        self.penup()
        self.move()

    def move(self):
        # Transformacion para crear una cuadricula
        posX = random.randint(-19, 19) * 20
        posY = random.randint(-14, 14) * 20
        self.goto(posX, posY)