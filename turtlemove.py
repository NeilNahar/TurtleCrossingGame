from turtle import Turtle

class TurtleMove(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.shape("turtle")
        self.setpos(0,-280)
        self.left(90)
        self.boundary_reach=False
        
    def forward(self):
        if self.ycor()<=280:
            self.fd(20)
    
    def turtle_reset(self):
        self.setpos(0,-280)