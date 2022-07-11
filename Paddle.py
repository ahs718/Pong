import turtle
from Window import window


# Paddle Class
class Paddle:
    # Initial Setup
    def __init__(self, x, y, upKey, downKey) -> None:
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x, y)
        self.upKey = upKey
        self.downKey = downKey

        # Keyboard binding
        window.onkeypress(self.paddleUp, upKey)
        window.onkeypress(self.paddleDown, downKey)

    # Paddle movement controls
    def paddleUp(self) -> None:
        y = self.paddle.ycor()
        y += 20
        self.paddle.sety(y)

    def paddleDown(self) -> None:
        y = self.paddle.ycor()
        y -= 20
        self.paddle.sety(y)
