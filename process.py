def check(guess,code): 
    '''
    Returns a tuple (white,red) for a given guess and code
    
    White:
    
    A boolean is found for each pair of values in `guess` and `code` (a,b)
    This is broken into 4 parts, all of which must evaluate to True:
    
    - `a` must occur somewhere in `code`
    - `a` must not equal `b` (this would be a red)
    - ***TODO: Explain prevention of counting red as white***
    - the number of occurences of `a` in the slice of guess from a to the end must not be greater than
      the number of occurences of `a` in `code`. This prevents double counting of whites.
       
    We then take the number of `True` values of the resulting list
    
    Red:

    A simple list comprehension - for each pair of values of `guess` and `code`
    we see if they are equal. The number of `True` values is taken.
    '''
    return [a in code and not (a == b) and not all([a == guess[x] for x in [i for i,v in enumerate(code) if v == a]]) and not (code.count(a) < guess[i:].count(a)) for i,(a,b) in enumerate(zip(guess,code))].count(True), [a == b for a,b in zip(guess,code)].count(True)