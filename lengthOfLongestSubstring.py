class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        i = 0
        j = 1
        max_sequence = 1

        sub = ""

        while (i < j) and (j < len(s) - 1):

            if not sub:
                sub = s[i]

            if s[j] not in sub:
                sub += s[j]
                print(f"sub: {sub}")
                j += 1
                if len(sub) > max_sequence:
                    max_sequence = len(sub)
            else:
                i += 1
                j = i + 1
                sub = ""

        return max_sequence



s = "xxxx"


sol = Solution()
print(sol.lengthOfLongestSubstring(s))
