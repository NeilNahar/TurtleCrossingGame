from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level=1
        self.score()
    
    def score(self):
        self.clear()
        self.update_score()
        
    def update_score(self):
        self.setpos(-280,270)
        self.write(f"Level: {self.level}",font=('Arial', 12, 'normal'))

    def game_over(self):
        self.clear()
        self.setpos(0, 0)
        self.write("Game Over",  align="center", font=('Arial', 12, 'normal'))
        self.update_score()