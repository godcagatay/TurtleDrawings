import turtle
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light pink")
turtle_screen.title("Turtle Python")

turtle_instence = turtle.Turtle()
turtle_instence.color("blue")

def shrinkingSquare(size):
    for s in range(4):
        turtle_instence.forward(size)
        turtle_instence.left(90)
        size = size - 5

shrinkingSquare(300)
shrinkingSquare(280)
shrinkingSquare(260)
shrinkingSquare(240)
shrinkingSquare(220)
shrinkingSquare(200)
shrinkingSquare(180)
shrinkingSquare(160)
shrinkingSquare(140)
shrinkingSquare(120)
shrinkingSquare(100)
shrinkingSquare(80)
shrinkingSquare(60)
shrinkingSquare(40)
shrinkingSquare(20)


turtle.done()