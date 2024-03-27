from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

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

# Scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    ball.move()
    screen.update()

    # Detect collision with top & bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()

    # Detect r_paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score()

    # Detect l_paddle misses ball
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_score()





screen.exitonclick()
