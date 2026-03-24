from turtle import Turtle

# Clase Snake
class Snake:

    def __init__(self, color, shape):
        self.segments = []
        self.color = color
        self.shape = shape
        self.create_snake()

    # Serpiente 
    # Usamos segmentos
    def create_snake(self):
        head = Turtle(self.shape)
        head.color(self.color)
        head.shapesize(1.2, 1.2)
        head.penup()        # Desactiva el rastro del movimiento 
        head.goto(0, 0)     # Inicio de la serpiente en el centro del panel
        self.segments.append(head)

    def move(self):
        # Movimiento del cuerpo
        if len(self.segments) > 1:
            for i in range(len(self.segments) -1, 0, -1):   # Recorremos la lista desde el final
                self.segments[i].goto(
                    self.segments[i-1].xcor(),
                    self.segments[i-1].ycor()
                )

        # Movimiento cabeza
        self.segments[0].forward(20)

    def grow(self):
        new_body = Turtle(self.shape)
        new_body.color(self.color)
        new_body.shapesize(0.9, 0.9)
        new_body.penup()
        self.segments.append(new_body)

    def head(self):
        return self.segments[0]

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()

        self.segments.clear()
        self.create_snake()