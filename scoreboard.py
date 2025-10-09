from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(0, 255)
        self.write(f"Score: {self.score}", align= "center", font=("Arial", 25, "normal"))
        
    
    
    def refresh(self):
        self.clear()    # to delete the previous score
        self.score += 1
        self.write(f"Score: {self.score}", align= "center", font=("Arial", 25, "normal")) 
        
         
