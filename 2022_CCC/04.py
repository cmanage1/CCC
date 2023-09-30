num = int(input())
sameNum = []
for i in range(num):
    get = input().split()
    sameNum.append(get)

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
    
    print(pairs)