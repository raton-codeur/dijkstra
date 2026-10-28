import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def get_graph():
    G = nx.read_weighted_edgelist("graph.txt")
    for node1, node2 in G.edges:
        G[node1][node2]["weight"] = int(G[node1][node2]["weight"])
    pos = nx.spring_layout(G, seed=0)
    return G, pos

def save(G, pos, distances, pending, current, i_step):
    plt.figure()

    node_colors = []
    for node in G.nodes:
        if node == current:
            node_colors.append("red")
        elif node not in pending:
            node_colors.append("lightgreen")
        elif distances[node] < float("inf"):
            node_colors.append("lightblue")
        else:
            node_colors.append("lightgray")

    node_labels = {
        node: f"{node}\n{distances[node]}"
        for node in G.nodes
    }

    nx.draw(G, pos, with_labels=True, labels=node_labels, node_color=node_colors, node_size=2000)

    weights = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights, font_size=12)

    plt.legend(handles=[
        Patch(color="red", label="Current"),
        Patch(color="lightgreen", label="Visited"),
        Patch(color="lightblue", label="Discovered"),
        Patch(color="lightgray", label="Unknown")
    ])

    plt.savefig(f"states/step{i_step:03d}.png")
    plt.close()

def print_paths(G, previous):
    for node in G.nodes:
        path = [node]
        while previous[path[-1]] is not None:
            path.append(previous[path[-1]])

        print(" <- ".join(path))
