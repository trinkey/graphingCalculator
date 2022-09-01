step = 0.1

screenWidth = 600 # Any Integer
screenHeight = 400 # Any Integer

import turtle, numpy, math
x = 0 - (screenWidth / 2)

screen = turtle.Screen()
screen.setup(screenWidth, screenHeight)
screen.bgcolor("#333333")
screen.tracer(0)

turtle1 = turtle.Turtle()
turtle1.color("deep sky blue")
turtle1.pu()
turtle1.speed(0)
turtle1.goto(-100, 0)

turtle2 = turtle.Turtle()
turtle2.color("medium spring green")
turtle2.pu()
turtle2.speed(0)
turtle2.goto(-100, 0)

turtle3 = turtle.Turtle()
turtle3.color("orchid")
turtle3.pu()
turtle3.speed(0)
turtle3.goto(-100, 0)

for i in range(round(screenWidth / step)):
    equation1 = 0.001 * (x ** 3) + x
    equation2 = math.floor(x / 15) * 15
    equation3 = 0.003 * x ** 2 - (screenHeight / 2)
    
    turtle1.goto(x, equation1)
    turtle1.pd()
    
    turtle2.goto(x, equation2)
    turtle2.pd()
    
    turtle3.goto(x, equation3)
    turtle3.pd()
    
    x += step

turtle1.hideturtle()
turtle2.hideturtle()
turtle3.hideturtle()

screen.update()
