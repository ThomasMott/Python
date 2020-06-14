#fizz if div by 3
#buzz if div by 5
#fizzbuzz if both

def fizzbuzz(start, end, divOne, divTwo, wordOne, wordTwo):
    for n in range (start,end):
        if (n % divOne == 0) and (n % divTwo == 0):
            print(wordOne + wordTwo)
        elif (n % 3 == 0):
            print(wordOne)
        elif (n % 5 == 0):
            print(wordTwo)
        else:
            print(n)

        
fizzbuzz(0,101,3,5,"fizz","buzz")
