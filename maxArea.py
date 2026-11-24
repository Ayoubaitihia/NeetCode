class Solution:
    def maxArea(self, heights: list[int]) -> int:

        values = []

        left = 0
        right = len(heights) - 1

        max_value = 0

        while left < right:
            value = (right - left) * (min(heights[left], heights[right]))

            if value > max_value:
                max_value = value

            values.append(value)

            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_value


sol = Solution()

print(sol.maxArea([1,7,2,5,4,7,3,6]))
