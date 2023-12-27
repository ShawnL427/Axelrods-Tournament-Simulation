import random

#STRAT
def pacifist(index, own, opponent):
    return(True)

def hater(index, own, opponent):
    return(False)

def titForTat(index, own, opponent):
    if(index ==0):
        return(True)
    else:
        return(opponent[index-1])
    
def randomS(index, own, opponent):
    random_number = random.randint(0, 1)
    if(random_number == 0):
        return(True)
    if(random_number == 1):
        return(False)

def friedman(index, own, opponent):
    if(index == 0):
        return(True)
    if(False in opponent):
        return(False)
    return(True)

def titForTwoTats(index, own, opponent):
    if(index <2):
        return(True)
    if(opponent[index-1] == False and opponent[index-2] == False):
        return(False)
    return(True)

def twoTitsForTat(index, own, opponent):
    if(index ==0):
        return(True)
    if(opponent[index-1] == False):
        return(False)
    if(index > 1 and opponent[index-2] == False):
        return(False)
    return(True)

def alternate(index, own, opponent):
    if(index == 0):
        return(True)
    if(own[index-1] == True):
        return(False)
    return(True)

def third(index, own, opponent):
    if((index + 1) % 3 == 0):
        return(False)
    return(True)


#GAME
def playGame(strat1, strat2):
    
    s1List = []
    s2List = []
    s1Points = 0
    s2Points = 0

    for i in range(100):
        hold = s1List
        s1List.append(strat1(i, s1List, s2List))
        s2List.append(strat2(i, s2List, hold))
        if(s1List[i] == True and s2List[i] == True):
            s1Points +=3
            s2Points +=3
        if(s1List[i] == False and s2List[i] == True):
            s1Points +=5
            s2Points +=0
        if(s1List[i] == True and s2List[i] == False):
            s1Points +=0
            s2Points +=5
        if(s1List[i] == False and s2List[i] == False):
            s1Points +=1
            s2Points +=1
    
    
    """print(f"{strat1.__name__}: {s1List}")
    print(f"{strat2.__name__}: {s2List}")
    print(f"{strat1.__name__}: {s1Points}")
    print(f"{strat2.__name__}: {s2Points}")
    """
    return(s1Points, s2Points)
    

#Tournament
def playTournament(stratList):

    pointDict = {}

    for i in range(len(stratList)-1):
        for j in range(i+1, len(stratList)):
            val = playGame(stratList[i], stratList[j])
            if(stratList[i].__name__ in pointDict):
                pointDict[stratList[i].__name__] += val[0]
            else:
                pointDict[stratList[i].__name__] = val[0]
            if(stratList[j].__name__ in pointDict):
                pointDict[stratList[j].__name__] += val[1]
            else:
                pointDict[stratList[j].__name__] = val[1]
    
    print(pointDict.items())
    for x in pointDict.items():
        print(f"{x[0]}: {x[1]}")
            
playTournament([pacifist, hater, titForTat, randomS, friedman, titForTwoTats, twoTitsForTat, alternate, third])

#playGame(titForTat, hater)

