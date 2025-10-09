from turtle import Turtle
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
Move_distance = 20
left_direction = 180
right_direction = 0
up_direction = 90
down_direction = 270


class Snake:
    
    def __init__(self):
        self.segments_list = []
        self.create_snake()

    def create_snake(self):
        for part in starting_positions:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(part) #to move it to that exact position x and y axis.
            self.segments_list.append(new_segment)
            
            
    def move(self):
        for l_two_segment in range(len(self.segments_list)-1, 0, -1):
            self.segments_list[l_two_segment].goto(self.segments_list[l_two_segment-1].pos())
           
        self.segments_list[0].forward(Move_distance)
        
        
    def turn_left(self):
        if self.segments_list[0].heading() != right_direction:
            self.segments_list[0].setheading(left_direction)

    def turn_right(self):
        if self.segments_list[0].heading() != left_direction:
            self.segments_list[0].setheading(right_direction)
        
    def move_up(self):
        if self.segments_list[0].heading() != down_direction:
            self.segments_list[0].setheading(up_direction)
       
    def move_down(self):
        if self.segments_list[0].heading() != up_direction:
            self.segments_list[0].setheading(down_direction)
         
        
        