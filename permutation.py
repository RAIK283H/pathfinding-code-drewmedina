import math

def sjt(graph):
    n = len(graph)
    if n == 0:
        return []
    paths = []
    initial_path = [[i, True] for i in range(n)]
    paths.append([i[0] for i in initial_path])
    def largest_mobile_values(array):
        ans = (float('-inf'), False)
        index = -1
        for i in range(len(array)):
            if array[i][1]:
                if i - 1 >= 0 and array[i - 1][0] < array[i][0]:
                    if array[i][0] > ans[0]:
                        ans = array[i]
                        index = i
            if not array[i][1]:
                if i + 1 < len(array) and array[i + 1][0] < array[i][0]:
                    if array[i][0] > ans[0]:
                        ans = array[i]
                        index = i
        return ans, index
    def flip_larger(array, mobile):
        for i in range(len(array)):
            if array[i][0] > mobile:
                array[i][1] = not array[i][1]
                
    largest_mobile, mobile_index = largest_mobile_values(initial_path)
    while mobile_index > -1:
        if largest_mobile[1]:
            initial_path[mobile_index], initial_path[mobile_index - 1] = initial_path[mobile_index - 1], initial_path[mobile_index]
            paths.append([i[0] for i in initial_path])
        else:
            initial_path[mobile_index], initial_path[mobile_index + 1] = initial_path[mobile_index + 1], initial_path[mobile_index]
            paths.append([i[0] for i in initial_path])
        flip_larger(initial_path, largest_mobile[0])
        largest_mobile, mobile_index = largest_mobile_values(initial_path)
    return paths
def check_hamiltonian(graph, paths):
    valid_cycles = []
    def is_valid(path):
        for i in range(len(path) - 1):
            if path[i + 1] not in graph[path[i]][1]:
                return False
        return True
    for path in paths:
        if is_valid(path + [path[0]]):
            valid_cycles.append(path + [path[0]])
    return valid_cycles
def optimal_cycles(graph, paths):
    def tot_distance(path):
        return sum([math.sqrt(((graph[path[i]][0][0] - graph[path[i + 1]][0][0]) ** 2) + ((graph[path[i]][0][1] - graph[path[i + 1]][0][1]) ** 2)) for i in range(len(path) - 1)])
    optimal_cycles = []
    current_min = float('inf')
    valid_cycles = check_hamiltonian(graph, paths)
    for cycle in valid_cycles:
        curr_distance = tot_distance(cycle)
        if curr_distance < current_min:
            current_min = curr_distance
            optimal_cycles = [cycle]
        elif curr_distance == current_min:
            optimal_cycles.append([cycle])
    return optimal_cycles
def get_largest_clique(graph):
    nodes = range(1, len(graph))
    def is_clique(subset):
        for i in range(len(subset)):
            for j in range(len(subset)):
                if j != i and subset[j] not in graph[subset[i]][1]:
                    return False
        return True
    largest_clique = []
    def get_subsets(subset, index):
            nonlocal largest_clique
            if index == len(nodes):
                if is_clique(subset) and len(subset) > len(largest_clique):
                    largest_clique = subset.copy()
                return
            subset.append(nodes[index])
            get_subsets(subset, index + 1)
            subset.pop()
            get_subsets(subset, index + 1)
    get_subsets([], 0)
    return largest_clique if largest_clique else []
