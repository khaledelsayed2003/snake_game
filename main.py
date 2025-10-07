"""snake game"""
from turtle import Turtle, Screen, turtles

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
parts_list = []

for part in starting_positions:
    snake_part = Turtle(shape="square")
    snake_part.color("white")
    snake_part.penup()
    snake_part.goto(part) #to set the position of that square
    parts_list.append(snake_part)
    
    

def move():
    for step in range(4):
        parts_list[2].forward(60)
        parts_list[1].forward(60)
        parts_list[0].forward(60)

       
        
move()













































screen.exitonclick()