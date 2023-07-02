from copy import deepcopy
from graph import graph

def count_clusters(graph: graph):
    cluster_count = 0
    visited = [False for i in range(graph.getLen())]

    for i in range(graph.getLen()):
        if not visited[i]:
            cluster_count += 1
            visit(graph, i, visited)
    
    return cluster_count

def visit(graph: graph, i: int, visited: list):
    stack = []
    stack.append(i)

    while len(stack) != 0:
        node = stack.pop()
        visited[node] = True
        for i in range(graph.getLen()):
            if graph.getList()[node][i] != 0 and graph.getList()[node][i] != float('inf') and not visited[i]:
                stack.append(i)

def get_longest_edge(graph: graph):
    max_elmt = 0
    max_i = 0
    max_j = 0
    for i in range(graph.getLen()):
        for j in range(i+1, graph.getLen()):
            elmt = graph.getList()[i][j]
            if elmt > max_elmt:
                max_elmt = elmt
                max_i = i
                max_j = j

    return max_i, max_j

                

def cluster_mst(mst: graph, n: int):
    clustered = deepcopy(mst)
    while count_clusters(clustered) < n:
        # print(count_clusters(clustered))
        i, j = get_longest_edge(clustered)
        clustered.remove_edge(i, j)
    # clustered.print()
    return clustered
    