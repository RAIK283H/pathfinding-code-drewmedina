import math
import unittest

import global_game_data
import graph_data
from pathing import get_bfs_path, get_dfs_path
import permutation

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
if __name__ == '__main__':
    unittest.main()
