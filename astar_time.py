import csv
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'


def astar_time(start, end):
    # Begin your code (Part 6)

    # Create the adjacency list
    graph = {}
    with open(edgeFile, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            start_node = int(row["start"])
            end_node = int(row["end"])
            distance = float(row["distance"])
            speed_limit = float(row["speed limit"]) * 5 / 18

            # V = s / t -> t = s / v
            time_required = distance / speed_limit

            if not start_node in graph:
                graph[start_node] = [(time_required, end_node, speed_limit)]
            else:
                graph[start_node].append((time_required, end_node, speed_limit))

    # Get the heuristic value from each node to the target node
    # Assumes the target node is in one of the columns
    heuristic = {}
    with open(heuristicFile, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            current_node = int(row["node"])
            heuristic_end = float(row[str(end)])
            heuristic[current_node] = heuristic_end

    # Set to store visited nodes (closed list)
    visited = set()

    # Open list to store the next node to visit
    # Index 0: time
    # Index 1: path 
    # Index 2: speed limit
    open_list = []
    open_list.append((0, [start], float("inf")))
    while open_list:

        # Get the node to visit
        current_time, current_path, _ = open_list.pop(0)
        current_node = current_path[-1]

        # If already visited, don't visit again
        if current_node in visited:
            continue

        # Otherwise, visit the current node
        visited.add(current_node)

        # If the current node is the destination, return results
        if current_node == end:
            return current_path, current_time, len(visited)
        
        # If the current node doesn't have any adjacent nodes, stop
        if not current_node in graph:
            continue

        # Iterate over all adjacent nodes
        adjacent_nodes = graph[current_node]
        for adjacent_time, adjacent_node, adjacent_speed in adjacent_nodes:

            # If already visited, no need to visit again
            if adjacent_node in visited:
                continue

            # Push the adjacent node to the open list
            new_time = current_time + adjacent_time
            new_path = current_path[:]
            new_path.append(adjacent_node)
            open_list.append((new_time, new_path, adjacent_speed))

        # Sort the open list
        # open_list = sorted(open_list, key=lambda x: x[0] + heuristic[x[1][-1]])
        open_list = sorted(open_list, key=lambda x: x[0] + 1 / x[2])
    
    return None, float("inf"), len(visited)
    
    # End your code (Part 6)


if __name__ == '__main__':
    path, time, num_visited = astar_time(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total second of path: {time}')
    print(f'The number of visited nodes: {num_visited}')
