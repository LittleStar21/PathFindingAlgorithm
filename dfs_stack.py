import csv

edgeFile = 'edges.csv'

def dfs(start, end):
    # Begin your code (Part 2)
    
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
    
    # List for representing a stack, start-end = bottom-top
    # Stores tuples of length 2 (deque only used as a queue)
    # Index 0: total distance for current path 
    # Index 1: list containing current path
    stack = []
    stack.append((0, [start]))
    while stack:

        # Pop the top element in the stack
        current_dist, current_path = stack.pop()
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

            # Push the adjacent node to the stack
            next_path = current_path[:]
            next_path.append(adjacent_node)
            next_dist = current_dist + adjacent_dist
            stack.append((next_dist, next_path))
        
    # Path not found
    return None, float("inf"), len(visited)

    # End your code (Part 2)


if __name__ == '__main__':
    path, dist, num_visited = dfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
