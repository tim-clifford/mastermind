import random
def rules(): return "".join(open("rules.txt").readlines())
def getColors(path):
    with open(path) as f:
        try:
            n = int(f.readline().split()[-1])
            maxChoice = int(f.readline().split()[-1])
        except ValueError: 
            print("colors.txt is corrupted")
            raise SystemExit
        return n,maxChoice,[color.split()[0] for color in f.readlines()]
def codeGen(colors,n):
    return [random.choice(colors) for i in range(n)]
