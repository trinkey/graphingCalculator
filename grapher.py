step = 0.1 # How visually accurate the graph is - I suggest keeping it at 1 unless you need to chage it othewise
mode = 1 # Modes: 0 - input/output; 1 - graph only; 2 - both

screenWidth = 600 # Any Integer
screenHeight = 400 # Any Integer

# Imagine the equasion# = as a y =
def equations(x): # Define the equasions here. If you dont want one, just set it to 0 and it will meka a straight line at y = 0 
    global equation1, equation2, equation3
    equation1 = 0.001 * (x ** 3) + x
    equation2 = 0.003 * x ** 2 - (screenHeight / 2)
    equation3 = math.floor(x / 15) * 15
    
    # You don't need to do anything below this line
    
    if not equation1 <= 1000000 * screenHeight and not 1000000 * equation1 >= screenHeight: turtle1.pu(); equation1 = screenHeight
    if not equation2 <= 1000000 * screenHeight and not 1000000 * equation2 >= screenHeight: turtle2.pu(); equation2 = screenHeight
    if not equation3 <= 1000000 * screenHeight and not 1000000 * equation3 >= screenHeight: turtle3.pu(); equation3 = screenHeight

import turtle, math
try: import numpy
except: pass

equation1, equation2, equation3 = 0, 0, 0

x = 0 - (screenWidth / 2)

screen = turtle.Screen()
screen.update()
screen.setup(screenWidth, screenHeight)
screen.bgcolor("#333333")
screen.tracer(0)

turtle1 = turtle.Turtle()
turtle1.color("deep sky blue")
turtle1.pu()
turtle1.speed(0)

turtle2 = turtle.Turtle()
turtle2.color("medium spring green")
turtle2.pu()
turtle2.speed(0)

turtle3 = turtle.Turtle()
turtle3.color("orchid")
turtle3.pu()
turtle3.speed(0)

if mode == 1 or mode == 2:
    for i in range(round(screenWidth / step)):
        equations(x)
        
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

if mode == 0 or mode == 2:
    while True:
        try:
          x = input("What x coordinate do you wanna find the y values for? (decimals supported)")
          equations(float(x))
          print("Y values when x = " + x + ":\nEquation 1: " + str(equation1) + "\nEquation 2: " + str(equation2) + "\nEquation 3: " + str(equation3))
        except: print("Bad input")
screen.mainloop()
