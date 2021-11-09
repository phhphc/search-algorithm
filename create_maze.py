maze = [
'''2
3 6 -3
5 14 -1
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x   x   xx xx        xxxxx x       x
x     x     xxx xxxxxxxxx    xxxxxxx
x x   +xx  xxxx xxx xxxx   xxx xxxxx
  x   x x xx   xxxx     xx   x x   x
x          xx +xx  x xxxxx  xx x xxx
xxxxxxx x      xx  x xxxxxx xx x xxx
xxxxxxxxx  x x  xx      xx  x    xxx
x          x x  x    x xxx  x xx xxx
xxxxx x  x x x     x x   S    xx xxx
xxxxx x         xx x    xxxx xxx xxx
xxxxx   xxxxxxx    x  xxxxxx xxxxxxx
x      xxxxxxxx xx   xxxxxx  xxxxxxx
xxxxxxxxxxxxxxx xx xxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx''',
'''2
3 6 -3
5 14 -1
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxx                x             x
xxx   x   x  xxx xx     x x xxx x xx
x    x+x  x    x xx  xxxxxxxxxxxxxxx
x  x   x  x  x x     x             x
x  xx     xxxx+x     x             x
x  x  x x     x x             S     
x  x  x  xx x        x     xxxx    x
xxx    x  x  x x x  x x    x  x    x
xxx              xx        x  x    x
x xxxx xxxxxx xx  x x x xxxx xxxx xx
x  xxx xxxx   xxx   xxx xxx   xxxx x
x  xxx   xx xxxxx xx xx xxxx xxxxx x
x                                  x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx''',
'''4
3 6 -10
3 5 -10
4 5 -10
5 14 -10
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x   x   xx                   x   x
x     x     xxxxxxxxxxxxxxxx     x
x    ++xxxxxxxx xxx x   x   xx   x
x    +x x xx   xxxx     x    x   x
x    x     xx +xx  xxx  x    xxx x
x   x   x      xx  x   xx  x x x x
x  xxxx                        x x
x x                        S   x x
x xxx x  x x x    x            x x
x x        x xxx  x  xxx    x  x x
x x x   x         x  x   x  x  x x
x x xxxxxxxxxxxxxx xxxx  xxxxxxx x
x     x                 xx       x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxx''',
'''2
3 6 -7
5 14 -2
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x   x   xx xx        xx   xx  x  x
x     x     xxxxxxxxxx   x x  x  x
x x   +xx  xxxx xxx xx   x x  x xx
  x   x x xx   xxxx  x          xx
x x        xx +xx  x x  x xxx  xxx
x   xxx x      xx  x x   xxxx xxxx
xxxxxxxxx  x x  xx   x      x   xx
x          x x Sx x  x     xxx  xx
xxxxx x  x x x     x x  xx       x
x    xx xxxxxx x  xx xxx xxxx xxxx
xxxxx xx xxxxx    xx   x xxx  xxxx
xxxx  x  xxx x xx xxxx xxxx   xxxx
xxx      xxx   x   xxx xxx xxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx''',
'''0
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x   x   xx xx        xxxxx xxxxxxx
x     x     xxxxxxxxxxx    x  xxxx
x x    xx  xxxx     xxx xxx  xxxxx
x x   x x xx     x       xx xxxxxx
x          xx  xx  x xx xxx    xxx
xxxxxxx x      xx  x xx xxx xx xxx
xxxxxxxxx  x x  x x  xx     xx xxx
x          x x Sx x  xxx xxx   xxx
xxxxx x  x x x    x      xxx x  xx
xxx x xx xxxxxx xx x xxx xxx xx xx 
xxx   xx xxxxxx    x xx  xx  xx xx
x x  xxx xxxxxxx xxx xxx xxx xx xx
x                     xx   x  x xx
xxxxxxxxxxxxxxxxxxxx xxxxxxxxxxxxx''',
'''0
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x   x   xx xx        xxxxx x       x
x     x     xxx xxxxxxxxx    xxxxxxx
x x    xx  xxxx xxx xxxx   xxx xxxxx
x x   x x xx   xxxx     xx   x x     
x          xx  xx  x xxxxx  xx x xxx
xxxxxxx x      xx  x xxxxxx xx x xxx
xxxxxxxxx  x x  xx      xx  x    xxx
x          x x Sx    x xxx  x xx xxx
xxxxx x  x x x     x x        xx xxx
xxxxx x         xx x    xxxx xxx xxx
xxxxx   xxxxxxx    x  xxxxxx xxxxxxx
x      xxxxxxxx xx   xxxxxx  xxxxxxx
xxxxxxxxxxxxxxx xx xxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx''',
'''0
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
xxxxx                x             x
xxx   x   x  xxx xx     x x xxx x xx
x    x x  x    x xx  xxxx xxxxxxx xx
x  x   x  x  x x     x             x
x  xx     xxxx x     x             x
x  x  xxx     x x    x             x
x  x  x  xxxx        x     xxxx    x
xxx    x  x  x xSx  x x    x  x    x
xxx              xx   x    x  x    x
x xxxx xxxxxx xx  x x x xxxx xxxx xx
x  xxxxxxxx   xxx   xxx xxx   xxxx x
x  xxxx  xx xxxxx xx xx xxxx xxxxx x
x           xxxx  xx               x 
xxxxxxxxxxxxxxxxxxxxxxxxxx xxxxxxxxx''',
'''0
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x   x   xx xx                    x
x     x     xxxxxxxxx   x        x
x x    xx  xxxx xxx x   x    x   x
x x   x x xx   xxxx     x    x   x
x          xx  xx  xxx  x    xxxxx
xxxxxxx x      xx  x   xx  x x xxx
xxxxxxxxx  x x  x       x  x    xx
x          x x Sx xxxxxxx  x  xxxx
xxxxx x  x x x    x            x x
xxxxx      x xxx  x  xxx    x  x x
xxxxx   x         x  x   x  x    x
xxxxxxxxxxxxxxxx     xx  x  xxxx x
x                       xx     x x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxx''',
'''0
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x   x   xx xx        xx   xx  x  x
x     x     xxxxxxxxxx   x x  x  x
x x    xx  xxxx xxx xx   x x  x xx
  x   x x xx   xxxx  x          xx
x x        xx  xx  x x  x xxx  xxx
x   xxx x      xx  x x   xxxx xxxx
xxxxxxxxx  x x  xx   x      x   xx
x          x x Sx x  x     xxx  xx
xxxxx x  x x x     x x  xx       x
x     xx xxxxxx x  xx xxx xxxx xxxx
xxxxx xx xxxxx    xx   x xxx  xxxx
xxxx  x  xxx x xx xxxx xxxx   xxxx
xxx      xxx   x   xxx xxx xxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx''',
'''2
7 9 -8
5 13 -4
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x   x   xx xx        xx   xx  x  x
x     x     xxxxxxxxxx   x x  x  x
x x    xx  xxxx xxx xx   x x  x xx
  x   x x xx   xxxx  x          xx
x x        xx+ xx  x x  x xxx  xxx
x   xxx x      xx  x x   xxxx xxxx
xxxxxxxxx+ x x  x    x      x   xx
x          x x  x x  x     xxx  xx
xxxxx x  x x x     x x  xx       x
x     xx xxxxxx x  x  xxx    x xxx
xxxxx xx xxxxx    xx       S  xxxx
xxxx  x  xxx x xx xx x xxxx   xxxx
xxx      xxx   x       xxx xxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx''',
'''5
13 1 -13
5 7 -16
2 4 -5
3 4 -6
2 8 -14
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x   x   xx xx                    x
x   + x +   xxxxxxxxx   x        x
x x +  xx  xxxx xxx x   x    x   x
x x   x x xx   xxxx     x    x   x
x      +   xx  xx  xxx  x    xxxxx
xxxxxxx x      xx  x   xx  x x xxx
xxxxxxxxx  x x  x       x  x    xx
x          x x Sx xxxxxxx  x  xxxx
xxxxx x  x x x    x            x x
xxxxx      x xxx  x  xxx    x  x x
xxxxx   x         x  x   x  x    x
xxxxxxxxxxxxxxxx     xx  x  xxxx x
x+                      xx     x x
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx xxx''',
'''10
1 2 -14
2 4 -13
4 4 -15
11 3 -16
13 4 -11
13 7 -12
12 10 -7
1 29 -2
9 32 -13
12 28 -11
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
x + x   xx xx        xxxxx x +     x
x   + x     xxx xxxxxxxxx    xxxxxxx
x x    xx  xxxx xxx xxxx   xxx xxxxx
x x + x x xx   xxxx     xx   x x     
x          xx  xx  x xxxxx  xx x xxx
xxxxxxx x      xx  x xxxxxx xx x xxx
xxxxxxxxx  x x  xx      xx  x    xxx
x          x x Sx    x xxx  x xx xxx
xxxxx x  x x x     x x        xx+xxx
xxx   x         xx x    xxxx xxx xxx
xxx+x   xxxxxxx    x  xxxxxx xxxxxxx
x         +xxxx xx   xxxx   +  xxxxx
xxxx+xx+xxxxxxx xx xxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'''
]

print("maze length: %d"%len(maze))
n = int(input('Select maze: '))%len(maze)
with open('maze_map.txt', 'w') as outfile:
  outfile.write(maze[n])


