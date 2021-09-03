from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.value = 50
        self.pencolor("black")
        self.hideturtle()
        self.broadcast()

    def broadcast(self):
        self.clear()
        self.penup()
        score_message = f"U.S. States Remaining: {self.value}"
        self.setposition(200, 260)
        self.pendown()
        self.write(score_message, False, align="center", font=("Courier", 20, "bold"))

    def count(self, num):
        self.value = self.value - num


