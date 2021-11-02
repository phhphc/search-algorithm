from numpy import abs


def BFS(matrix, start, end):

    height, width = len(matrix), len(matrix[0])

    previous = [[None]*width for i in range(height)]
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
        return None, None
    else:
        (x, y) = end
        route = []
        while previous[x][y] != 0:
            route.insert(0, (x,y))
            (x,y) = previous[x][y]
        route.insert(0, start)

        browse = []
        for x in range(height):
            for y in range(width):
                if previous[x][y] != None and (x,y) not in route:
                    browse.append((x,y))

        return route, browse

def DFS(matrix, start, end):

    height, width = len(matrix), len(matrix[0])

    previous = [[None]*width for i in range(height)]
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
        return None, None
    else:
        (x, y) = end
        route = []
        while previous[x][y] != 0:
            route.insert(0, (x,y))
            (x,y) = previous[x][y]
        route.insert(0, start)

        browse = []
        for x in range(height):
            for y in range(width):
                if previous[x][y] != None and (x,y) not in route:
                    browse.append((x,y))

        return route, browse
    
def GBFS(matrix, start, end): # greedy best first search

    height, width = len(matrix), len(matrix[0])

    def heuristic(x, y):
        return abs(x - end[0]) + abs(y - end[1])

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
        return None, None
    else:
        (x, y) = end
        route = []
        while previous[x][y] != 0:
            route.insert(0, (x,y))
            (x,y) = previous[x][y]
        route.insert(0, start)
    
        browse = []
        for x in range(height):
            for y in range(width):
                if previous[x][y] != None and (x,y) not in route:
                    browse.append((x,y))

        return route, browse
             
def AStar(matrix, start, end): # A*

    height, width = len(matrix), len(matrix[0])

    def heuristic(x, y):
        return abs(x - end[0]) + abs(y - end[1])

    previous = [[None]*width for i in range(height)]
    h = [[None]*width for i in range(height)]
    g = [[None]*width for i in range(height)]
    for i in range(height):
        for j in range(width):
            if matrix[i][j] != 'x':
                h[i][j] = heuristic(i, j)
    previous[start[0]][start[1]] = g[start[0]][start[1]] = 0

    queue = [start]

    def f(x,y): # estimated cost of the cheapest solution
        return h[x][y] + g[x][y]

    def dequeue(queue):
        n = 0
        for i in range(len(queue)):
            if f(queue[i][0], queue[i][1]) < f(queue[n][0], queue[n][1]):
                n = i
        return queue.pop(n)

    def move(x, y, prev):
        if matrix[x][y] != 'x':

            if previous[x][y] == None:
                queue.append((x,y))
                previous[x][y] = prev
                g[x][y] = g[ prev[0] ][ prev[1] ] + 1

            elif f(x, y) < f(prev[0], prev[1]) and (x, y) in queue:
                previous[x][y] = prev
                g[x][y] = g[ prev[0] ][ prev[1] ] + 1

    while len(queue) != 0:
        (x, y) = dequeue(queue)
        if (x,y) == end: 
            break

        move(x + 1,y,(x,y))
        move(x - 1,y,(x,y))
        move(x, y + 1,(x,y))
        move(x, y - 1, (x,y))

    if previous[end[0]][end[1]] == None:
        return None, None
    else:
        (x, y) = end
        route = []
        while (x, y) != start:
            route.insert(0, (x,y))
            (x,y) = previous[x][y]
        route.insert(0, start)
    
        browse = []
        for x in range(height):
            for y in range(width):
                if previous[x][y] != None and (x,y) not in route:
                    browse.append((x,y))

        return route, browse