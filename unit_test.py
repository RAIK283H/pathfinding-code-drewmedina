import math
import unittest
import global_game_data
import graph_data
from pathing import get_bfs_path, get_dfs_path, get_dijkstra_path
import permutation
import f_w

class TestPathFinding(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('Test'.isupper())

    def test_floating_point_estimation(self):
        first_value = 0
        for x in range(1000):
            first_value += 1/100
        second_value = 10
        almost_pi = 3.1
        pi = math.pi
        self.assertNotEqual(first_value,second_value)
        self.assertAlmostEqual(first=first_value,second=second_value,delta=1e-9)
        self.assertNotEqual(almost_pi, pi)
        self.assertAlmostEqual(first=almost_pi, second=pi, delta=1e-1)

    def test_bfs_path_working(self):
        idx = 1
        target = 6

        global_game_data.current_graph_index = idx
        global_game_data.target_node = {idx: target}
        graph_data.graph_data = {
            idx: [
                (0, [2, 3]),
                (1, [4]),
                (2, [4, 5]),
                (3, [6]),
                (4, [6]),
                (5, [7, 8]),
                (6, [9]),
                (7, [9]),
                (8, [10]),
                (9, [])
            ]
        }
        expected_bfs_path = [2, 4, 6, 9]
        bfs_path_result = get_bfs_path()
        self.assertEqual(bfs_path_result, expected_bfs_path)

    def test_bfs_failing(self):
        idx = 1
        target = 6

        global_game_data.current_graph_index = idx
        global_game_data.target_node = {idx: target}
        graph_data.graph_data = {
            idx: [
                (0, [2, 3]),
                (1, [4]),
                (2, [4, 5]),
                (3, []),
                (4, []),
                (5, []),
                (6, [9]),
                (7, [9]),
                (8, [10]),
                (9, [])
            ]
        }
        try:
            get_bfs_path()
        except AssertionError:
            return
        self.fail("No error")

    def test_dfs_path(self):
        idx = 1
        target = 8

        global_game_data.current_graph_index = idx
        global_game_data.target_node = {idx: target}
        graph_data.graph_data = {
            idx: [
                (0, [2, 3]),
                (1, [4]),
                (2, [4, 5]),
                (3, [6]),
                (4, [6]),
                (5, [7, 8]),
                (6, [9]),
                (7, [9]),
                (8, [10, 9]),
                (9, [])
            ]
        }
        expected_dfs_path = [0, 2, 5, 8, 8, 9]
        dfs_path_result = get_dfs_path()
        self.assertEqual(dfs_path_result, expected_dfs_path)

    def test_dfs_failing(self):
        idx = 1
        target = 6

        global_game_data.current_graph_index = idx
        global_game_data.target_node = {idx: target}
        graph_data.graph_data = {
            idx: [
                (0, [2, 3]),
                (1, [4]),
                (2, [4, 5]),
                (3, []),
                (4, []),
                (5, []),
                (6, [9]),
                (7, [9]),
                (8, [10]),
                (9, [])
            ]
        }
        try:
            get_dfs_path()
        except AssertionError:
            return
        self.fail("No error")
    
    def test_sjt(self):
        graph = [[(0, 0), [1,2]], 
                 [(0, 1), [0, 3]],
                 [(1, 1), [0, 3]],
                 [(1, 0), [1, 2]]]
        actual = permutation.sjt(graph)
        expected = [[0, 1, 2, 3], [0, 1, 3, 2], [0, 3, 1, 2], [3, 0, 1, 2], 
                    [3, 0, 2, 1], [0, 3, 2, 1], [0, 2, 3, 1], [0, 2, 1, 3], [2, 0, 1, 3], [2, 0, 3, 1],
                      [2, 3, 0, 1], [3, 2, 0, 1], [3, 2, 1, 0], [2, 3, 1, 0], [2, 1, 3, 0], [2, 1, 0, 3], 
                      [1, 2, 0, 3], [1, 2, 3, 0], [1, 3, 2, 0], [3, 1, 2, 0], [3, 1, 0, 2], [1, 3, 0, 2], 
                      [1, 0, 3, 2], [1, 0, 2, 3]]
        self.assertEqual(actual, expected)
    def test_hamiltonian(self):
        graph = [[(0, 0), [1,2]], 
                 [(0, 1), [0, 3]],
                 [(1, 1), [0, 3]],
                 [(1, 0), [1, 2]]]
        actual = permutation.check_hamiltonian(graph, permutation.sjt(graph))
        expected =[[0, 1, 3, 2, 0], [0, 2, 3, 1, 0], [2, 0, 1, 3, 2], [3, 2, 0, 1, 3], [2, 3, 1, 0, 2], [1, 3, 2, 0, 1], [3, 1, 0, 2, 3], [1, 0, 2, 3, 1]]
        self.assertEqual(actual, expected)
    def test_optimals(self):
        graph = [[(0, 0), [1,2]], 
                 [(0, 1), [0, 3]],
                 [(1, 1), [0, 3]],
                 [(1, 0), [1, 2]]]
        actual = permutation.optimal_cycles(graph, permutation.sjt(graph))
        expected = [[0, 1, 3, 2, 0], [[0, 2, 3, 1, 0]], [[2, 0, 1, 3, 2]], [[3, 2, 0, 1, 3]], [[2, 3, 1, 0, 2]], [[1, 3, 2, 0, 1]], [[3, 1, 0, 2, 3]], [[1, 0, 2, 3, 1]]]   
        self.assertEqual(actual, expected)
    def test_largest_clique(self):
        graph = [[(0, 0), [1,2]], 
                 [(0, 1), [0, 2]],
                 [(1, 1), [0, 1]],
                 [(1, 0), [1, 2]]]
        actual = permutation.get_largest_clique(graph)
        expected = [1, 2]   
        self.assertEqual(actual, expected)
    def test_get_dijkstra_path(self):
        idx = 0
        target = 2

        global_game_data.current_graph_index = idx
        global_game_data.target_node = {idx: target}
        graph_data.graph_data = [
                [[(0, 0), [1, 2]], [(1, 1), [0, 3]], [(2, 2), [0, 3]], [(3, 3), [1, 2]]]
            ]
        
        path = get_dijkstra_path() 
        self.assertIsNotNone(path) 
        self.assertTrue(len(path) > 0) 
        self.assertEqual(path, [0, 2, 3])
    def test_get_dijkstra_path_fail(self):
        idx = 0
        target = 2

        global_game_data.current_graph_index = idx
        global_game_data.target_node = {idx: target}
        graph_data.graph_data = [ [[(0, 0), [1]],
                                 [(1, 1), [0]], 
                                 [(2, 2), [3]], 
                                 [(3, 3), [2]] ]]
        
        path = get_dijkstra_path() 
        self.assertEqual(path, None)

    def test_f_w_small_matrix(self):
        graph = [
            [(0, 0), [1]],
            [(1, 0), [0, 2]],
            [(2, 0), [1, 3]],
            [(3, 0), [2]]
        ]
        path = [0, 1, 2, 3]
        f_w_path = f_w.find_optimal_path(graph, 0)
        assert path == f_w_path, "F_W Small Matrix Failed"

    def test_f_w_large_matrix(self):
        graph = [
            [(0, 0), [1, 2]],
            [(1, 1), [0, 3, 4]],
            [(2, 0), [0, 4]],
            [(1, -1), [1, 5]],
            [(3, 0), [1, 2, 5, 6]],
            [(2, -2), [3, 4, 6]],
            [(4, 0), [4, 5, 7]],
            [(5, 0), [6]]
        ]
        path = [0, 2, 4, 6, 7]
        f_w_path = f_w.find_optimal_path(graph, 0)
        assert path == f_w_path, "F_W Large Matrix Failed"

    def test_f_w_fail(self):
        graph = [
            [(0, 30), [1, 2]],
            [(231, 50), [0]],
            [(220, 1), [0]],
            [(12340, 10), [4]], 
            [(11, 1000), [3]], 
            [(20, 20), []], 
            [(155, 30), [0]], 
            [(351, 100), [0]]
        ]
        path = [0]
        graph_matrix = f_w.convert_graph_to_matrix(graph)
        _, P = f_w.compute_shortest_paths(graph_matrix)
        f_w_path = f_w.build_path(P, 0, 6)
        print("HELLO", path, f_w_path)
        assert path == f_w_path[:-1], "F_W fail test did not fail" 

if __name__ == '__main__':
    unittest.main()
