from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = 0
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
        self.score = 0 
        self.update_scoreboard()
               
             
