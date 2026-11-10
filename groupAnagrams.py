
class Solution:

    def isAnagrams(self, s: str, t: str):
        # if not s:
        #     return False

        return sorted(s) == sorted(t)

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        i = 0
        checked = []
        result = []

        for i in range(len(strs)):
            sublists = []

            if strs[i] in checked:
                continue

            sublists.append(strs[i])

            for j in range(i+1, len(strs)):
                if self.isAnagrams(strs[i], strs[j]):
                    sublists.append(strs[j])
                    checked.append(strs[j])

            result.append(sublists)

        return result


# strs = ["act","pots","tops","cat","stop","hat"]

# strs = ["", "", ""]


strs = ["", ""]

sol = Solution()

# print(sol.isAnagrams("", ""))

print(sol.groupAnagrams(strs))
