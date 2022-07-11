import turtle
from Score import Score


# Ball Class
class Ball:
    # Initial Setup
    def __init__(self, dx, dy) -> None:
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.dx = dx
        self.dy = dy

    # Move the ball
    def moveBall(self) -> None:
        self.ball.setx(self.ball.xcor() + self.dx)
        self.ball.sety(self.ball.ycor() + self.dy)

    # Border checking
    def checkBorder(self, paddle1, paddle2) -> None:
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.dy *= -1

        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.dy *= -1

        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            self.dx *= -1
            paddle1.score += 1
            Score.write(Score, paddle1, paddle2)

        if self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.dx *= -1
            paddle2.score += 1
            Score.write(Score, paddle1, paddle2)

    # Paddle and ball collision
    def checkCollision(self, paddle1, paddle2) -> None:
        if (self.ball.xcor() < -340) and (self.ball.xcor() > -350) and (self.ball.ycor() < paddle1.paddle.ycor() + 40) and (self.ball.ycor() > paddle1.paddle.ycor() - 40):
            self.ball.setx(-340)
            self.dx *= -1

        if (self.ball.xcor() > 340) and (self.ball.xcor() < 350) and (self.ball.ycor() < paddle2.paddle.ycor() + 40) and (self.ball.ycor() > paddle2.paddle.ycor() - 40):
            self.ball.setx(340)
            self.dx *= -1
