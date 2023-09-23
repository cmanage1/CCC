'''
+50 per package deliver\ed
-10 for collision 
+500 if num_packages_del > num_obstancles
'''

P = int(input("")) # num packages del
C = int(input("")) # num of collisions

def solve(P, C):
  res = P*50 - C*10
  if P>C:
    res += 500

  return res

F = solve(P,C)
print(F)