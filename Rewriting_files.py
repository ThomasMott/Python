data = []
outputdata = []
capdata = []
final = []
yes = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


def file_capitalize():
    file = open ("sonnet.txt","r") #opens .txt file
    for line in file: #appends each line to data variable
        data.append(line)
    file.close #closes file

    for i in range(len(data)):
        x = data[i].capitalize() #capitalizes first letter of each sentence
        outputdata.append(x) #appends it to outputdata

    capdata = [' '.join(i).split() for i in outputdata] #split into characters in 2d array

    for i in range(len(outputdata)):
        for j in range(len(outputdata[i])): #check each character in array
            if outputdata[i][j] in yes: #checks if in yes variable to remove punctuation
                final.append(outputdata[i][j])
    
    file = open ("sonnet_caps.txt","a")
    for word in data:
        file.write(word)
    file.close
    
    print(str1)
    

file_capitalize()

