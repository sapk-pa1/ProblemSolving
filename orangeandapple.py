def location(self_pos, vector2D):
    loc = []
    for i in range(len(vector2D)):
        loc.append(self_pos+ vector2D[i])
    return loc
# Function that returns True if the Apples or the Oranges Landed in the house and False Otheriwse 

def viccinity_house(postions):
    if postions in range(s,t+1):
        return True
    else:
        return False

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_pos = location(a, apples)
    orange_pos = location(b, oranges)
    ## Using the filter function 
    '''
    filter(function, sequence)
    Parameters:
    function: function that tests if each element of a 
    sequence true or not.
    sequence: sequence which needs to be filtered, it can 
    be sets, lists, tuples, or containers of any iterators.
    Returns:
    returns an iterator that is already filtered.

    Source : GeekforGeeks
    '''
    landed_apples = filter(viccinity_house, apple_pos)
    landed_oranges = filter(viccinity_house, orange_pos)
    print(len(list(landed_apples)))
    print(len(list(landed_oranges)))

s = 2
t= 3
a= 1
b =5
m = 1
n = 1
apples = [2]
oranges =[ -2]

countApplesAndOranges(s,t,a,b,apples, oranges)

    
