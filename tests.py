#!/usr/bin/env python3

import unittest

from astar import *


class TestMazes(unittest.TestCase):
    def test_maze_1(self):
        """
        This is the maze:
        21 22 23 24 25
        16 17 18 19 20
        11 12 13 14 15
        6  7  8  9  10
        1  2  3  4  5
        Start: 1
        Goal: 25
        """
        ss = StarSolver()
        ss.read_maze_file('input_1.json')
        self.assertEqual(
            ss.solve_the_maze(ss.start_node, ss.goal_node),
            '1 -> 7 -> 13 -> 19 -> 25')

    def test_maze_2(self):
        """
        This is the maze:
        21 22 23 24 25
        16 17 18 19 20
        11          15
        6  7  8  9  10
        1  2  3  4  5
        Start: 1
        Goal: 25
        """
        ss = StarSolver()
        ss.read_maze_file('input_2.json')
        expected_output = [
            '1 -> 7 -> 8 -> 9 -> 15 -> 20 -> 25',
            '1 -> 6 -> 11 -> 17 -> 23 -> 24 -> 25'
        ]
        actual_output = ss.solve_the_maze(ss.start_node, ss.goal_node)
        self.assertTrue(actual_output in expected_output)

    def test_maze_3(self):
        """
        This is the maze:
        11 12 13 14 15
        6  7  8  9  10
        1  2  3  4  5
        Start: 1
        Goal: 9
        """
        ss = StarSolver()
        ss.read_maze_file('input_3.json')
        self.assertEqual(
            ss.solve_the_maze(ss.start_node, ss.goal_node), '1 -> 2 -> 8 -> 9')

    def test_maze_4(self):
        """
        This is the maze:
        21 22 23 24 25
        16 17 18 19 20
        11 12       15
        6  7  8  9  10
        1  2  3  4  5
        Start: 1
        Goal: 25
        """
        ss = StarSolver()
        ss.read_maze_file('input_4.json')
        expected_outputs = [
            '1 -> 7 -> 12 -> 18 -> 24 -> 25',
            '1 -> 7 -> 12 -> 18 -> 19 -> 25',
            '1 -> 6 -> 12 -> 18 -> 24 -> 25',
            '1 -> 6 -> 12 -> 18 -> 19 -> 25'
        ]
        self.assertTrue(
            ss.solve_the_maze(ss.start_node, ss.goal_node) in expected_outputs)


if __name__ == '__main__':
    unittest.main()
