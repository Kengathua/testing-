def add(x,y):
    #Adds two numbers
    return x+y

def subtract(x,y):
    #Gets the diffence between two numbers
    return x-y

def multiply(x,y):
    #Gets the multiple of a number by another number
    return x*y

def divide(x,y):
    #Gets the divion of two numbers
    if y==0:
        raise ValueError('Can not divide by zero!')
    return x/y