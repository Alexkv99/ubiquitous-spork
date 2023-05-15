class ReachableTestCase(unittest.TestCase):
    def test_reachable_nodes_case1(self):
        # Test case 1
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        start_node = 3
        expected_output = {3, 4}
        actual_output = reachable(adj_list, start_node)
        self.assertEqual(actual_output, expected_output)

    def test_reachable_nodes_case2(self):
        # Test case 2
        adj_list = [[1, 2], [3], [4], [0], []]
        start_node = 0
        expected_output = {0, 1, 2, 3, 4}
        actual_output = reachable(adj_list, start_node)
        self.assertEqual(actual_output, expected_output)

    def test_reachable_nodes_case3(self):
        # Test case 3
        adj_list = [[1], [2, 3], [0], [], []]
        start_node = 4
        expected_output = {4}
        actual_output = reachable(adj_list, start_node)
        self.assertEqual(actual_output, expected_output)

    def test_reachable_nodes_case4(self):
        # Test case 4
        adj_list = [[1, 2], [3], [], [0, 4], []]
        start_node = 1
        expected_output = {1, 2, 3, 0, 4}
        actual_output = reachable(adj_list, start_node)
        self.assertEqual(actual_output, expected_output)

    # Add more test cases for different scenarios

if __name__ == '__main__':
    unittest.main()
