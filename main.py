from turtle import Screen
from scoreboard import ScoreBoard
from turtlemove import TurtleMove
from block import Block
import time

s=Screen()
score_board=ScoreBoard()
turtle_move=TurtleMove()
block=Block()
s.setup(600,610)
s.listen()
s.tracer(0)
while not turtle_move.boundary_reach:
    time.sleep(0.2)
    s.update()
    s.onkey(turtle_move.forward,"Up")
    if turtle_move.ycor()>270:
        score_board.level+=1
        score_board.score()
        turtle_move.turtle_reset()
        if block.block_speed<=9:
            block.block_speed+=1
    for i in block.block_list:
        if abs(turtle_move.xcor()-i.xcor())<30 and abs(turtle_move.ycor()-i.ycor())<10:
            print("touch")
            score_board.game_over()
            turtle_move.boundary_reach=True
    block.initialize()
s.exitonclick()