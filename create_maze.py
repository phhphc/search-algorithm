maze = [
'''2
3 6 -3
5 14 -1
xxxxxxxxxxxxxxxxxxxxxx
x   x   xx xx        x
x     x     xxxxxxxxxx
x x   +xx  xxxx xxx xx
  x   x x xx   xxxx  x
x          xx +xx  x x
xxxxxxx x      xx  x x
xxxxxxxxx  x x  xx   x
x          x x Sx x  x
xxxxx x  x x x     x x
xxxxxxxxxxxxxxxxxxxxxx''',
'''2
3 6 -3
5 14 -1
xxxxxxxxxxxxxxxxxxxxxx
                     x
x                    x
x     +              x
x                    x
x             +      x
x                    x
x                    x
x              S     x
x                    x
xxxxxxxxxxxxxxxxxxxxxx''',
'''2
3 6 -32
5 14 -2
xxxxxxxxxxxxxxxxxxxxxx
x   x   xx xx        x
x     x     xxxxxxxxxx
x x   +xx  xxxx xxx xx
x x   x x xx   xxxx  x
x          xx +xx  x x
xxxxxxx x      xx  x x
xxxxxxxxx  x x  x    x
x          x x Sx x  x
xxxxx x  x x x    x  x
xxxxxxxxxxxxxxxxxxxx x''',
'''0
xxxxxxxxxxxxxxxxxxxxxx
x   x   xx xx        x
x     x     xxxxxxxxxx
x x    xx  xxxx xxx xx
x x   x x xx   xxxx  x
x          xx  xx  x x
xxxxxxx x      xx  x x
xxxxxxxxx  x x  x    x
x          x x Sx x  x
xxxxx x  x x x    x  x
xxxxxxxxxxxxxxxxxxxx x''',
'''2
3 6 -7
5 14 -2
xxxxxxxxxxxxxxxxxxxxxx
x   x   xx xx        x
x     x     xxxxxxxxxx
x x   +xx  xxxx xxx xx
  x   x x xx   xxxx  x
x x        xx +xx  x x
x   xxx x      xx  x x
xxxxxxxxx  x x  xx   x
x          x x Sx x  x
xxxxx x  x x x     x x
xxxxxxxxxxxxxxxxxxxxxx''',
'''5
3 6 -3
8 2 -10
8 4 -10
9 2 -10
9 19 -10
xxxxxxxxxxxxxxxxxxx xx
x                    x
x                    x
x     +              x
x                    x
x                    x
x                    x
x                    x
x + +          S     x
x +                + x
xxxxxxxxxxxxxxxxxxxxxx'''
]

print("maze length: %d"%len(maze))
n = int(input('Select maze: '))%len(maze)
with open('maze_map.txt', 'w') as outfile:
  outfile.write(maze[n])


