step = 0.1 # How visually accurate the graph is - I suggest keeping it at 0.1 unless you need to chage it othewise

mode = 1 # Modes: 0 - input/output; 1 - graph only; 2 - both

screenWidth = 1000 # Any Integer
screenHeight = 750 # Any Integer


# Imagine the equasion# = as a y =
def equations(x): # Define the equasions here. If you dont want one, just set it to 0 and it will meka a straight line at y = 0 
    global equation1, equation2, equation3, equation4, equation1string, equation2string, equation3string, equation4string, screenWidth, screenHeight, mode
    try: equation1 = math.floor(x / 15) * 10
    except: equation1 = float("nan") # ignore this line
    try: equation2 = 0.003 * x ** 2 - (screenHeight / 2) + 10
    except: equation2 = float("nan") # and this one
    try: equation3 = 100 * math.sin(x / 10)
    except: equation3 = float("nan") # and this
    try: equation4 = 10 * math.sqrt(-x)
    except: equation4 = float("nan") # and finally, this
    
    # You don't need to do anything below this line
    
    try:
        if math.isnan(float(equation1)): turtle1.pu()
        if math.isnan(float(equation2)): turtle2.pu()
        if math.isnan(float(equation3)): turtle3.pu()
        if math.isnan(float(equation4)): turtle4.pu()
    except: pass

    if math.isnan(float(equation1)): equation1 = 0; equation1string = "NaN"
    if math.isnan(float(equation2)): equation2 = 0; equation2string = "NaN"
    if math.isnan(float(equation3)): equation3 = 0; equation3string = "NaN"
    if math.isnan(float(equation4)): equation4 = 0; equation4string = "NaN"

import turtle, math
try: import numpy
except: print("The numpy library is not installed. Please consider installing it.")

equation1, equation2, equation3, equation4 = 0, 0, 0, 0

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
    
    turtle4 = turtle.Turtle()
    turtle4.color("gold")
    turtle4.pu()
    turtle4.speed(0)
    
    for i in range(round(screenWidth / step)):
        equations(x)
        
        turtle1.goto(x, equation1)
        turtle1.pd()
        
        turtle2.goto(x, equation2)
        turtle2.pd()
        

        turtle3.goto(x, equation3)
        turtle3.pd()
        
        turtle4.goto(x, equation4)
        turtle4.pd()
        
        x += step

        turtle1.hideturtle()
        turtle2.hideturtle()
        turtle3.hideturtle()
        turtle4.hideturtle()

try: screen.update()
except: pass

if mode == 0 or mode == 2:
    while True:
        try:
            equation1string, equation2string, equation3string, equation4string = "", "", "", ""
            x = input("What x coordinate do you wanna find the y values for? (decimals supported)\n")
            equations(float(x))

            if equation1string == "": equation1string = str(equation1)
            if equation2string == "": equation2string = str(equation2)
            if equation3string == "": equation3string = str(equation3)
            if equation4string == "": equation4string = str(equation4)
            
            if mode == 2: print("Y values when x = " + x + ":\nEquation 1 (blue): " + equation1string + "\nEquation 2 (green): " + equation2string + "\nEquation 3 (purple): " + equation3string+ "\nEquation 4 (purple): " + equation4string)
            else: print("Y values when x = " + x + ":\nEquation 1 : " + equation1string + "\nEquation 2 : " + equation2string + "\nEquation 3 : " + equation3string+ "\nEquation 4 : " + equation4string)
        
        except: print("Bad input")

try: screen.mainloop()
except: pass
