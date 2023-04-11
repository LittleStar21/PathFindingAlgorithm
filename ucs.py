import csv
from queue import PriorityQueue

edgeFile = 'edges.csv'


def ucs(start, end):
    # Begin your code (Part 3)

    # Create the adjacency list
    graph = {}
    with open(edgeFile, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            start_node = int(row["start"])
            end_node = int(row["end"])
            distance = float(row["distance"])
            # speed_limit = float(row["speed limit"])

            if not start_node in graph:
                graph[start_node] = [(distance, end_node)]
            else:
                graph[start_node].append((distance, end_node))

    # Set to store visited nodes
    visited = set()

    # Stores tuples of length 2 (deque only used as a queue)
    # Index 0: total distance for current path (also used for sorting)
    # Index 1: list containing current path
    # Priority queue to sort by distance
    queue = PriorityQueue()
    queue.put((0, [start]))
    while queue.qsize() != 0:

        # Get the next node with the closest distance
        # Front element in the priority queue
        current_dist, current_path = queue.get()
        current_node = current_path[-1]

        # If already visited, don't visit again
        if current_node in visited:
            continue

        # Otherwise, visit the current node
        visited.add(current_node)

        # If the current node is the destination, return results
        if current_node == end:
            return current_path, current_dist, len(visited)
        
        # If the current node doesn't have any adjacent nodes, stop
        if not current_node in graph:
            continue

        # Iterate over all adjacent nodes
        adjacent_nodes = graph[current_node]
        for adjacent_dist, adjacent_node in adjacent_nodes:

            # If already visited, no need to add to queue
            if adjacent_node in visited:
                continue

            # Push the adjacent node to the queue
            next_path = current_path[:]
            next_path.append(adjacent_node)
            next_dist = current_dist + adjacent_dist
            queue.put((next_dist, next_path))

    # Path not found
    return None, float("inf"), len(visited)

    # End your code (Part 3)


if __name__ == '__main__':
    path, dist, num_visited = ucs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
