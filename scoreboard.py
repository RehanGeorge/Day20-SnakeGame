from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        with open("data.txt") as data:
            self.high_score = data.read()
        self.speed("fastest")
        self.setposition(0, 265)
        self.color("White")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.points} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.points += 1
        self.update_scoreboard()

    def reset(self):
        if self.points > int(self.high_score):
            self.high_score = self.points
            with open("./data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.points = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.setposition(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
