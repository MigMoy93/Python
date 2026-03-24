from turtle import Turtle

# Clase marcador
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)     # arriba del todo
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}  High: {self.highscore}",
                   align="center", font=("Arial", 20, "normal"))

    def increase(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

        self.score = 0
        self.goto(0, 260)   
        self.update()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("💀💥   GAME OVER   💥💀", align="center", font=("Arial", 26, "normal"))