#Calcuate length of an iterable object
def length(user_object):
    """
    This function takes input of user_object and outputs the length of the user_object
    """
    return len(user_object)

#Create a set from an object
def my_set(object_1):
    """
    This function takes input of object_1 and returns the set of that object
    """
    object_set = set(object_1)
    return object_set


#Create a range function with a start, stop, step

def range_funct(s_top, s_tart=0, s_tep=1):
    for val in range(s_tart, s_top, s_tep):
        print(val)