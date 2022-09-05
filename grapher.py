step = 0.1 # How visually accurate the graph is - I suggest keeping it at 0.1 unless you need to chage it othewise

mode = 2 # Modes: 0 - input/output; 1 - graph only; 2 - both

screenWidth = 1000 # Any Integer
screenHeight = 750 # Any Integer

equations = [ # Define equations here. Make sure every one starts with 'lambda x: ' and if theres another equation after it it should have a comma after it - treat that as a 'y = ' when writing equations
    lambda x: math.floor(x / 15) * 10,
    lambda x: 0.003 * x ** 2 - (screenHeight / 2) + 10,
    lambda x: 100 * math.sin(x / 10),
    lambda x: 10 * math.sqrt(abs(-x)) if x > 0 else float("nan")
]

# You do not need to do anything below this line.

# Import libraries
import turtle, math, random
try: import numpy
except: print("The numpy library is not installed. Please consider installing it.")

graphers = [] # List for the class object
turtleColors = ["#FF6347", "#FF8C00", "#FFD700", "#7CFC00", "#00FA9A", "#00CED1", "#6495ED", "#9370DB", "#DA70D6"] # Colors for the turtle

class Graph: # Define the class
    def __init__(self, color, equation, mode):
        self.equation = equation # set the equation function
        self.ycor = 0.0 # define the variable for later
        if mode == 1 or mode == 2: # Define turtle if mode is 1 or 2
            self.turtle = turtle.Turtle() # turtle object
            self.turtle.color(color) # set turtle color
            self.turtle.pu() # penup
            self.turtle.speed(0) # maximum speed
    
    def graphEquation(self, x): # What to do when graphing
        self.ycor = self.equation(x) # Calculate y value
        if math.isnan(float(self.ycor)): self.turtle.pu() # If output is nan then penup
        else: self.turtle.goto(x, self.ycor) # If it isnt nan then goto correct coords
        self.turtle.pd() # pendown
    
    def inout(self, x):  # What to do when input/output
        try:
            self.vairbale = self.equation(float(x)) # calculate equation
            if math.isnan(float(self.vairbale)): return "NaN" # if nan return NaN
            else: return self.vairbale # it not nan return answer
        except: return "Bad Input D:" # if error return bad input

if mode == 1 or mode == 2: # if mode 1 or 2 setup turtle window
    screen = turtle.Screen()
    screen.setup(screenWidth, screenHeight)
    screen.bgcolor("#333333")
    screen.tracer(0)

for i in range(len(equations)): graphers.append(Graph(turtleColors[i % 9], equations[i], mode)) # create Graph class object with color and equation

if mode == 1 or mode == 2:
    x = 0 - (screenWidth / 2) # Set minimum x value

    for i in range(round(round(screenWidth / step) + step))): # for every step in the screen
        for o in graphers: o.graphEquation(x) # graph each equation for x value
        x += step # increase x by step
    for o in graphers: o.turtle.hideturtle() # hide turtles

    screen.update() # update the screen

if mode == 0 or mode == 2:
    while True: # loop forever
        x = input("What do you wanna find the y values for (decimals supported)?\n") # input x value
        print("Outputs when x = " + x) # first print statement
        for o in range(len(graphers)): print("Equation " + str(o + 1) + ": " + str(graphers[o].inout(x))) # print output for each equation
        print() # newline

if mode == 1: # if mode is 1 make sure graph window doesnâ€™t instantly close
    screen.mainloop()
