from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.title("My Snake game")
screen.setup(width=600, height=600)

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []  # List to store each segment of the snake

for position in starting_position:
    new_turtle = Turtle("square")
    new_turtle.penup()  # Prevents drawing lines when moving
    new_turtle.goto(position)
    new_turtle.color("white")
    segments.append(new_turtle)  # Add the segment to the list

screen.exitonclick()
