import turtle
import math

def draw_ellipse(t, center_x, center_y, radius_x, radius_y, color="white"):
    
    t.pencolor(color)
    t.penup()
    
    for angle in range(0, 361, 5):  
        rad = math.radians(angle)
        x = center_x + math.cos(rad) * radius_x
        y = center_y + math.sin(rad) * radius_y
        t.goto(x, y)
        t.pendown()

def draw_3d_sphere():
    window = turtle.Screen()
    window.bgcolor("black")
    
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    colors = ["red", "blue", "green", "orange", "purple", "white", "yellow", "pink", "cyan","magenta"]
             
    for i in range(10):
        angle = (i / 10) * 100  
        rad_angle = math.radians(angle)
        adjusted_radius_y = 100 * math.cos(rad_angle)  
        draw_ellipse(t, 0, 0, 100, adjusted_radius_y, colors[i])
    
    turtle.exitonclick()

draw_3d_sphere()
