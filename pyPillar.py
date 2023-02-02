from ursina import *
import random

def add(list, arrIndex, index):
    global points
    temp = list[index]
    num = numsArr[arrIndex-1]
    list[index] = num
    numsArr.remove(num)
    if (temp != 0):
        numsArr.append(temp)
    bankAdd(temp)
    if (index != 9):
        if (list[index+1] == num+1):
            points += (num + list[index+1])
    if (index != 0):
        if (list[index-1] == num-1):
            points += (num + list[index-1])

def bankAdd(num):
    bank[0] = num
    bank[1] = numsArr[random.randint(1, len(numsArr))-1]

def choose(list, chosen, number, ind):
    if (chosen == 0):
        add(list, number, ind)
    elif (chosen == 1):
        add(list, number, ind)
    else:
        bankAdd(numsArr[random.randint(1, len(numsArr))-1])

def isSorted(list):
    if (sorted(list) == list):
        gameEnd()

def gameEnd():
    print("Game End")
    #exit()

def createTowers():
    for i in range(5):
        add(list1, random.randint(1, len(numsArr)), i)
        add(list2, random.randint(1, len(numsArr)), i)
        pillar1.append(Entity(model = 'cube', texture = 'wood.jpg', scale = (0.8), position = Vec2(5, i-3)))
        pillar2.append(Entity(model = 'cube', texture = 'wood.jpg', scale = (0.8), position = Vec2(-5, i-3)))

def main():
    isSorted(list1)
    isSorted(list2)
    print("Bank: ", bank)
    #wait for user choice
    #choose(input)
    print("list 1: ", list1)
    print("list 1: ", list2)
    print("Points: ", points)

app = Ursina()

max = 50
numsArr = [i+1 for i in range(max)]
list1 = [0 for i in range(10)]
list2 = [0 for i in range(10)]
bank = [0, 0]
points = 0
pillar1 = []
pillar2 = []

createTowers()
main()
app.run()