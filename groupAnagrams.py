
class Solution:

    def isAnagrams(self, s: str, t: str):
        return sorted(s) == sorted(t)

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        i = 0
        checked = []
        result = []

        while i < len(strs) - 1:

            sublists = []
            if not strs[i]:
                sublists.append(strs[i])
                i += 1
                continue


            if strs[i] not in checked:
                sublists.append(strs[i])

            j = i + 1
            while j < len(strs):
                if self.isAnagrams(strs[i], strs[j]) and (strs[i] not in checked):
                    checked.append(strs[j])
                    sublists.append(strs[j])
                j += 1
            i += 1

            if sublists:
                result.append(sublists)

        if strs[i] not in checked:
            sublists = [strs[i]]
            result.append(sublists)

        return result


strs = ["", "", ""]

sol = Solution()

print(sol.groupAnagrams(strs))
