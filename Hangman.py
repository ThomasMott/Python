#Hangman game

import random
def validate(guess):
    #check guess is 1 char long and guess is in the alphabet
    if guess.isalpha() and len(guess) == 1:
        return True
    else:
        return False
    

words = ["jazz", "Apple", "Character", "Rhythm", "CodeLab", "Piano"]
word = random.choice(words)
#word stored as a variable
guessed = []
#guessed is a list
guessedword = list(len(word)*"_")
#print(guessedword)
wordaslist = list(word)
lives = 9

while True:
    if lives == 0 :
        print("Game Over")
        break
    #If lives is = 0 then print game over and break out of the loop
    elif guessedword == wordaslist:
        print("Great, well done Winner!")
        break
    #check if the guessed word is correct, if it is print well done, if not break out of the loop
    print(" ".join(guessedword))
    #print guessed word all together with __ for each missing letter
    print("Lives left: %d"%(lives))
    #print the number of lives left over
    guess = input("Guess: ")
    while validate(guess) == False:
        guess = input("Guess: ")

    if guess not in guessed:
        #if the guess input is not in the guessed list
        guessed.append(guess)
        #add letter to the guess list
        if guess not in wordaslist:
                lives = lives -1
               #if it is a new guess and it is not in the list
        else:
            for i in range(0,len(wordaslist)):
                if guess == wordaslist[i]:
                    #[i] counts along the position to check if the guess matches any of the letter
                    guessedword[i] = guess
            
    else:
        print("you have already guessed that")
        #if that letter has been guessed inform them and don't take a life off them
        
