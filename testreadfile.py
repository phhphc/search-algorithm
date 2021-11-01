from collections import defaultdict

f=open("test.txt");
a=f.readline();
line=[];
line.append(a);
k=0;
while (a!=""):
    a=f.readline();
    line.append(a);
for i in line:
    print(i);
        
#for i in line:
#    for j in enumerate(i):
#        print(line.index(i), j);

"""class point:
    def __init__(self,i,j, data):
        self.i=i;
        self.j=j;
        self.data=data;
    def printPoint(self):
        print(self.i,",",self.j,":",self.data);"""


"""for i in listP:
    if(i.data=="s"): i.printPoint();
    if(i.data=="e"): i.printPoint();"""

for x,i in enumerate(line):
    for y, j in enumerate(i):
        if(j=="s"): print(x,y,j);
        if(j=="e"): print(x,y,j);

class graph:
    def __init__(self):
        self._graph = defaultdict(set);

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        #if not self._directed:
         #   self._graph[node2].add(node1);

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1];

def addtoGraph(line=[], g=graph):
    for x,i in enumerate(line):
        for y,j in enumerate(i):
            #some fvcking dumb code that show that i so fvcking suck at python
            if(j==" " or j=="s" or j=="e"):
                if (line[x][y+1] is not None): 
                    if(line[x][y+1]==" " or line[x][y+1]=="s" or line[x][y+1]=="e"): g.add(line[x][y],line[x][y+1]);
                if(line[x][y-1] is not None):
                   if(line[x][y-1]==" " or line[x][y-1]=="s" or line[x][y-1]=="e"): g.add(line[x][y],line[x][y-1]);
                if(line[x+1][y+1] is not None):
                   if(line[x+1][y+1]==" " or line[x+1][y+1]=="s" or line[x+1][y+1]=="e"): g.add(line[x][y],line[x+1][y+1]);
                if(line[x-1][y+1] is not None):
                   if(line[x-1][y+1]==" " or line[x-1][y+1]=="s" or line[x-1][y+1]=="e"): g.add(line[x][y],line[x-1][y+1]);
                if(line[x+1][y-1] is not None):
                   if(line[x+1][y-1]==" " or line[x+1][y-1]=="s" or line[x+1][y-1]=="e"): g.add(line[x][y],line[x+1][y-1]);
                if(line[x-1][y-1] is not None):
                   if(line[x-1][y-1]==" " or line[x-1][y-1]=="s" or line[x-1][y-1]=="e"): g.add(line[x][y],line[x-1][y-1]);
                if(line[x+1][y] is not None):
                   if(line[x+1][y]==" " or line[x+1][y]=="s" or line[x+1][y]=="e"): g.add(line[x][y],line[x+1][y]);
                if(line[x-1][y] is not None):
                   if(line[x-1][y]==" " or line[x-1][y]=="s" or line[x-1][y]=="e"): g.add(line[x][y],line[x-1][y]);

#g=graph();
#addtoGraph(line, g);
#print(g.is_connected(line[2][0],line[2][1]));