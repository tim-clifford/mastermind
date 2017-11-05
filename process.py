def check(guess,code): 
    '''
    Returns a tuple (white,red) for a given guess and code
    
    ### White:
    A boolean is found for each pair of values in `guess` and `code` (a,b)
    This is broken into 3 parts, all of which must evaluate to True:
    - `a` must occur somewhere in `code`
    - `a` must not equal `b` (this would be a red)
    - ***TODO: explanation***

    We then take the number of `True` values of the resulting list
    
    ### Red:

    A simple list comprehension - for each pair of values of `guess` and `code`
    we see if they are equal. The number of `True` values is taken.
    '''
    return [a in code and not (a == b) and not all([a == guess[x] for x in [i for i,v in enumerate(code) if v == a]]) for a,b in zip(guess,code)].count(True), [a == b for a,b in zip(guess,code)].count(True)
