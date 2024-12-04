from graph_data import graph_data
import math



def compute_shortest_paths(weight_matrix):
    node_count = len(weight_matrix)
    distance_matrix = [row[:] for row in weight_matrix]
    predecessor_matrix = [[None] * node_count for _ in range(node_count)]

    for intermediate_node in range(node_count):
        for source_node in range(node_count):
            for target_node in range(node_count):
                if distance_matrix[source_node][intermediate_node] + distance_matrix[intermediate_node][target_node] < distance_matrix[source_node][target_node]:
                    distance_matrix[source_node][target_node] = distance_matrix[source_node][intermediate_node] + distance_matrix[intermediate_node][target_node]
                    predecessor_matrix[source_node][target_node] = intermediate_node
    return distance_matrix, predecessor_matrix
def convert_graph_to_matrix(input_graph):
    node_count = len(input_graph)
    adjacency_matrix = [[math.inf] * node_count for _ in range(node_count)]
    for node_index, node_data in enumerate(input_graph):
        for neighbor_index in node_data[1]:
            adjacency_matrix[node_index][neighbor_index] = math.sqrt(
                (input_graph[node_index][0][0] - input_graph[neighbor_index][0][0]) ** 2 +
                (input_graph[node_index][0][1] - input_graph[neighbor_index][0][1]) ** 2
            )
        adjacency_matrix[node_index][node_index] = 0
    return adjacency_matrix

def build_path(predecessor_matrix, start_node, end_node):
    if predecessor_matrix[start_node][end_node] is None:
        return [start_node, end_node] if start_node != end_node else [start_node]
    intermediate_node = predecessor_matrix[start_node][end_node]
    return build_path(predecessor_matrix, start_node, intermediate_node)[:-1] + build_path(predecessor_matrix, intermediate_node, end_node)

def find_optimal_path(input_graph, target_node):
    adjacency_matrix = convert_graph_to_matrix(input_graph)
    _, predecessor_matrix = compute_shortest_paths(adjacency_matrix)
    path_to_target = build_path(predecessor_matrix, 0, target_node)
    path_from_target = build_path(predecessor_matrix, target_node, len(input_graph) - 1)

    return path_to_target[:-1] + path_from_target

if __name__ == "__main__":
    selected_graph = graph_data[3]
    optimal_path = find_optimal_path(selected_graph, 0)
    print(f"Path: {optimal_path}")
