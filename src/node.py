class node:
    
    def __init__(self, no, arr):
        self.no = no
        self.edge = {}
        for i in range(len(arr)):
            self.edge[i] = arr[i]
        self.visited = False

    def get_no(self):
        return self.no
    
    def get_edge(self):
        return self.edge
    
    def get_visited(self):
        return self.visited
    
    def visit(self):
        self.visited = True

    def reset(self):
        self.visited = False

