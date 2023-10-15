import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light green")
drawing_board.title("Python turtle")
turtle_instance = turtle.Turtle()

'''
#----------------------------------#
#Square

num_sides = 4
angle = 360 / num_sides
side_length = 200

for s in range(4):
    turtle_instance.forward(200)
    turtle_instance.left(90)

turtle.done()

#----------------------------------#
#Triangle

num_sides = 3
angle = 360 / num_sides
side_length = 200

for t in range(num_sides):
    turtle_instance.left(angle)
    turtle_instance.forward(side_length)

turtle.done()
#----------------------------------#

#Any Polygon

num_sides = 8
angle = 360 / num_sides
side_length = 150

for p in range(num_sides):
    turtle_instance.forward(side_length)
    turtle_instance.left(angle)

turtle.done()
#----------------------------------#
'''

#Star

num_sides = 5
angle = 360 / 5 * 2     #Special formula for star angles
side_length = 200

for s in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_length)

turtle.done()