import random

def intInputer(inputstring):
    while True:
        try:
            num = int(input(inputstring))
            if num > 0:
                break
            else:
                print("Adj meg egy egész számot, ami nagyobb mint 0!")
        except ValueError:
            print("Hibás bemenet! Adj meg egy egész számot, ami nagyobb mint 0!")
    return num

def createLadder(rungsnumber):
    ladder = []

    ladder.append(1) #földről indulunk
    for _ in range(rungsnumber - 1):
        ladder.append(random.randint(0, 1))
    ladder.append(1) #legfelső fok

    return ladder

def checkLadder(ladder, rungsnumber):
    usable = True
    badrungs = 0

    for i in range(rungsnumber):
        if(ladder[i] == 0):
            badrungs +=1
        else:
            badrungs = 0
        if(badrungs >= 3):
            usable = False

    return usable

def ladderWays(ladder, rungsnumber):
    ways = [0] * (rungsnumber + 1)
    ways[0] = 1 # földről 1 lehetőség

    # első három fok
    if ladder[1]: ways[1] = 1
    if rungsnumber >= 2 and ladder[2]: ways[2] = ways[1] + ways[0]
    if rungsnumber >= 3 and ladder[3]: ways[3] = ways[2] + ways[1] + ways[0]

    # többi fok
    for i in range(4, rungsnumber + 1):
        if ladder[i]:
            ways[i] = ways[i-1] + ways[i-2] + ways[i-3]
    
    return ways[rungsnumber]

rungsnumber = intInputer("A létra fokainak száma: ")

ladder = createLadder(rungsnumber)
print(f"A generált létra (0. index a föld): {ladder}")

usable = checkLadder(ladder, rungsnumber)
print(f"Elérhető-e a teteje: {usable}")

if(usable):
    ways = ladderWays(ladder, rungsnumber)
    print(f"Hányféleképpen lehet feljutni: {ways}")