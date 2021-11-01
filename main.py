from numpy import e
from visual import visualize_maze 
from parse import get_matrix
import search

matrix, bonus_points, start, end = get_matrix('maze_map.txt')
search.BFS(matrix, start, end)
print(f'The height of the matrix: {len(matrix)}')
print(f'The width of the matrix: {len(matrix[0])}')
print(matrix)
print(bonus_points)
print(start)
print(end)
#visualize_maze(matrix,bonus_points,start,end)