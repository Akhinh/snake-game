from turtle import Turtle
ALIGNMENT = "center"
FONT = ('arial', 9, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        # this line of code is introduce, to keep record of the high_score after closing the game
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.color("white")
        self.goto(0, 285)
        self.write(f"score = {self.score}   high_score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def update(self):
        if self.score > self.high_score:
            self.high_score = self.score
            # write mode is used to update the high_score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scores()

    def refresh(self):
        self.score += 1
        self.update_scores()


