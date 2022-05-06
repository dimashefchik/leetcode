# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for x in nums:
            valid = target - x
            if valid in nums[nums.index(x)+1:]:
                result.append(nums.index(x))
                result.append(nums.index(valid,nums.index(x)+1))
                break
        return result
