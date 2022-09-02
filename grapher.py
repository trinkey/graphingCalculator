step = 0.1 # How visually accurate the graph is - I suggest keeping it at 0.1 unless you need to chage it othewise

mode = 2 # Modes: 0 - input/output; 1 - graph only; 2 - both

screenWidth = 600 # Any Integer
screenHeight = 400 # Any Integer

# Imagine the equasion# = as a y =
def equations(x): # Define the equasions here. If you dont want one, just set it to 0 and it will meka a straight line at y = 0 
    global equation1, equation2, equation3, equation1string, equation2string, equation3string
    equation1 = math.floor(x / 15) * 10
    equation2 = 0.003 * x ** 2 - (screenHeight / 2) + 10
    equation3 = 10 * math.sqrt(x)
    # You don't need to do anything below this line
    
    if math.isnan(float(equation1)): turtle1.pu(); equation1 = 0; equation1string = "NaN"
    if math.isnan(float(equation2)): turtle2.pu(); equation2 = 0; equation2string = "NaN"
    if math.isnan(float(equation3)): turtle3.pu(); equation3 = 0; equation3string = "NaN"

import turtle, math
try: import numpy
except: print("The numpy library is not installed. Please consider installing it.")

equation1, equation2, equation3 = 0, 0, 0

x = 0 - (screenWidth / 2)

if mode == 1 or mode == 2:
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
          equation1string, equation2string, equation3string = "", "", ""
          x = input("What x coordinate do you wanna find the y values for? (decimals supported)")
          equations(float(x))
          if equation1string == "": equation1string = str(equation1)
          if equation2string == "": equation2string = str(equation2)
          if equation3string == "": equation3string = str(equation3)
          if mode == 2: print("Y values when x = " + x + ":\nEquation 1 (blue): " + equation1string + "\nEquation 2 (green): " + equation2string + "\nEquation 3 (purple): " + equation3string)
          else: print("")("Y values when x = " + x + ":\nEquation 1 : " + equation1string + "\nEquation 2 : " + equation2string + "\nEquation 3 : " + equation3string)
        except: print("Bad input")
screen.mainloop()
