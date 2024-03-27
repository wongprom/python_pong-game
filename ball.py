from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")

    def move(self):
        new_y = self.ycor() + 10
        new_x = self.xcor() + 10
        self.goto(x=new_x, y=new_y)
