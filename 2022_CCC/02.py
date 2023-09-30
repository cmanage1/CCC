n = int(input())

gold_players = 0
for i in range(n):
    goal = int(input())
    fowl = int(input())
    
    sum = goal*5-fowl*3
    if sum>40:
        gold_players+=1

print(gold_players,end="")
if gold_players==n:
    print('+')