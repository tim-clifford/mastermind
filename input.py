def read(path): return [a.replace("\n","") for a in open(path).readlines()]
def guessFrom(colors):
    while True:
        guess = input("Enter guess (seperated by spaces): ").split()
        guess = [i.lower() for i in guess]
        for i in guess:
            if not i in colors: 
                print("Invalid guess")
                break
        else: break
    return guess
