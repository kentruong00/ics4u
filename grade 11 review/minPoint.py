#Create a midpoint function
def midpoint(x1, y1, x2, y2): #dont use same name variables as function arguments
    midX = (x1 + x2)/2
    midY = (y1 + y2)/2
    return midX , midY #returns a tuple: an data type in python, that is an immutable data set, that uses parentheses

print(midpoint(int(input()), int(input()), int(input()), int(input()),))