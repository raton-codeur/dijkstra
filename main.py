import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge("A", "B", weight=4)
G.add_edge("A", "B", weight=4)
G.add_edge("A", "C", weight=2)
G.add_edge("B", "C", weight=1)
G.add_edge("B", "D", weight=5)
G.add_edge("C", "D", weight=8)
G.add_edge("C", "E", weight=10)
G.add_edge("D", "E", weight=2)
G.add_edge("D", "F", weight=6)
G.add_edge("E", "F", weight=3)
pos = nx.spring_layout(G, seed=0)

distances = {node: float("inf") for node in G.nodes}
distances["A"] = 0
visited = set()
previous = {node: None for node in G.nodes}

# def print_graph(G):
#     pos = nx.spring_layout(G)
#     nx.draw(G, pos, with_labels=True)
#     weights = nx.get_edge_attributes(G, "weight")
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
#     plt.show()
# print_graph(G)

def draw_state(G, distances, previous, visited, current=None):
    pos = nx.spring_layout(G, seed=42)

    # Colors for each node
    colors = []
    for node in G.nodes:
        if node == current:
            colors.append("red")
        elif node in visited:
            colors.append("lightgreen")
        elif distances[node] < float("inf"):
            colors.append("lightblue")
        else:
            colors.append("lightgray")

    # Node labels: name + distance
    labels = {}
    for node in G.nodes:
        distance = distances[node]
        labels[node] = f"{node}\n{distance}"

    # Draw the graph
    nx.draw(
        G, pos,
        labels=labels,
        with_labels=True,
        node_color=colors,
        node_size=1100
    )

    # Highlight predecessor edges
    path_edges = [
        (parent, node)
        for node, parent in previous.items()
        if parent is not None
    ]

    nx.draw_networkx_edges(
        G, pos,
        edgelist=path_edges,
        edge_color="green",
        width=3
    )

    # Display edge weights
    weights = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

    plt.show()



# graphe = {
#     "A": {"B": 4, "C": 2},
#     "B": {"A": 4, "C": 1, "D": 5},
#     "C": {"A": 2, "B": 1, "D": 3},
#     "D": {"B": 5, "C": 3}
# }
# start = "A"
# end = "D"
# distances = {noeud: float("inf") for noeud in graphe}
# distances[start] = 0
# visited = set()

# def main():
#     print("test")

# if __name__ == "__main__":
#     main()
