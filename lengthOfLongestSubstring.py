class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i = 0
        j = 1
        max_sequence = 1
        count = 1

        while (i < j) and (j < len(s) - 1):

            

            if s[i] < s[j] and s[j] > s[j-1]:
                # print(f"i={i} | {s[i]}")
                # print(f"j={j} | {s[j]}")
                j += 1
                count += 1
                # print(f"count: {count}")
            else:
                i += 1
                j = i + 1
                count = 1

            if count > max_sequence:
                max_sequence = count

        return max_sequence



s = "xxxx"


sol = Solution()
print(sol.lengthOfLongestSubstring(s))
