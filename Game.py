import turtle
from Window import window
from Ball import Ball
from Paddle import Paddle
from Score import Score

# Paddles
paddle1 = Paddle(-350, 0, "w", "s")
paddle2 = Paddle(350, 0, "Up", "Down")

# Ball
ball = Ball(3, 3)

# Score
Score.write(Score, paddle1, paddle2)

# Main game Loop
while True:
    window.update()

    # Move ball & test collisions
    ball.moveBall()
    ball.checkBorder(paddle1, paddle2)
    ball.checkCollision(paddle1, paddle2)
