import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()


nodes = {
    "m0": (1, 0, 0, 0),  # Початковий стан: 1 маркер у вхідному буфері
    "m1": (0, 1, 0, 0),  # Процес 1 записує у буфер
    "m2": (0, 0, 1, 0),  # Процес 2 обробляє повідомлення
    "m3": (0, 0, 0, 1),  # Обробка завершена, результат у вихідному буфері
    "m4": (0, 1, 1, 1)   # Обидва процеси завершили роботу
}
G.add_nodes_from(nodes.keys())


edges = [
    ("m0", "m1"),  # t1: Процес 1 пише у буфер
    ("m1", "m2"),  # t2: Процес 2 обробляє
    ("m2", "m3"),  # t3: Результат потрапляє у вихідний буфер
    ("m1", "m4"),  # t4: Процес 3 обробляє паралельно
    ("m3", "m0")   # t5: Повернення до початкового стану
]
G.add_edges_from(edges)

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightgreen", font_size=10, font_weight="bold")

labels = {node: f"{node}\n{nodes[node]}" for node in nodes}
for node, (x, y) in pos.items():
    plt.text(x, y - 0.03, f"{nodes[node]}", fontsize=8, ha='center', bbox=dict(facecolor='white', alpha=0.6, edgecolor='none'))

nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"t{i+1}" for i, (u, v) in enumerate(edges)}, font_size=10)

plt.title("Модель взаємодії трьох процесів у мережі Петрі")
plt.show()
