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

        # make node
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


    def get_close(self,x,k):
        # initalize node
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
            u.color = "B"

            if u.distance > k:
                break
            
            if u.id not in ret:
                ret.append(u.id)

        ret.remove(s.id)
        return ret

