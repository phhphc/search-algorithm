def BFS(matrix, start, end):
    height = len(matrix)
    width = len(matrix[0])

    previous = [[' ']*width for i in range(height)]
    previous[start[0]][start[1]] = 0
    print(previous)

    queue = [start]
    print(queue)

     