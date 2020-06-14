import random
startNum=0
endNum=100
replay = True
highscore=100
guessList = []

while replay:
    guesses = 0
    randomNumber = random.randint(startNum,endNum)
    print(randomNumber)
    while True:   
        userInput = int(input("guess the number"))
        guessList.append(userInput)       
        if startNum<=userInput<=endNum:
            if randomNumber == userInput :
                guesses+=1
                print("success")
                print("it took", guesses, "guesses")
                if highscore >= guesses:
                    highscore = guesses
                print("your highscore is", highscore )
            elif:
                    for i in range(0, len(guessList)):
                if guessList[i] == userInput:
                print("You have already used this number")
                guessList.remove(userInput)
                else:
                break 
                break
            elif randomNumber>userInput:
                print("too low")
                guesses += 1
            elif randomNumber<userInput:
                print("too high")
                guesses += 1    
        else:
            print("invalid guess")

    again = str(input("would you like to play again? Y/N"))
    if again == "Y":
        continue
    else:
        break
            
