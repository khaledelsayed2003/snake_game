"""snake game"""
from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake() # create an object called snake from the class Snake that we imported from the file snake.


screen.listen() #An event listeners
screen.onkey(key="a", fun=snake.turn_left)
screen.onkey(key="d", fun=snake.turn_right)
   
   


game_is_on = True 
while game_is_on:
    screen.update()
    time.sleep(0.05)
    
    snake.move()
    
     

   













screen.exitonclick()