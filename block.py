from turtle import Turtle
from random import random,randint

class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.block_list=[]
        self.block_speed=1
        

    def initialize(self):
        self.create()
    
    def create(self):
        t=Turtle()
        t.color("white")
        t.penup()
        t.shape("square")
        t.shapesize(1,2)
        t.x=280
        t.y=randint(-260,260)
        t.setpos(t.x,t.y)
        t.color(random(),random(),random())
        t.speed(0.6)
        self.block_list.append(t)
        self.move()

    def move(self):
        for i in self.block_list:
            i.x-=20
            i.goto(i.x,i.y)
            i.speed(self.block_speed)
            # i.speed(0.6)