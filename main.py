# import turtle as t
#
# tim = t.Turtle()
#
# screen = t.Screen()
#
# screen.listen()
#
# def move_forwards():
#     tim.forward(10)
#
#
# screen.onkey(key = "space", fun = move_forwards)
#
# screen.exitonclick()

import turtle as t

tim = t.Turtle()

screen = t.Screen()

screen.listen()

# Functions of movement

def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def move_left():
    tim.left(10)
def move_right():
    tim.right(10)
def clear_screen():
    tim.reset()


# LLamando la función forwards mientras la pantalla esté activa:

screen.onkeypress(key="w",fun = move_forwards)
screen.onkeypress(key="s",fun = move_backwards)
screen.onkeypress(key="a",fun = move_left)
screen.onkeypress(key="d",fun = move_right)
screen.onkey(key="c",fun = clear_screen)


screen.exitonclick()