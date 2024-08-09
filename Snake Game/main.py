from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


def game():
    # This snake eats turtles
    # Mandotary stuffs
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("light sea green")
    screen.title("Rakin's Snake Game")
    screen.tracer(0)

    # objects
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()

    # User input
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")


    # Game life
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
    
    
    screen.update()
    time.sleep(0.5)

    screen.clear()
    screen.bgcolor("light sea green")
    screen.title("Rakin's Snake Game")
    time.sleep(1)
    screen.tracer(0)
    scoreboard.clear()
        
    def ask_play_again():
        screen.clear()
        screen.bgcolor("light sea green")
        screen.title("Play Again?")
        screen.tracer(0)
        screen.update()
        answer = screen.textinput("Game Over", "Do you want to play again? (yes/no)")

        if answer.lower() == "yes":
            game()
        else:
            screen.bye()
            screen.exitonclick()  # Close the game window
    
    ask_play_again()

game()

screen = Screen()
screen.exitonclick()
