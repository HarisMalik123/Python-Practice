from turtle import Screen,Turtle
from snake import Snake
import time
import random
file=open("data.txt")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        
        self.highscore=int(file.read())
        file.close()
        self.goto(0,280)
        self.color("white")
        self.hideturtle()
        self.w()
    def reset(self):
        
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt","w") as f:
                f.write(f"{self.highscore}")
        self.score=0
        self.w()
    def w(self):
        self.clear()
        self.write(f"Score : {self.score} High Score {self.highscore}" ,align="center",font=("Arial",12,"normal"))
    def increase_score(self):
        
        self.score=self.score+1
        self.w()
   
        
    
    
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("pink")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        random_x=random.randint(-280,280)
        random_y=random.randint(-280,280)
        self.goto(random_x,random_y)
    
        
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
f=Food()
s=Score()
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(f)<15:
        f.refresh()
        s.increase_score()
        snake.extend()
    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        s.reset()
        snake.reset()
    for segment in snake.segments[1:]:
         if snake.head.distance(segment) < 10:
             s.reset()
             snake.reset()

           

screen.exitonclick()
