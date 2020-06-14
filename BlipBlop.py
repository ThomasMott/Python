#find how many blob in each string and then output with total on end

txt = ["blip,blob,blob,blob", "blip,blip,blip", "blob,blip,blob,blip,blob"]
ans = []

def find(findWord):
    for i in range(0,len(txt)):
        
        x=(txt[i].split(","))
        print(x)
        ans.append((x.count(findWord)))

    ans.append(sum(ans))
    str(ans)
    print("|".join(map(str,ans)))

find("blob")
