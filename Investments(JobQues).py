#show what stocks and bonds need to be bought and sold to make even

string = "microsoft,stock,11;Google,stock,5;Google,bond,1|microsoft,stock,10;Google,bond,10"

#split string by remving "|"

x = string.split("|")

#split again
portfolio = x[0].split(";")
benchmark = x[1].split(";")

#split again
p_list = []
b_list = []

for p in portfolio:
    p_list.append(p.split(","))
for b in benchmark:
    b_list.append(b.split(","))

#string coparison

sell = 0
buy = 0


for i in range(len(p_list)):
    transactionMade = False
    for j in range(len(b_list)):
        if p_list[i][0] == b_list[j][0]:
            if p_list[i][1] == b_list[j][1]:
                if p_list[i][2] > b_list[j][2]:
                    sell = int(p_list[i][2]) - int(b_list[j][2])
                    print("sell " + str(sell) + " " + p_list[i][0] + " " + p_list[i][1])
                    transactionMade = True
                elif p_list[i][2] < b_list[j][2]:
                    buy = int(b_list[j][2]) - int(p_list[i][2])
                    print("buy " + str(buy))
                    transactionMade = True
                elif p_list[i][2] == b_list[j][2]:
                    print("is fine")
                    transactionMade = True
    if transactionMade == False:
        print("sell " + p_list[i][0])
