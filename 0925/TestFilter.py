def filter ( predicate, names ):
    result=[]
    for elem in names:
        if predicate(elem):
            result.append(elem)
    return result

def gt6(elem):
    return len(elem) > 6

def lt5(elem):
    return len(elem) < 5

def eq6(elem):
    return len(elem) == 6   #是等等於喔~

names=['Justin','Nick','Jackson']

print('大於6:',filter(gt6,names))
print('小於5:',filter(lt5,names))
print('等於6:',filter(eq6,names))