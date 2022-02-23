import colorgram
import turtle as t
import random

rgb_colors = []
colors = colorgram.extract("image.jpg", 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colour = (r, g, b)
    rgb_colors.append(new_colour)

timothy = t.Turtle()
timothy.shape("turtle")
# Ensuring the turtle module uses the RGB colour mode.
t.colormode(255)

colour_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41),
               (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
               (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
               (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
               (176, 192, 208), (168, 99, 102)]


def random_color():
    """Returns a random color"""
    random_rgb_colour = random.choice(colour_list)
    return random_rgb_colour


def draw_ten_dots():
    """Instructs timothy to draw ten dots in sequence"""
    for i in range(10):
        timothy.pencolor(random_color())
        timothy.dot(15)
        timothy.penup()
        timothy.forward(50)


def create_damien_hirst_painting():
    """Create a procedural and random Damien Hirst Painting using the turtle module."""
    starting_x = -225.00
    starting_y = -225.00
    timothy.penup()
    timothy.speed("fastest")
    timothy.hideturtle()
    timothy.setposition(starting_x, starting_y)
    for _ in range(10):
        draw_ten_dots()
        timothy.penup()
        starting_y += 50.00
        timothy.setposition(starting_x, starting_y)
    timothy.home()


create_damien_hirst_painting()

screen = t.Screen()
screen.exitonclick()
