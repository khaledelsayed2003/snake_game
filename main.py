"""snake game"""
from turtle import Turtle, Screen, turtles


screen = Screen()
parts_list = []


for part in range(3):
    snake_part = Turtle(shape="square")
    parts_list.append(snake_part)
    snake_part.penup()
    snake_part.color("black")
    

parts_list[1].backward(20)
parts_list[2].backward(40)



def move():
    for step in range(10):
        parts_list[2].forward(60)
        parts_list[1].forward(60)
        parts_list[0].forward(60)

       
        
move()













































screen.exitonclick()