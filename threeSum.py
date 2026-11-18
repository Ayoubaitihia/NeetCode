
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        result = []

        nums.sort()

        for i, num in enumerate(nums):

            left = i + 1
            right = len(nums) - 1

            while left < right:

                if num == nums[left] == nums[right]:
                    left += 1
                    continue

                sum = num + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1

        return result



sol = Solution()

print(sol.threeSum([-1,0,1,2,-1,-4]))
