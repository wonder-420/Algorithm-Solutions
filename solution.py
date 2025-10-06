class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Two Sum solution using hash map
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []
