num = int(input())
sameNum = []
for i in range(num):
    get = input().split()
    sameNum.append(get)
    sameNum.append([get[1],get[0]])

num = int(input())
diffNum = []
for i in range(num):
    get = input().split()
    diffNum.append(get)
    
num = int(input())
for i in range(num):
    get = input().split()
    pairs = []
    for j in range(len(get)):
        for k in range(j+1,len(get)):
            pairs.append([get[j],get[k]])
    
    for i in range(len(pairs)):
        if pairs[i] in sameNum:
    print(pairs)