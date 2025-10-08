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
    
    
    
def turn_left():
    segments_list[0].left(90)
def turn_right():
    segments_list[0].right(90)    
    
    
screen.listen()
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)


game_is_on = True 
while game_is_on:
    screen.update()
    time.sleep(0.05)
    
    for l_two_segment in range(len(segments_list)-1, 0, -1):
        segments_list[l_two_segment].goto(segments_list[l_two_segment-1].pos())
           
    segments_list[0].forward(20)
        

   






























screen.exitonclick()