step = 0.1 # How visually accurate the graph is - I suggest keeping it at 0.1 unless you need to chage it othewise

mode = 2 # Modes: 0 - input/output; 1 - graph only; 2 - both

screenWidth = 600 # Any Integer
screenHeight = 400 # Any Integer

# Define equations here.
# Make sure every one starts with 'lambda x: ' (That allows it to call it as a funtion which allows a variable to change after its defined)
# If theres another equation after it it should have a comma after it
# treat that as a 'y = ' when writing equations
equations = [
    lambda x: math.floor(x / 15) * 10,
    lambda x: 0.003 * x ** 2 - (screenHeight / 2) + 10,
    lambda x: 100 * math.sin(x / 10),
    lambda x: 10 * math.sqrt(abs(-x)) if x >= 0 else float("nan")
]

# You do not need to do anything below this line.

# Import libraries
import turtle, math, random
try: import numpy # Print statement if numpy isn't installed
except: print("The numpy library is not installed. Please consider installing it.")

graphers = [] # List for the class object
turtleColors = ["#FF6347", "#FF8C00", "#FFD700", "#7CFC00", "#00FA9A", "#00CED1", "#6495ED", "#9370DB", "#DA70D6"] # Colors for the turtle

# Define the class
class Graph:
    def __init__(self, color, equation, mode):
        self.equation = equation # Set the equation function
        self.ycor = 0.0 # Define the variable for later
        self.nan = False # Define the variable for later
        if mode == 1 or mode == 2: # Define turtle if mode is 1 or 2
            self.turtle = turtle.Turtle() # Turtle object
            self.turtle.color(color) # Set turtle color
            self.turtle.pu() # Pen up
            self.turtle.speed(0) # Maximum speed infinity
    
    def graphEquation(self, x): # What to do when graphing mode
        self.ycor = self.equation(x) # Calculate y value
        if math.isnan(float(self.ycor)): self.nan = True # If output is nan then self.nan = True
        else: self.turtle.goto(x, self.ycor); self.nan = False # If it isnt nan then goto correct coords
        if self.nan == False: # If it isn't nan
            self.turtle.pd() # Pen down
            self.turtle.fd(0) # Make it draw a dot
            self.turtle.pu() # Pen up
    
    def inout(self, x):  # What to do when input/output mode
        try:
            self.vairbale = self.equation(float(x)) # Calculate equation
            if math.isnan(float(self.vairbale)): return "NaN" # If equation output is nan return NaN
            else: return self.vairbale # It not nan return answer
        except: return "Bad Input D:" # If error return bad input

if mode == 1 or mode == 2: # If mode 1 or 2 setup turtle window
    screen = turtle.Screen() # Turtle Screen object
    screen.setup(screenWidth, screenHeight) # Screen size
    screen.bgcolor("#333333") # Screen color
    screen.tracer(0) # All actions happen as fast as possible

# Create Graph class object with color and equation
for i in range(len(equations)): graphers.append(Graph(turtleColors[i % 9], equations[i], mode))

# Create the graph if mode is 1 or 2
if mode == 1 or mode == 2:
    x = 0 - (screenWidth / 2) # Set minimum x value

    for i in range(round(screenWidth / step + step)): # For every step in the screen
        for o in graphers: o.graphEquation(x) # Graph each equation for x value
        x += step # Increase x by step
    for o in graphers: o.turtle.hideturtle() # Hide turtles

    screen.update() # Update the screen

# Do the input/output if mode is 0 or 2
if mode == 0 or mode == 2:
    while True: # Loop forever
        x = input("What x value do you want to find the y values for (decimals supported)?\n") # Input x value
        print("Outputs when x = " + x) # First print statement
        for o in range(len(graphers)): print("Equation " + str(o + 1) + ": " + str(graphers[o].inout(x))) # Print output for each equation
        print("") # New line

# If mode is 1 make sure graph window doesn't instantly close
if mode == 1: screen.mainloop() # Keep screen open after script stops (only does something on independent python where turtle opens a window)
