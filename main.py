"""snake game"""
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time
from random import randint


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
user_input = screen.textinput(title="Welcome to the snake game!", prompt="Type 'y' to start the game: ").lower()

snake = Snake() # create an object called snake from the class Snake that we imported from the file snake.
food = Food()
score = Score()

screen.listen() #An event listeners
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
   
   


game_is_on = False 

if user_input == 'y':
    game_is_on = True
else:
    print("Sorry you typed an invalid option! Pls type 'y' if you want to play!")

while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    
    if snake.segments_list[0].distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
    
    # Detect Collisions with the Wall
    if snake.segments_list[0].xcor() >= 285 or snake.segments_list[0].xcor() <= -285 or snake.segments_list[0].ycor() >= 285 or snake.segments_list[0].ycor() <= -285:
        score.reset()
        snake.reset()
        time.sleep(0.2)    
        
    # Detect Collisions with the the tail
    for segment in snake.segments_list[1:]:   # to slice the list and start comparing from any part after the head(index 0).
        if snake.segments_list[0].distance(segment) < 10:
            score.reset()
            snake.reset()
            time.sleep(0.2)
          
    
     

   













screen.exitonclick()