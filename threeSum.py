
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()

        cache = set()

        result = []

        for k, fixed in enumerate(nums):

            tripllet = []

            left = k + 1
            right = len(nums) - 1

            while left < right:

                sum = fixed + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    tripllet.append(fixed)
                    tripllet.append(nums[right])
                    tripllet.append(nums[left])

                    cache.add(tuple(tripllet))
                    right -= 1
                    left += 1

                tripllet = []

        for item in cache:
            result.append(list(item))

        return result


sol = Solution()

print(sol.threeSum([]))

