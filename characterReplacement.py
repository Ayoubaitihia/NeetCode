class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0

        max_freq = 0

        hashMap = {}

        for right in range(len(s)):

            if s[right] in hashMap:
                hashMap[s[right]] += 1
            else:
                hashMap[s[right]] = 1

            if hashMap[s[right]] > max_freq:
                max_freq = hashMap[s[right]]

            l = right - left + 1 

        return hashMap



s = "AAABABB"
k = 1

sol = Solution()

print(sol.characterReplacement(s, k))
