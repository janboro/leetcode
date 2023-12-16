"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.
 
Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""

from time import perf_counter


class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers_map: dict[int, int] = {}
        for i in range(len(nums)):
            searched: int = target - nums[i]
            if searched in numbers_map:
                return [numbers_map[searched], i]
            numbers_map[nums[i]] = i
        return []

start = perf_counter()
result = Solution().twoSum(nums=[2, 7, 11, 15], target=9)
stop = perf_counter()
print(f"Result: {result} | Time: {stop - start}")
