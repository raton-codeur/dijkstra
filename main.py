import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

G = nx.read_weighted_edgelist("graph.txt")
pos = nx.spring_layout(G, seed=0)

distances = {node: float("inf") for node in G.nodes}
distances["A"] = 0
visited=set()
previous={node: None for node in G.nodes}
current="A"
i_step = 0

def save():
    global i_step

    plt.figure()

    # node colors
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

    # node labels
    labels = {
        node: f"{node}\n{distances[node]}"
        for node in G.nodes
    }

    nx.draw(G, pos, with_labels=True, labels=labels, node_color=colors, node_size=2000)
    weights = {
        edge: int(weight)
        for edge, weight in nx.get_edge_attributes(G, "weight").items()
    }
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights, font_size=12)

    plt.legend(handles=[
        Patch(color="red", label="Current"),
        Patch(color="lightgreen", label="Visited"),
        Patch(color="lightblue", label="Discovered"),
        Patch(color="lightgray", label="Unknown")
    ])

    plt.savefig(f"states/step{i_step}.png")
    i_step += 1
    plt.close()

save()
current = "B"
save()


# def print_graph(G):
#     pos = nx.spring_layout(G)
#     nx.draw(G, pos, with_labels=True)
#     weights = nx.get_edge_attributes(G, "weight")
#     nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)
#     plt.show()
# print_graph(G)


