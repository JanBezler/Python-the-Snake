import turtle
import time
import random

tim = turtle.Turtle()
x=0
moves = []
while True:

    time.sleep(0.1)
    ran=random.randrange(-50,50)
    moves.append(ran)
    tim.left(ran)
    tim.forward(10)
    tim.pensize(10)

    x+=1
    if x == 10:
        bob = turtle.Turtle()
        z = 1

    if x > 10:

        bob.left(moves[len(moves)-11])
        bob.forward(10)
        bob.color("black")
        bob.pencolor("white")
        bob.pensize(12)
