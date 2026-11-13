
class Solution:

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        hashMap = {}
        result = []

        for s in strs:

            key = ''.join(sorted(s))

            if key not in hashMap:
                hashMap[key] = [] 

            hashMap[key].append(s)

        for h in hashMap.values():
            result.append(h)

        return result



strs = ["act","pots","tops","cat","stop","hat"]


sol = Solution()

print(sol.groupAnagrams(strs))
