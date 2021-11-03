def AStar(matrix, start, end, bonus_points): # A*

    height, width = len(matrix), len(matrix[0])

    def distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def allBonusPoint(): #tang suc hap dan cho bp
        (x,y,z)=(0,0,0);
        max=9999;
        dis=bonus_points[0]
        for (px,py,p) in bonus_points:
            if distance((px,py),start)<max: 
                max=distance((px,py),start)
                (x,y)=(px,py) #lay khoang cach cua tu gan start nhat #vi sao a? toi khong biet
            z=z+p-distance((px,py),dis)
        return (x,y,z)

    def heuristic(x, y): # this heuristic is not good
        c = distance((x, y), end)
        
        if (x, y) != end: # if agent dont eat bonus point, no bonus point will be added
            #for (px, py, p) in bonus_points: 
            (px,py,p)=allBonusPoint()
            b = distance((x, y), (px, py)) + p +distance((px,py),end)
            if b < 0: 
                c += b

        return c


    previous = [[None]*width for i in range(height)]
    h = [[None]*width for i in range(height)]
    g = [[None]*width for i in range(height)]
    for i in range(height):
        for j in range(width):
            if matrix[i][j] != 'x':
                h[i][j] = heuristic(i, j)
        
    g[start[0]][start[1]] = 0 

    queue = [start]

    def f(x,y, outer = [i], heuristic = True): # estimated cost of the cheapest solution
        b = 0 # bonux point
        if previous[x][y]:
            for (px, py, p) in bonus_points:
                if (x, y) == (px, py) or (px, py) in previous[x][y] or (px, py) in outer:
                    b += p
                    
        if heuristic:
            return h[x][y] + g[x][y] + b
        else:
            return g[x][y] + b

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
                g[x][y] = g[ prev[0] ][ prev[1] ] + 1

                if prev == start:
                    previous[x][y] = [prev]
                else:
                    previous[x][y] = previous[prev[0]][prev[1]] + [prev]

            elif f(x, y, heuristic=False) > f(prev[0], prev[1], [(x, y)], heuristic=False):
                if (x, y) not in queue:
                    queue.append((x, y))
                previous[x][y] = previous[prev[0]][prev[1]] + [prev]
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
        route = previous[x][y] + [end]

        browse = []
        for x in range(height):
            for y in range(width):
                if previous[x][y] != None and (x,y) not in route:
                    browse.append((x,y))

        return route, browse
