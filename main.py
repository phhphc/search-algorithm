from visual import visualize_maze 
from parse import get_matrix

matrix, bonus_points, start, end = get_matrix('maze_map.txt')
print(f'The height of the matrix: {len(matrix)}')
print(f'The width of the matrix: {len(matrix[0])}')
visualize_maze(matrix,bonus_points,start,end)