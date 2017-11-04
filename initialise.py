import random
def initCode(colors, n):
    with open("rules.txt") as f:
        print("\n".join(f.readlines()))
    random.shuffle(colors)
    return colors[:n]
