# write a visulaizer for the graph taken from the testcase1.txt

import networkx as nx
import matplotlib.pyplot as plt

# read the graph from the file
G = nx.read_edgelist("testcase1.txt", create_using=nx.Graph(), nodetype=int)

# draw the graph
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
