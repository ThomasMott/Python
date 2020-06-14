import random

num = 0
playNum = []
play = []
lineUp = []

num = int(input("how many players?"))

for i in range(1,num + 1):
    playNum.append(i)
for j in range(1,num + 1):
    play.append(str('player ' + str(j)))   

random.shuffle(playNum)

for k in range(0,num):
    print(str(play[k]) + " is " + str(playNum[k]))
