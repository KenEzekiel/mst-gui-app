from copy import deepcopy
from graph import graph
from prio_queue import prio_queue

def visit_node(queue, arr, node, visited):
    if node not in visited:
        visited.add(node)
        for i in range(len(arr)):
            if arr[i] != 0 and i != node:
                queue.enqueue([arr[i], node, i])


def prim(graph: graph) -> graph:
    # Initialization
    visited = set()
    n_elmt = graph.getLen()
    g_list = graph.getList()
    output = deepcopy(graph)
    output.to_inf(n_elmt)
    node = 0
    q = prio_queue()
    # Execution
    visit_node(q, g_list[node], node, visited)
    # print("visited", visited)
    while not q.isEmpty():
        elmt = q.dequeue()
        val = elmt[0]
        prev = elmt[1]
        node = elmt[2]
        if (node not in visited):
            output.add_edge(prev, node, val)
        visit_node(q, g_list[elmt[2]], elmt[2], visited)
        # print("visited", visited)        
    
    output.to_zero()
    # output.print()
    return output

