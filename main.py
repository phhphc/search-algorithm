from numpy import e
from visual import visualize_maze 
from parse import get_matrix
import search

matrix, bonus_points, start, end = get_matrix('maze_map.txt')
route, browse = search.AStar(matrix, start, end, bonus_points)
visualize_maze(matrix, bonus_points, start, end, route, browse)