import graph_data
import global_game_data
from numpy import random
from collections import deque
def set_current_graph_paths():
    global_game_data.graph_paths.clear()
    global_game_data.graph_paths.append(get_test_path())
    global_game_data.graph_paths.append(get_random_path())
    global_game_data.graph_paths.append(get_dfs_path())
    global_game_data.graph_paths.append(get_bfs_path())
    global_game_data.graph_paths.append(get_dijkstra_path())


def get_test_path():
    return graph_data.test_path[global_game_data.current_graph_index]


def get_random_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    assert(graph)
    end = len(graph) - 1
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    def dfs(path, index, target):
        if index in visited or (index == end and target != end):
            return False, []
        path.append(index)
        if index == target:
            return True, path.copy()
        visited.add(index)
        connects = graph[index][1].copy()
        while connects:
            rand = random.randint(0, len(connects))
            res, new_path = dfs(path, connects[rand], target)
            if res:
                return True, new_path
            connects.pop(rand)
        if path:
            path.pop()
        return False, []
    visited = set()
    res, to_target = dfs([], 0, target_node)
    visited = set()
    res, to_end = dfs([], target_node, end)
    
    assert(to_target)
    assert(to_end)
    return to_target + to_end





def get_dfs_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    assert(graph)
    end = len(graph) - 1
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    def dfs(path, index, target):
        if index in visited or (index == end and target != end):
            return False, []
        path.append(index)
        if index == target:
            return True, path.copy()
        visited.add(index)
        if index < len(graph):
            connects = graph[index][1].copy()
        else:
            connects = []
        while connects:
            res, new_path = dfs(path, connects[-1], target)
            if res:
                return True, new_path
            connects.pop()
        if path:
            path.pop()
        return False, []
    visited = set()
    res, to_target = dfs([], 0, target_node)
    visited = set()
    res, to_end = dfs([], target_node, end)
    assert(to_target)
    assert(to_end)
    for i in range(len(to_target) - 1):
        assert(to_target[i + 1] in graph[to_target[i]][1])
    for i in range(len(to_end) - 1):
        assert(to_end[i + 1] in graph[to_end[i]][1])
    return to_target + to_end


def get_bfs_path():
    graph = graph_data.graph_data[global_game_data.current_graph_index]
    assert(graph)
    end = len(graph) - 1
    target_node = global_game_data.target_node[global_game_data.current_graph_index]
    def bfs(path, index, target):
        connects = deque()
        connects.append([graph[index][1][0]])
        while connects:
            curr_node = connects.popleft()
            print(curr_node)
            if curr_node[-1] in visited:
                continue
            if curr_node[-1] == target:
                return True, curr_node
            else:
                visited.add(curr_node[-1])
                for neighbor in graph[curr_node[-1]][1]:
                    connects.append(curr_node.copy() + [neighbor])
        return False, []
    visited = set()
    res, to_target = bfs([], 0, target_node)
    visited = set()
    res, to_end = bfs([], target_node, end)
    
    assert(to_target)
    assert(to_end)
    for i in range(len(to_target) - 1):
        assert(to_target[i + 1] in graph[to_target[i]][1])
    for i in range(len(to_end) - 1):
        assert(to_end[i + 1] in graph[to_end[i]][1])
    return to_target + to_end


def get_dijkstra_path():
    return [1,2]
