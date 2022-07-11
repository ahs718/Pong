from Window import window
from Ball import Ball
from Paddle import Paddle

# Paddles
paddle1 = Paddle(-350, 0, "w", "s")
paddle2 = Paddle(350, 0, "Up", "Down")

# Ball
ball = Ball(3, 3)

# Main game Loop
while True:
    window.update()

    # Move ball & test collisions
    ball.moveBall()
    ball.checkBorder()
    ball.checkCollision(paddle1, paddle2)
