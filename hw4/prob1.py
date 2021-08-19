from collections import deque

class GNode:
    def __init__(self, id, c = "W", d = -1, p = None):
        self.id = id
        self.color = c
        self.distance = d
        self.parent = p
    
    def __str__(self):
        if (self.parent != None):
            return "(" + self.id + ", " + self.color + ", " \
              + str(self.distance) + ", " + self.parent.id + ")"
        else:
            return "(" + self.id + ", " + self.color + ", " \
              + str(self.distance) + ", None)"

    def __lt__(self, other):
        if self.id < other.id:
            return True
        else :
            return False
 
class Graph:
    def __init__(self, file_name):
        self.G = dict()
        self.node_dict = dict()

        lines = None
        with open(file_name, "r") as f:
            lines = f.readlines()

        # make Node
        node_set = set()
        for line in lines:
            src, tgt = line.strip().split(',')
            node_set.add(int(src))
            node_set.add(int(tgt))

        for node in node_set:
            self.node_dict[node] = GNode(node)
            self.G[self.node_dict[node]] = []

        # make Graph (dictionary list)
        for line in lines:
            src, tgt = line.strip().split(',')
            self.G[self.node_dict[int(src)]].append(self.node_dict[int(tgt)])


    def bfs(self,x):
        # initialize node
        for key in self.node_dict.keys():
            self.node_dict[key].color = 'W'
        ret = []

        # select start node
        s = self.node_dict[x]
        s.color = 'G'
        s.distance = 0
        Q = deque()
        Q.append(s)
        ret.append(s.id)
        
        while len(Q) > 0:
            u = Q.popleft()
            for v in sorted(self.G[u]):
                if v.color == "W":
                    v.color = "G"
                    v.distance = u.distance + 1
                    v.parent = u
                    Q.append(v)
                    ret.append(v.id)
            u.color = "B"

        return ret

    def dfs(self,x):
        # initialize node
        for key in self.node_dict.keys():
            self.node_dict[key].color = 'W'
        ret = []

        # select start node
        s = self.node_dict[x]
        s.color = 'G'
        s.distance = 0
        Stack = deque()
        Stack.append(s)
        
        while len(Stack) > 0:
            u = Stack.pop()
            if u.id not in ret:
                ret.append(u.id)

            for v in sorted(self.G[u], reverse=True):
                if v.color == "W" or v.color == "G":
                    v.color = "G"
                    v.distance = u.distance + 1
                    v.parent = u
                    Stack.append(v)
            u.color = "B"

        return ret
