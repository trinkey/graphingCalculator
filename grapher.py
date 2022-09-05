import turtle, math
try: import numpy
except: print("The numpy library is not installed. Please consider installing it.")

step = 0.1 # How visually accurate the graph is - I suggest keeping it at 0.1 unless you need to chage it othewise

screenWidth = 1000 # Any Integer
screenHeight = 750 # Any Integer

equations = [
    lambda x: math.floor(x / 15) * 10,
    lambda x: 0.003 * x ** 2 - (screenHeight / 2) + 10,
    lambda x: 100 * math.sin(x / 10),
    lambda x: 10 * math.sqrt(abs(-x)) if x > 0 else float("nan")
]

screen = turtle.Screen()
screen.update()
screen.setup(screenWidth, screenHeight)
screen.bgcolor("#333333")
screen.tracer(0)


graphers = []
turtleColors = ["#FF6347", "#FF8C00", "#FFD700", "#7CFC00", "#00FA9A", "#00CED1", "#6495ED", "#9370DB", "#DA70D6"]

class Graph:
    def __init__(self, color, equation):
        self.equation = equation
        self.color = color
        self.ycor = 0.0
        self.turtle = turtle.Turtle()
        self.turtle.color(self.color)
        self.turtle.pu()
        self.turtle.speed(0)
    
    def graphEquation(self, x):
        self.ycor = self.equation(x)
        if math.isnan(float(self.ycor)): self.turtle.pu()
        else: self.turtle.goto(x, self.ycor)
        self.turtle.pd()
    
    def inout(self, x): 
        try:
            self.vairbale = self.equation(float(x))
            if math.isnan(float(self.vairbale)): return "NaN"
            else: return self.vairbale
        except: return "Bad Input D:"

for i in range(len(equations)): graphers.append(Graph(turtleColors[i % 9], equations[i]))

x = 0 - (screenWidth / 2)

for i in range(round(float(round(screenWidth / step)) + float(step))):
    
    for o in graphers: o.graphEquation(x)
    
    x += step

for o in graphers:
    o.turtle.hideturtle()

screen.update()

while True:
    x = input("What do you wanna find the y values for (decimals supported)?\n")
    print("Outputs when x = " + x)
    for o in range(len(graphers)): print("Equation " + str(o + 1) + ": " + str(graphers[o].inout(x)))
    print()
