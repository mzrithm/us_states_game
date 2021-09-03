from turtle import Turtle, Screen
import time


class Timer(Turtle):

    def __init__(self):
        super().__init__()
        self.message = ""
        self.start = time.time()
        self.limit = 600
        self.passed = time.time() - self.start
        self.on = True
        self.pencolor("black")
        self.hideturtle()
        self.broadcast()

    def broadcast(self):
        self.clear()
        self.penup()
        clock = self.limit - self.passed
        mins, secs = divmod(clock, 60)
        mins = int(mins)
        secs = int(secs)
        self.message = f"Minutes Remaining: {mins:02d}:{secs:02d}"
        self.check_time(clock)
        self.setposition(-215, -280)
        self.pendown()
        self.write(self.message, False, align="center", font=("Courier", 20, "bold"))

    def check_time(self, clock):
        if clock <= 0:
            self.on = False
            self.message = "GAME OVER"



