from numpy import e
from visual import visualize_maze 
from parse import get_matrix
import search

matrix, bonus_points, start, end = get_matrix('maze_map.txt')
route = search.BFS(matrix, start, end)
visualize_maze(matrix, bonus_points, start, end, route)