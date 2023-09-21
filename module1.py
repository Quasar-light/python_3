"""****Your module should have the following capabilities:**
* Has a function to calculate the square footage of a house
* Has a function to calculate the circumference of a circle
* Has a function to change feet to inches"""


def house(lgth, wdth):
    
    sqr_ft = 0

    for i in range(len(lgth)): 
        sqr = lgth[i] * wdth[i]
        sqr_ft = sqr_ft + sqr
    return sqr_ft


def circle(d):
    return d * 3.14


    

def ft_in(feet):
    return feet/12
