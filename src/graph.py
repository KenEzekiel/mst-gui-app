from node import node
class graph:
    # All index starts from 0
    list_rep: list
    list_node: list

    def __init__(self, list_rep):
        self.list_rep = list_rep
        self.list_node = []
        for i in range(len(list_rep)):
            temp = node(i, list_rep[i])
            self.list_node.append(temp)

    def to_inf(self, num: int):
        self.list_rep = [[float('inf') for j in range(num)] for i in range(num)]

    # Prints the list representation of the graph
    def print(self):
        for i in self.list_rep:
            for j in i:
                print(j, end=" ")
            print("")

    # Adds an edge between two nodes with a weight
    def add_edge(self, fr: int, to: int, weight: int):
        # print("len ", len(self.list_rep))
        # print("fr ", fr, "to ", to)
        if len(self.list_rep) - 1 < fr:
            self.add_node()
            fr = len(self.list_rep)-1
            # print(fr)
        if len(self.list_rep) - 1 < to:
            self.add_node()
            to = len(self.list_rep)-1
            # print(to)
        self.list_rep[fr][to] = weight
        self.list_rep[to][fr] = weight

    # Adds a node
    def add_node(self):
        node = [0 for i in range(len(self.list_rep)+1)]
        for i in range(len(self.list_rep)):
            self.list_rep[i].append(0)
        self.list_rep.append(node)

    # Returns the number of element in the graph
    def getLen(self):
        return len(self.list_rep)
    
    def getList(self):
        return self.list_rep

    def to_zero(self):
        for i in range(self.getLen()):
            for j in range(self.getLen()):
                if self.list_rep[i][j] == float('inf'):
                    self.list_rep[i][j] = 0