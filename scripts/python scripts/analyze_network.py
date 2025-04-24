import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
 
# Load data
data = pd.read_csv("data/book5.csv")
graph = nx.from_pandas_edgelist(data, source='Source', target='Target')
 
# Visualize the graph
nx.draw(graph, with_labels=True, node_color='skyblue', node_size=1500, edge_color='gray')
plt.show()