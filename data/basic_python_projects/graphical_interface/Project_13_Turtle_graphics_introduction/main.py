import math
import turtle as turtle_module
import random

def prepare_turtle():
    turtle_module.colormode(255)
    turtle = turtle_module.Turtle()
    turtle.speed("fastest")
    turtle.setposition(0, -100)
    turtle.hideturtle()
    return turtle

def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def draw_image(turtle, first_radius, second_radius, first_parts, second_parts):
    starting_point = (turtle.pos()[0], turtle.pos()[1])
    first_scale, first_step = get_params_from_radius(first_radius, first_parts)
    second_scale, second_step = get_params_from_radius(second_radius, second_parts)
    first_angle = 0
    second_angle = 0
    continue_drawing = True
    while continue_drawing:
        turtle.pendown()
        turtle.circle(20)
        turtle.penup()
        
        first_angle = (first_angle + first_scale) % 360
        second_angle = (second_angle + second_scale) % 360
        #inner_circle
        turtle.setheading(first_angle)
        turtle.forward(first_step)
        #outer_circle
        turtle.setheading(second_angle)
        turtle.forward(second_step)

        if turtle.distance(starting_point) < 1:
            continue_drawing = False

def start_animation():
    turtle = prepare_turtle()
    for number in range(1, 10):
        turtle.clear()
        turtle.color(get_random_color())
        #radius adjust the size of the circles, while the parts adjust the number of circles i.e., the rotation speed
        draw_image(turtle,50,200, 100, 1000)

def get_params_from_radius(radius, parts):
    #calcualte the angle and step size for each circle based on the radius and parts
    angle = 360 / parts
    step = 2 * radius * math.sin(math.radians(angle / 2))
    return angle, step

start_animation()
screen = turtle_module.Screen()
screen.exitonclick()