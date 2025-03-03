import turtle

window = turtle.Screen()
window.bgcolor("black")

t1 = turtle.Turtle()
t1.speed(0)
colors=["red","blue","green","orange","purple","white","yellow","pink","grey","cyan"]


#refrence points for big square 
big_square = [
    (-100, -100),  # bottom left
    (100, -100),   # bottom right
    (100, 100),    # top right
    (-100, 100)    # top left
]
#refrence points for little square
little_square = [
    (-60, -60),  
    (60, -60),
    (60, 60),
    (-60, 60)
]

for i in range(10):
    shift=i*-10
    t1.pencolor(colors[i])
    t1.penup()
    t1.goto(big_square[0][0]+shift,big_square[0][1]+shift) 
    t1.pendown()
    t1.goto(big_square[1][0]+shift,big_square[1][1]+shift)
    t1.goto(big_square[2][0]+shift,big_square[2][1]+shift)
    t1.goto(big_square[3][0]+shift,big_square[3][1]+shift)
    t1.goto(big_square[0][0]+shift,big_square[0][1]+shift)
    t1.penup()
    t1.goto(little_square[0][0]+shift,little_square[0][1]+shift)
    t1.pendown()
    t1.goto(little_square[1][0]+shift,little_square[0][1]+shift)
    t1.goto(little_square[2][0]+shift,little_square[2][1]+shift)
    t1.goto(little_square[3][0]+shift,little_square[3][1]+shift)
    t1.goto(little_square[0][0]+shift,little_square[0][1]+shift)
    t1.penup()
    t1.goto(big_square[0][0]+shift,big_square[0][1]+shift)
    t1.pendown()
    t1.goto(little_square[0][0]+shift,little_square[0][1]+shift)
    t1.penup()
    t1.goto(big_square[1][0]+shift,big_square[1][1]+shift)
    t1.pendown()
    t1.goto(little_square[1][0]+shift,little_square[1][1]+shift)
    t1.penup()
    t1.goto(big_square[2][0]+shift,big_square[2][1]+shift)
    t1.pendown()
    t1.goto(little_square[2][0]+shift,little_square[2][1]+shift)
    t1.penup()
    t1.goto(big_square[3][0]+shift,big_square[3][1]+shift)
    t1.pendown()
    t1.goto(little_square[3][0]+shift,little_square[3][1]+shift)


turtle.exitonclick()