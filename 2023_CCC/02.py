'''
return total spiceness after adding
'''

N = int(input(""))
peppers = []
for i in range(N):
  peppers.append(input(""))

def solve(n, peppers):
  res = 0
  d = {
    "Pablano": 1500,
    "Mirasol": 6000
  }

  for p in peppers:
    res += d[p]

  return res

F = solve(N, peppers)
print(F)