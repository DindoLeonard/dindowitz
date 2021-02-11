import turtle as t
from snake_mod import Snake
import time
from food import Food
from scoreboard import Scoreboard

# Screen main
screen = t.Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Shortcut for classes/functions
food = Food()
snake = Snake()
snake.create_snake()
scoreboard = Scoreboard()


# Game controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Main game
game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.add_piece()
    # Collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.reset()
        snake.reset()

    # Collision with tail
    for piece in snake.pieces[1:]:
        # This is SLICING method
        if snake.head.distance(piece) < 10:
            scoreboard.reset()
            snake.reset()

        # THIS METHOD IS NOT SLICING
        # if piece == snake.head:
        #     pass
        # elif snake.head.distance(piece) < 10:
        #     scoreboard.game_over()
        #     game = False

# Exit protocol
screen.exitonclick()
