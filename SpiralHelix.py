import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("cornsilk3")
turtle_screen.title("Python turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("yellow")
turtle_instance.speed(0)

turtle_colors = ["red", "yellow", "green", "orange", "darkOrchid1", "deepPink4", "brown"]

for i in range(20):
    turtle_instance.color(turtle_colors[i % 7])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(10)

#turtle.done()
turtle.mainloop()