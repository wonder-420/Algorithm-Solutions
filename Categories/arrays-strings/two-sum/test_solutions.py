#!/usr/bin/env python3
import unittest
import importlib.util
import sys
import os

class TestSolutions(unittest.TestCase):
    
    def test_two_sum(self):
        # Dynamically import and test solutions
        spec = importlib.util.spec_from_file_location(
            "two_sum", 
            "categories/arrays-strings/two-sum/solution.py"
        )
        two_sum_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(two_sum_module)
        
        # Test cases
        test_cases = [
            ([2, 7, 11, 15], 9, [0, 1]),
            ([3, 2, 4], 6, [1, 2]),
            ([3, 3], 6, [0, 1])
        ]
        
        for nums, target, expected in test_cases:
            with self.subTest(nums=nums, target=target):
                result = two_sum_module.Solution().twoSum(nums, target)
                self.assertEqual(sorted(result), sorted(expected))

if __name__ == "__main__":
    unittest.main()
