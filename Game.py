import turtle
from Window import window
from Ball import Ball
from Paddle import Paddle

# Paddles
paddle1 = Paddle(-350, 0, "w", "s")
paddle2 = Paddle(350, 0, "Up", "Down")

# Ball
ball = Ball(3, 3)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))

# Main game Loop
while True:
    window.update()

    # Move ball & test collisions
    ball.moveBall()
    ball.checkBorder()
    ball.checkCollision(paddle1, paddle2)
