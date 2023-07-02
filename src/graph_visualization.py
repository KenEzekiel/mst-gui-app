from copy import deepcopy
import networkx as nx
import graph
import matplotlib.pyplot as plt

def visualize(graph: graph):
    g = nx.Graph()
    g.add_nodes_from([i for i in range(graph.getLen())])

    for i in range(graph.getLen()):
        for j in range(i+1, graph.getLen()):
            elmt = graph.getList()[i][j]
            if elmt != 0 and elmt != float('inf'):
                # g.add_weighted_edges_from([(i, j, elmt)])
                g.add_edge(i, j, weight=elmt)

    
    # pos = nx.get_node_attributes(g,'pos')
    pos = nx.shell_layout(g)
    nx.draw(g, pos, with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(g,'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
    plt.savefig('./img/plotgraph.png', dpi=300, bbox_inches='tight')
    plt.clf()
    return deepcopy(pos)


def visualize_with_MST(graph: graph, MST: graph, pos):
    mst = nx.Graph()
    mst.add_nodes_from([i for i in range(graph.getLen())])

    for i in range(graph.getLen()):
        for j in range(i+1, graph.getLen()):
            elmt = graph.getList()[i][j]
            if elmt != 0 and elmt != float('inf'):
                if MST.getList()[i][j] == elmt:
                    mst.add_edge(i, j, weight=elmt, color='red', width=3)
                else:
                    mst.add_edge(i, j, weight=elmt, color='gray', width=1)

    # pos = nx.get_node_attributes(g,'pos')
    pos = pos
    edges = mst.edges()
    colors = [mst[u][v]['color'] for u,v in edges]
    width = [mst[u][v]['width'] for u,v in edges]
    nx.draw(mst, pos, with_labels=True, font_weight='bold', edge_color=colors, width=width)
    labels = nx.get_edge_attributes(mst,'weight')
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels)
    plt.savefig('./img/MST.png', dpi=300, bbox_inches='tight')
    plt.clf()

def visualize_cluster(clustered: graph):
    g = nx.Graph()
    g.add_nodes_from([i for i in range(clustered.getLen())])
    for i in range(clustered.getLen()):
        for j in range(i+1, clustered.getLen()):
            elmt = clustered.getList()[i][j]
            if elmt != 0 and elmt != float('inf'):
                g.add_edge(i, j, weight=elmt, color='green', width=5)

    pos = nx.shell_layout(g)
    edges = g.edges()
    colors = [g[u][v]['color'] for u,v in edges]
    width = [g[u][v]['width'] for u,v in edges]
    nx.draw(g, pos, with_labels=True, font_weight='bold', edge_color=colors, width=width)
    labels = nx.get_edge_attributes(g,'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
    plt.savefig('./img/Cluster.png', dpi=300, bbox_inches='tight')
    plt.clf()
