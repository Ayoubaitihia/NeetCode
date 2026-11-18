class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hashMap = {}

        for i, num in enumerate(nums):

            missing = target - num

            if missing in hashMap.keys():
                return [i, hashMap[missing]]
            else:
                hashMap[num] = i



nums = [3,4,5,6]
target = 7


sol = Solution()
print(sol.twoSum(nums, target))
