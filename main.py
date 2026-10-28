from utils import get_graph, save, print_paths

def main():
    G, pos = get_graph()

    distances = {node: float("inf") for node in G.nodes}
    distances["A"] = 0
    current = "A"
    pending = distances.copy()
    previous = {node: None for node in G.nodes}
    i_step = 0

    save(G, pos, distances, pending, current, i_step)
    i_step += 1

    while pending:
        for neighbor in G.neighbors(current):
            if neighbor in pending:
                new_distance = distances[current] + G[current][neighbor]["weight"]
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    pending[neighbor] = new_distance
                    previous[neighbor] = current

        del pending[current]

        if pending:
            current = min(pending, key=pending.get)
        else:
            current = None

        save(G, pos, distances, pending, current, i_step)
        i_step += 1

    print_paths(G, previous)

if __name__ == "__main__":
    main()
