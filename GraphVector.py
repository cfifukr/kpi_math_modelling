
import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

nodes = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 1, 0, 1)]
G.add_nodes_from(nodes)

edges = [((1, 0, 0, 0), (0, 1, 0, 0)),  # t1: перехід зі стану 1 у 2
         ((0, 1, 0, 0), (0, 0, 1, 0)),  # t2
         ((0, 0, 1, 0), (0, 0, 0, 1)),  # t3
         ((0, 0, 0, 1), (0, 1, 0, 1)),  # t4
         ((0, 1, 0, 1), (0, 0, 1, 0)),  # t5
         ((0, 1, 0, 0), (1, 0, 0, 0))]  # t6: повернення у початковий стан
G.add_edges_from(edges)

pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold")
labels = {node: str(node) for node in nodes}
nx.draw_networkx_labels(G, pos, labels, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"t{i+1}" for i, (u, v) in enumerate(edges)}, font_size=10)
plt.title("Граф досяжних розміток мережі Петрі")
plt.show()