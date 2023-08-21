import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import networkx as nx
import pickle
from math import sin,cos,pi

File = open('testcase1.txt','r')
x = File.readline()
x = x[:-1].split(' ')
vert= int(x[0])
edg= int(x[1])
src = int(x[2])
dst = int(x[3])

# print(vert,edg,src,dst)
adjmat = [[0 for i in range(vert)]for j in range(vert)]
# print(adjmat)
net = []
for i in range(edg-1):
    x = File.readline()
    x = x[:-1].split(' ')
    srctmp = int(x[0])
    dsttmp = int(x[1])
    cp = int(x[2])
    a = tuple([srctmp,dsttmp,cp])
    net.append(a)
    # adjmat[srctmp][dsttmp] = cp

x = File.readline()
x = x.split(' ')
srctmp = int(x[0])
dsttmp = int(x[1])
cp = int(x[2])

a = tuple([srctmp,dsttmp,cp])
net.append(a)


# Create a new directed graph
G = nx.DiGraph()

# Add the edges with weights to the graph
for edge in net:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Load the positions of the nodes from a file
# try:
#     with open('positions.pkl', 'rb') as f:
#         pos = pickle.load(f)
# except FileNotFoundError:
#     pos = nx.spring_layout(G)

# pos = nx.spring_layout(G) # Original supposed to be

num_nodes = vert
radius = vert/2

# Create a regular polygon layout for the nodes
pos = {}
for i in range(num_nodes):
    theta = i * (2 * pi / num_nodes)
    x = radius * cos(theta)
    y = radius * sin(theta)
    pos[i] = (x, y)


# Draw the nodes and edges
nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_edges(G, pos, arrowstyle='->',arrowsize=20) # ,connectionstyle='arc3, rad=0.1'

# Draw the edge labels
# edge_labels = nx.get_edge_attributes(G, 'weight')

labels = {}
for u, v, data in G.edges(data=True):
    if (u, v) in labels:
        labels[(u, v)]["label"] += "\n" + str(data["weight"])
    else:
        labels[(u, v)] = {"label": str(data["weight"])}
    if (v, u) in labels:
        labels[(v, u)]["label"] += "\n" + str(data["weight"])
    else:
        labels[(v, u)] = {"label": str(data["weight"])}

nx.draw_networkx_edge_labels(G, pos, edge_labels= {(u, v): str(d['weight']) for u, v, d in G.edges(data=True)},label_pos=0.3  ) # edge_labels

# Draw the node labels
node_labels = {node: node for node in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels)

# Save the positions of the nodes to a file
with open('positions.pkl', 'wb') as f:
    pickle.dump(pos, f)

# Show the plot
plt.axis('off')
plt.title('Input Graph')
plt.savefig('input.png')
plt.clf()
# plt.show()
File.close()
File = open('output1.txt')

flowGraph = []
residualGraph = []
x = File.readline()
while x != '\n':
    # print(x)
    x=x[:-1].split(' ')
    # print(x)
    tmp=[]
    for i in x:
        if i != '':
            tmp.append(int(i))
    flowGraph.append(tmp)
    x=File.readline()
print(flowGraph)

x = File.readline()
while x != '\n':
    # print(x)
    x=x[:-1].split(' ')
    # print(x)
    tmp=[]
    for i in x:
        if i != '':
            tmp.append(int(i))
    residualGraph.append(tmp)
    x=File.readline()
print(residualGraph)

import pickle
import networkx as nx
import matplotlib.pyplot as plt
from networkx.convert_matrix import from_numpy_array

# Load graph from .pkl file
with open('positions.pkl', 'rb') as f:
    graph = pickle.load(f)

# Load adjacency matrix from file
# flowGraph = ...
# You can load the adjacency matrix from a file, or create it from the graph object.

# Create a NetworkX graph object from the adjacency matrix
G = from_numpy_array(np.array(flowGraph))

# Compute node positions using spring layout
# pos = nx.spring_layout(G)

pos = {}
for i in range(num_nodes):
    theta = i * (2 * pi / num_nodes)
    x = radius * cos(theta)
    y = radius * sin(theta)
    pos[i] = (x, y)


# Get edge labels from adjacency matrix
edge_labels = {(i, j): w for i, row in enumerate(flowGraph) for j, w in enumerate(row) if w > 0}

# Draw the graph using Matplotlib
nx.draw_networkx_nodes(G, pos, node_size=300)
nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle='->',arrowsize=20)
nx.draw_networkx_labels(G, pos,  font_family='sans-serif')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_family='sans-serif',label_pos=0.3)

plt.axis('off')
plt.title('Flow Graph')
plt.savefig('flowGraph.png')

plt.clf()
# plt.show()

import pickle
import networkx as nx
import matplotlib.pyplot as plt
from networkx.convert_matrix import from_numpy_array

# Load graph from .pkl file
with open('positions.pkl', 'rb') as f:
    graph = pickle.load(f)

# Load adjacency matrix from file
# flowGraph = ...
# You can load the adjacency matrix from a file, or create it from the graph object.

# Create a NetworkX graph object from the adjacency matrix
G = from_numpy_array(np.array(residualGraph))

# Compute node positions using spring layout
# pos = nx.spring_layout(G)

pos = {}
for i in range(num_nodes):
    theta = i * (2 * pi / num_nodes)
    x = radius * cos(theta)
    y = radius * sin(theta)
    pos[i] = (x, y)


# Get edge labels from adjacency matrix
edge_labels = {(i, j): w for i, row in enumerate(residualGraph) for j, w in enumerate(row) if w > 0}

# Draw the graph using Matplotlib
nx.draw_networkx_nodes(G, pos, node_size=300)
nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle='->',arrowsize=20,edge_cmap=plt.cm.Reds)
nx.draw_networkx_labels(G, pos,  font_family='sans-serif')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_family='sans-serif',label_pos=0.3)

plt.axis('off')
plt.title('Residual Graph')
plt.savefig('residualGraph.png')

plt.clf()
# plt.show()