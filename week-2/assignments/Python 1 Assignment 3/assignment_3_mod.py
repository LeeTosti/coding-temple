#Square footage of a house
def sf_house(width, length):
    """
    This function takes in the inputs of width and length and returns square footage which is width * length
    """
    return int(width * length)


#Circumference of a circle
from math import pi
def circumference(radius):
    """
    This function takes in the input of radius and returns the radius as the integer of 2 times pi times radius
    """
    return int(2*pi*radius)

#Convert feet to inches
def feet_to_inches(feet):
    """
    This function takes the input measurement of feet and returns inches which is feet times 12
    """
    return int(feet * 12)
