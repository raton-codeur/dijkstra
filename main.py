import networkx as nx
import matplotlib.pyplot as plt
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class State:
    distances: dict
    visited: set
    previous: dict
    current: str | None

def get_graph():
    result = nx.Graph()
    result.add_edge("A", "B", weight=4)
    result.add_edge("A", "B", weight=4)
    result.add_edge("A", "C", weight=2)
    result.add_edge("B", "C", weight=1)
    result.add_edge("B", "D", weight=5)
    result.add_edge("C", "D", weight=8)
    result.add_edge("C", "E", weight=10)
    result.add_edge("D", "E", weight=2)
    result.add_edge("D", "F", weight=6)
    result.add_edge("E", "F", weight=3)
    return result
G = get_graph()
pos = nx.spring_layout(G, seed=0)

states = []
state = State(
    distances={node: float("inf") for node in G.nodes},
    visited=set(),
    previous={node: None for node in G.nodes},
    current="A"
)
state.distances["A"] = 0
states.append(deepcopy(state))

def draw_state(G, state):
    



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
