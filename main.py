from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Move Paddles
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Ball
ball = Ball()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()


screen.exitonclick()
