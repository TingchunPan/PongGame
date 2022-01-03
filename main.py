
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreBoard import Scoreboard
import time

wn=Screen()
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)
wn.title("Pong Game")

paddle_r=Paddle((370,0))
paddle_l=Paddle((-370,0))

ball=Ball()
scoreBoard=Scoreboard()

wn.listen()
wn.onkey(paddle_r.go_up,"Up")
wn.onkey(paddle_r.go_down,"Down")
wn.onkey(paddle_l.go_up,"Left")
wn.onkey(paddle_l.go_down,"Right")
game_start=True

while game_start:
    time.sleep(ball.speed)
    wn.update()
    ball.move()
#detect wall
    if ball.ycor()>280 or ball.ycor() <-280:
      ball.bounce_y()
    if ball.distance(paddle_r) < 50 and ball.xcor() > 340 or ball.distance(paddle_l) < 50 and ball.xcor() < -340:
        ball.bounce_x()
#detect R misses
    if ball.xcor() > 380:
        ball.reset_direction()
        scoreBoard.add_l_score()
#detect L misses
    if ball.xcor() < -380:
        ball.reset_direction()
        scoreBoard.add_r_score()
wn.exitonclick()