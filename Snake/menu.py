from turtle import Turtle

# Clase Menu
class Menu:

    def __init__(self):
        self.menu = Turtle()
        self.menu.hideturtle()
        self.menu.penup()
        self.menu.color("white")

        # Valores seleccionados
        self.vel = None # Se asigna despues con set_easy
        self.color = "lime"
        self.shape = "square"
        self.in_menu = True
        self.set_easy()

    def draw(self):
        self.menu.clear()

        self.menu.goto(0, 120)
        self.menu.write("🐍  SNAKE GAME  🐍", align="center", font=("Arial", 30, "bold"))

        # marcar seleccion
        if self.vel == 0.15:
            dificultad = "[FACIL]"
        elif self.vel == 0.10:
            dificultad = "[NORMAL]"
        else:
            dificultad = "[DIFICIL]"

        self.menu.goto(0, 40)
        self.menu.write(f"1 - Facil   2 - Normal   3 - Dificil",
                        align="center", font=("Arial", 16, "normal"))

        self.menu.goto(0, 10)
        self.menu.write(f"Dificultad actual: {dificultad}",
                        align="center", font=("Arial", 14, "bold"))

        self.menu.goto(0, -20)
        self.menu.write("C - Cambiar color   F - Cambiar forma",
                        align="center", font=("Arial", 16, "normal"))

        self.menu.goto(0, -60)
        self.menu.write("ENTER - Jugar",
                        align="center", font=("Arial", 18, "bold"))

        self.menu.goto(0, -100)
        self.menu.write(f"Color: {self.color}   Forma: {self.shape}",
                        align="center", font=("Arial", 14, "normal"))

    # Dificultades 
    # Los valores se asignan en segundos, mayor vlaor, mas lento
    def set_easy(self):
        self.vel = 0.15

    def set_normal(self):
        self.vel = 0.10

    def set_hard(self):
        self.vel = 0.06

    # Cambiar color
    def change_color(self):
        colores = ["lime", "cyan", "yellow", "white"]
        i = colores.index(self.color)
        self.color = colores[(i + 1) % len(colores)]

    # Cambiar forma
    def change_shape(self):
        formas = ["square", "circle", "arrow", "turtle"]
        i = formas.index(self.shape)
        self.shape = formas[(i + 1) % len(formas)]

    def start(self):
        self.in_menu = False