from numpy import sqrt


def BFS(matrix, start, end):

    previous = [[None]*len(matrix[0]) for i in range(len(matrix))]
    previous[start[0]][start[1]] = 0

    queue = [start]

    def move(x, y, prev): # if move to end return True
        if matrix[x][y] != 'x' and previous[x][y] == None:
            queue.append((x,y))
            previous[x][y] = prev
        return True if end == (x,y) else False

    while len(queue) != 0:
        (x, y) = queue.pop(0)
        if move(x + 1,y,(x,y)) or move(x - 1,y,(x,y)) or move(x, y + 1,(x,y)) or move(x, y - 1, (x,y)):
            break
    

    if previous[end[0]][end[1]] == None:
        return None
    else:
        (x, y) = end
        route = []
        while previous[x][y] != 0:
            route.insert(0, (x,y))
            (x,y) = previous[x][y]
        route.insert(0, start)

        return route

def DFS(matrix, start, end):

    previous = [[None]*len(matrix[0]) for i in range(len(matrix))]
    previous[start[0]][start[1]] = 0

    stack = [start]

    def move(x, y, prev): # if move to end return True
        if matrix[x][y] != 'x' and previous[x][y] == None:
            stack.append((x,y))
            previous[x][y] = prev
        return True if end == (x,y) else False

    while len(stack) != 0:
        (x, y) = stack.pop()
        if move(x + 1,y,(x,y)) or move(x - 1,y,(x,y)) or move(x, y + 1,(x,y)) or move(x, y - 1, (x,y)):
            break
    

    if previous[end[0]][end[1]] == None:
        return None
    else:
        (x, y) = end
        route = []
        while previous[x][y] != 0:
            route.insert(0, (x,y))
            (x,y) = previous[x][y]
        route.insert(0, start)

        return route
    
def GBFS(matrix, start, end): # greedy best first search

    height, width = len(matrix), len(matrix[0])

    def heuristic(x, y):
        return sqrt((x - end[0])**2 + (y - end[1])**2)

    previous = [[None]*width for i in range(height)]
    h = [[None]*width for i in range(height)]
    for i in range(height):
        for j in range(width):
            if matrix[i][j] != 'x':
                h[i][j] = heuristic(i, j)
    previous[start[0]][start[1]] = 0

    queue = [start]

    def dequeue(queue):
        n = 0
        for i in range(len(queue)):
            if h[ queue[i][0] ][ queue[i][1] ] < h[ queue[n][0] ][ queue[n][1] ]:
                n = i
        return queue.pop(n)

    def move(x, y, prev): # if move to end return True
        if matrix[x][y] != 'x' and previous[x][y] == None:
            queue.append((x,y))
            previous[x][y] = prev
        return True if end == (x,y) else False

    while len(queue) != 0:
        (x, y) = dequeue(queue)
        if move(x + 1,y,(x,y)) or move(x - 1,y,(x,y)) or move(x, y + 1,(x,y)) or move(x, y - 1, (x,y)):
            break
    

    if previous[end[0]][end[1]] == None:
        return None
    else:
        (x, y) = end
        route = []
        while previous[x][y] != 0:
            route.insert(0, (x,y))
            (x,y) = previous[x][y]
        route.insert(0, start)

        return route
             

     