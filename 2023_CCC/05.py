# Word hunt

# DFS all directions for word

f = open('j5/j5.01.01.in')

lines = f.readlines()
word = ""
iGrid = []

for i, line in enumerate(lines):
    if i == 0:
        word = line
    elif i == 1:
        R = int(line)
    elif i == 2:
        C = int(line)
    else:
        iGrid.append(line)

grid = []
for g in iGrid:
    letters = g.strip("\n").split(" ")
    letters[-1] = letters[-1][:2]
    grid.append(letters)


def solve(grid, word):
    ROWS, COLS = R, C
    res = 0
    visited = set()

    def dfs(i, j, l):
        if i not in range(ROWS) or j not in range(COLS) or (i, j) in visited:
            return False
        
        letter = word[l]

        if grid[i][j] == letter:
            print(letter)
            # 6 directions
            ans = (
                dfs(i+1, j, l+1)
            or dfs(i, j+1, l+1)
            or dfs(i+1, j+1, l+1)
            or dfs(i-1, j, l+1)
            or dfs(i, j-1, l+1)
            or dfs(i-1, j-1, l+1)
            )
            
        
        return ans
    
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == word[0]:
                visited = set()
                if dfs(0, 0, 0):
                    res += 1
    return res

ans = solve(grid, word)
print(ans)