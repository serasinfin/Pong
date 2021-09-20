from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# Start window game
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Class init
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Paddle controls
screen.listen()
# Right paddle control
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# Left paddle control
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Game loop
game_is_on = True
while game_is_on:
	time.sleep(ball.move_speed)
	screen.update()
	ball.move()

	# Detect collision with wall
	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()

	# Detect collision with paddle
	if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
		ball.bounce_x()

	# Detect R paddle misses
	if ball.xcor() > 380:
		ball.reset_position()
		scoreboard.l_point()

	# Detect R paddle misses
	if ball.xcor() < -380:
		ball.reset_position()
		scoreboard.r_point()

screen.exitonclick()
