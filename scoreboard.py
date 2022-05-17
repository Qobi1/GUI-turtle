from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.level()

    def level(self):
        self.goto(-220, 250)
        self.write(arg=f'Level: {self.score}', align='center', font=("arial", 20, 'bold'))

    def increase_level(self):
        self.goto(-220, 250)
        self.clear()
        self.score += 1
        self.write(arg=f'Level: {self.score}', align='center', font=("Arial", 20, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align='center', font=("Arial", 20, 'bold'))