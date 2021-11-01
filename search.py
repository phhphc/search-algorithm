def BFS(matrix, start, end):
<<<<<<< HEAD
    height = len(matrix)
    width = len(matrix[0])

    previous = [[' ']*width for i in range(height)]
    previous[start[0]][start[1]] = 0
    print(previous)

    queue = [start]
    print(queue)
=======

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
        return []
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
        return []
    else:
        (x, y) = end
        route = []
        while previous[x][y] != 0:
            route.insert(0, (x,y))
            (x,y) = previous[x][y]
        route.insert(0, start)

        return route
    
             
>>>>>>> bfs

     