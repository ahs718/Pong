import turtle


# Score Module
class Score:
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)

    def write(self, paddle1, paddle2) -> None:
        self.pen.clear()
        self.pen.write(f"Player 1: {paddle1.score}  Player 2: {paddle2.score}",
                       align="center", font=("Courier", 24, "normal"))
