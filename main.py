from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(500, 400) # Screen setup
user_bit = screen.textinput(title="Make your bit", prompt="Which turtle will win the race? Enter a color:")
print(user_bit)

turtle_colors = ("red","yellow","green","blue","purple","pink")
y_position =[-70, -40, -10, 20, 50, 80]
all_turtle = []

for i in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(turtle_colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtle.append(new_turtle)


if user_bit:
    is_race_on = True

while is_race_on:
    for turtles in all_turtle:
        if turtles.xcor() > 230:
            is_race_on = False
            winning_color = turtles.color()
            if winning_color == user_bit:
                print(f" You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {turtles.pencolor()} is the winner!")

        rand_distance = random.randint(0, 10)
        turtles.forward(rand_distance)

screen.exitonclick()