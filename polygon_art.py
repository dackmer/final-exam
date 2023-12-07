import turtle
import random


class Draw:
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.__num_sides = num_sides
        self.__size = size
        self.__orientation = orientation
        self.__location = location
        self.__color = color
        self.__border_size = border_size

    def get_num_side(self):
        return self.__num_sides

    def set_num_sides(self, num_sides):
        self.__num_sides = num_sides

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def get_orientation(self):
        return self.__orientation

    def set_orientation(self, orientation):
        self.__size = orientation

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_border_size(self):
        return self.__border_size

    def set_border_size(self, border_size):
        self.__border_size = border_size


def draw_polygon(num_sides, size, orientation, location, color, border_size):
    turtle.penup()
    turtle.goto(location[0], location[1])
    turtle.setheading(orientation)
    turtle.color(color)
    turtle.pensize(border_size)
    turtle.pendown()
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(360/num_sides)
    turtle.penup()


def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


ask = input("Which art do you want to generate? Enter a number between 1 to 8, inclusive: ")

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# draw a polygon at a random location, orientation, color, and border line thickness

if ask == 1:
    num_sides = random.randint(2, 3)  # triangle
if ask == 2:
    num_sides = random.randint(2, 4)
if ask == 3:
    num_sides = random.randint(2, 5)
if ask == 4:
    num_sides = random.randint(2, 6)
if ask == 5:
    num_sides = random.randint(2, 7)
if ask == 6:
    num_sides = random.randint(2, 8)
if ask == 7:
    num_sides = random.randint(2, 9)
if ask == 8:
    num_sides = random.randint(2, 10)
size = random.randint(50, 150)
orientation = random.randint(0, 90)
location = [random.randint(-300, 300), random.randint(-200, 200)]
color = get_new_color()
border_size = random.randint(1, 10)
draw_polygon(num_sides, size, orientation, location, color, border_size)


# specify a reduction ratio to draw a smaller polygon inside the one above
reduction_ratio = 0.618

# reposition the turtle and get a new location
turtle.penup()
turtle.forward(size*(1-reduction_ratio)/2)
turtle.left(90)
turtle.forward(size*(1-reduction_ratio)/2)
turtle.right(90)
location[0] = turtle.pos()[0]
location[1] = turtle.pos()[1]

# adjust the size according to the reduction ratio
size *= reduction_ratio

# draw the second polygon embedded inside the original 
draw_polygon(num_sides, size, orientation, location, color, border_size)


# hold the window; close it by clicking the window close 'x' mark
turtle.done()