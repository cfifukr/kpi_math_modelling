
import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()

nodes = ["M0", "M1", "M2", "M3", "M4"]
G.add_nodes_from(nodes)


edges = [("M0", "M1"), ("M1", "M2"), ("M2", "M3"), ("M3", "M4"), ("M4", "M2"), ("M1", "M0")]
G.add_edges_from(edges)

pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=15, font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"t{i+1}" for i, (u, v) in enumerate(edges)}, font_size=12)
plt.title("Граф досяжних розміток мережі Петрі")
plt.show()