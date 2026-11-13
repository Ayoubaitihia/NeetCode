
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        checked = []

        nums.sort()

        print("Nums:", nums)

        result = []

        for k, n in enumerate(nums):

            triplet = []

            print("k:", k)

            if k in checked:
                continue

            left = k + 1
            right = len(nums) - 1

            while right > left:

                if right in checked:
                    right -= 1
                if left in checked:
                    left += 1

                if n + nums[right] + nums[left] > 0:
                    right -= 1
                elif n + nums[right] + nums[left] < 0:
                    left += 1
                else:
                    triplet.append(n)
                    triplet.append(nums[right])
                    triplet.append(nums[left])

                    checked.append(k)
                    checked.append(right)
                    checked.append(left)
                    break

            print("Checked:", checked)
            print("Triplet:", triplet)

            if triplet:
                result.append(triplet)

        return result


sol = Solution()

print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
