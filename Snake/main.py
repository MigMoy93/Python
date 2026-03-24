from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard
from menu import Menu
from sound import sound_eat, sound_die


# -------------------------
# Estado del juego
# -------------------------
class GameState:
    def __init__(self):
        self.direction = "RIGHT"   # direccion inicial
        self.paused = False
        self.cambio_permitido = True


state = GameState()


# -------------------------
# Controles — solo cambian estado, no tocan la serpiente
# -------------------------
def up():
    if state.cambio_permitido and state.direction != "DOWN":
        state.direction = "UP"
        state.cambio_permitido = False

def down():
    if state.cambio_permitido and state.direction != "UP":
        state.direction = "DOWN"
        state.cambio_permitido = False

def left():
    if state.cambio_permitido and state.direction != "RIGHT":
        state.direction = "LEFT"
        state.cambio_permitido = False

def right():
    if state.cambio_permitido and state.direction != "LEFT":
        state.direction = "RIGHT"
        state.cambio_permitido = False

def toggle_pause():
    state.paused = not state.paused


# -------------------------
# Pantalla
# -------------------------
screen = Screen()
screen.bgcolor("#111111")
screen.setup(width=800, height=600)
screen.title("🐍  Snake Game  🐍")
screen.tracer(0)


# -------------------------
# Menú
# -------------------------
menu = Menu()

screen.listen()
screen.onkey(menu.set_easy, "1")
screen.onkey(menu.set_normal, "2")
screen.onkey(menu.set_hard, "3")
screen.onkey(menu.change_color, "c")
screen.onkey(menu.change_shape, "f")
screen.onkey(menu.start, "Return")

while menu.in_menu:
    menu.draw()
    screen.update()
menu.menu.clear()


# -------------------------
# Juego
# -------------------------
snake = Snake(menu.color, menu.shape)
food = Food("red")
scoreboard = Scoreboard()

vel = menu.vel

# Controles juego
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(toggle_pause, "space")

# Mapa de direccion a heading
HEADINGS = {
    "UP": 90,
    "DOWN": 270,
    "LEFT": 180,
    "RIGHT": 0,
}

game_on = True

while game_on:

    screen.update()
    time.sleep(vel) # En segundos

    if state.paused:
        continue

    # Aplicar direccion a la serpiente
    snake.head().setheading(HEADINGS[state.direction])
    snake.move()

    # Detectar toque con comida
    if snake.head().distance(food) < 20:
        sound_eat()
        food.move()
        snake.grow()
        scoreboard.increase()
        vel = max(vel * 0.95, 0.03)   # reduce el sleep al comer, mínimo 0.03s

    head = snake.head()

    # Detectar paredes
    if abs(head.xcor()) > 380 or abs(head.ycor()) > 280:
        sound_die()
        scoreboard.game_over()
        screen.update()
        time.sleep(3)
        snake.reset()
        scoreboard.reset()
        state.direction = "RIGHT"   # resetear direccion
        vel = menu.vel              # vuelve a la velocidad inicial de la dificultad elegida

    # Detectar choque con el cuerpo
    # Bucle for apartir de la pos 1, ignora la cabeza (primer segmento)
    for segment in snake.segments[1:]:
        if head.distance(segment) < 10:
            sound_die()
            scoreboard.game_over()
            screen.update()
            time.sleep(3)
            snake.reset()
            scoreboard.reset()
            state.direction = "RIGHT"   # resetear direccion
            vel = menu.vel

    state.cambio_permitido = True


screen.exitonclick()