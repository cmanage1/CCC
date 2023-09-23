from  collections import deque
N = 7
grid = [[0, 0, 1, 1, 0, 1, 0], [0,0,1, 0,1, 0,0]]


def solve(P, grid):
  res = 0
  ROWS, COLS = len(grid), len(grid[0])
  directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
  visited = set()

  def search(i, j):
    nei = 0
    for dr, dc in directions:
      new_r, new_c = dr+i, dc+j
      if (new_r, new_c) not in visited:
        if new_r in range(ROWS) and new_c in range(COLS):
          if grid[new_r][new_c] == 1:
            visited.add((new_r, new_c))
            nei += 1
    return nei

  for i in range(ROWS):
    for j in range(COLS):
      if grid[i][j] == 1 and (i,j) not in visited:
        nei = search(i, j)
        if nei == 0:
          res += 3
        else:
          res += 3 + nei
        visited.add((i, j))

  return res

F = solve(N, grid)
print(F)