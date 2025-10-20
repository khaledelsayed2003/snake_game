from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        with open("snake_game/data.txt", "r") as file:  # Read the high score from data file (I)
            self.high_score = int(file.read())
        self.score = 0
        self.color("yellow")
        self.hideturtle()
        self.penup()
        self.goto(0, 255)
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        self.clear()    # to delete the previous score
        self.write(f"Score: {self.score} High Score: {self.high_score}", align= "center", font=("Arial", 25, "normal"))
        
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
     
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_game/data.txt", "w") as file:  # save the high score into the data file (O)
                file.write(f"{self.high_score}") 
        self.score = 0 
        self.update_scoreboard()
               
             
