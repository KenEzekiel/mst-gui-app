from copy import deepcopy
from graph import graph
from prio_queue import prio_queue


def enqueue_all(queue: prio_queue, graph: graph):
    visited = set()
    n_elmt = graph.getLen()
    g_list = graph.getList()
    for i in range(n_elmt):
        for j in range(n_elmt):
            if g_list[i][j] != 0 and i != j and (i, j) not in visited:
                queue.enqueue([g_list[i][j], i, j])
                visited.add((i,j))
                visited.add((j,i))
    return

def isCyclicUtil(v, visited, parent, graph):
        # Algorithm Reference : GFG
        # Mark the current node as visited
        visited[v] = True
        # print(visited)
        # graph.print()
        # Recur for all the vertices
        # adjacent to this vertex
        for i in range(graph.getLen()):
 
            # If the node is not visited then recurse on it

            if (graph.getList()[v][i] != 0 and graph.getList()[v][i] != float('inf')) and v != i:
                if (visited[i] == False):
                    if (isCyclicUtil(i, visited, v, graph)):
                        # print("True 1")
                        return True
            # If an adjacent vertex is visited and not parent of current vertex, then there is a cycle
            
                elif parent != i:
                    # print("parent", parent, i) 
                    # print("True 2")
                    return True
        # print("False")
        return False

def isCyclic(graph: graph):
        # Mark all the vertices as not visited
        visited = [False for i in range(graph.getLen())]
 
        # Call the recursive helper
        # function to detect cycle in different
        # DFS trees
        for i in range(graph.getLen()):
 
            # Don't recur for u if it
            # is already visited
            if visited[i] == False:
                
                if (isCyclicUtil(i, visited, -1, graph)) == True:
                    return True
 
        return False


def kruskal(graph: graph) -> graph:

    n_elmt = graph.getLen()
    output = deepcopy(graph)
    output.to_inf(n_elmt)
    cnt = 0

    p_q = prio_queue()

    # Queue all element first, sort by value, ascending
    enqueue_all(p_q, graph)
    # print(p_q)

    while cnt < n_elmt and not p_q.isEmpty():
        elmt = p_q.dequeue()
        min_val = elmt[0]
        min_i = elmt[1]
        min_j = elmt[2]
        # print("i j", min_i, min_j, "val", min_val)
        temp = deepcopy(output)
        temp.add_edge(min_i, min_j, min_val)
        if not isCyclic(temp):
            # print("final i j", min_i, min_j, "val", min_val)

            output.add_edge(min_i, min_j, min_val)
            cnt += 1
    output.to_zero()
    # output.print()
    return output


