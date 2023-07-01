from graph import graph
from prim import prim
from kruskal import kruskal
from graph_visualization import visualize, visualize_with_MST


# Get input from text file
# Outputs a class representation of graph
def open_file(file_name: str) -> graph:
    file = open(file_name, "r")
    file = file.read()
    # print(file)
    file = file.split("\n")
    for i in range(len(file)):
        file[i] = (file[i].split(" "))
        for j in range(len(file[i])):
            if (file[i][j] == ""):
                del file[i][j]

    for i in range(len(file)):
        for j in range(len(file[i])):
            file[i][j] = int(file[i][j])

    output = graph(file)
    # output.print()
    return output
    

# test = open_file("./txt/b.txt")
# test.print()
# pos = visualize(test)
# test.add_edge(0, 6, 10)
# test.add_edge(0, 7, 15)
# test.print()
# out1 = prim(test)
# out2 = kruskal(test)

# check = True
# for i in range(out1.getLen()):
#     for j in range(out1.getLen()):
#         if out1.getList()[i][j] != out2.getList()[i][j]:
#             check = False

# print(check)
# visualize_with_MST(test, out1, pos)