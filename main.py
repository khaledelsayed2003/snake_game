"""snake game"""
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments_list = []
screen.tracer(0)

for part in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(part) #to move it to that exact position x and y axis.
    segments_list.append(new_segment)
    
   
game_is_on = True 
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments_list:
        seg.forward(20)




# screen.update()
# time.sleep(0.3) 



# segments_list[2].forward(20)
# segments_list[1].forward(20)
# segments_list[0].left(90)
# segments_list[0].forward(20)
# screen.update()
# time.sleep(0.3)
# segments_list[2].forward(20)
# segments_list[1].left(90)
# segments_list[1].forward(20)
# segments_list[0].forward(20)
# screen.update()
# time.sleep(0.3)



# segments_list[2].left(90)
# segments_list[2].forward(20)
# segments_list[1].forward(20)
# segments_list[0].left(90)
# segments_list[0].forward(20)
# screen.update()
# time.sleep(2)
# segments_list[2].forward(20)
# segments_list[1].left(90)
# segments_list[1].forward(20)
# segments_list[0].forward(20)
# screen.update()
# time.sleep(0.3)



# segments_list[2].left(90)
# segments_list[2].forward(20)
# segments_list[1].forward(20)
# segments_list[0].left(90)
# segments_list[0].forward(20)
# screen.update()
# time.sleep(0.3)
# segments_list[2].forward(20)
# segments_list[1].left(90)
# segments_list[1].forward(20)
# segments_list[0].forward(20)
# screen.update()
# time.sleep(0.3)


# segments_list[2].left(90)
# segments_list[2].forward(20)
# segments_list[1].forward(20)
# segments_list[0].left(90)
# segments_list[0].forward(20)
# screen.update()
# time.sleep(0.3)
# segments_list[2].forward(20)
# segments_list[1].left(90)
# segments_list[1].forward(20)
# segments_list[0].forward(20)
# screen.update()
# time.sleep(0.3)


























screen.exitonclick()