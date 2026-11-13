class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        if len(nums) < 2 or len(nums) > 1000:
            return []

        hashMap = {}

        for i, num in enumerate(nums):

            if nums[i] < -10000000 or nums[i] > 10000000:
                return []

            if target < -10000000 or target > 10000000:
                return []


            missing = target - num

            if missing in hashMap.keys():
                return [i, hashMap[missing]]
            else:
                hashMap[num] = i

        return []





nums = [50,5]

target = 10


sol = Solution()

print(sol.twoSum(nums, target))
