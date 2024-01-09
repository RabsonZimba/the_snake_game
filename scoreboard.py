from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.score = 0
        self.color("white")
        self.write(f"Score:{self.score}", align="center", font=('Arial', 12, 'normal'))
        self.hideturtle()

    def count_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 12, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align="center", font=('Arial', 18, 'normal'))

