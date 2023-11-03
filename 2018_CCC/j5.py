from collections import deque, defaultdict

'''
@param graph : bidirectional graph, adj list representation
@param N : total verteces(nodes) in graph
@return None
'''
def solve(graph, N):
    # we're using array and not set since we need to keep order (sets are unordered)
    visited = [False] * N

    def bfs(node, min_steps):
        visited[0] = True
        q = deque([])
        q.append((1, 1))
        
        # normal bfs while keeping track of curr page and steps
        # steps can be thought of as the number of edges it takes to reach a certain vertex(node)
        while q:
            curr_page, steps = q.popleft()

            # we encounter an end page since only end pages have no more pages to go to
            if len(graph[curr_page]) == 0:
                # no need for anything fancy, we just need to keep track of min steps it takes to reach here
                min_steps = min(steps, min_steps)
           
            # otherwise we iterate neighbours while tracking steps it takes
            else:
                for path in graph[curr_page]:
                    if not visited[path - 1]: # always check visited to prevent infinite loops
                        q.append((path, steps + 1)) # bfs the neighbour while adding 1 step (1 more edge to reach here)
                        visited[path - 1] = True # mark the current node before we do more bfs (within this for loop it is path-1) as visited
        
        return min_steps

    min_steps = bfs(0, float("inf"))

    # Check if we visited all the verteces
    all_visited = True
    for visit in visited:
        if not visit:
            all_visited = False
    
    print("Y" if all_visited else "N")
    print(min_steps)

N = int(input())
graph = defaultdict(list) # we can do this without defaultdict, this was for less code

# handle edge case
if N == 0:
    exit()

for i in range(N):
    line = input().split()
    line_len = int(line[0])

    for j in range(1, line_len + 1):
        # our pages are 1 indexed in the problem so we'll make the graph that way
        graph[i+1].append(int(line[j]))

# print(graph) # to see what our graph looks like
solve(graph, N)
