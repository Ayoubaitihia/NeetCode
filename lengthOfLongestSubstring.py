# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:

#         i = 0
#         j = 1
#         max_sequence = 1

#         sub = ""

#         while (i < j) and (j < len(s) - 1):

#             if not sub:
#                 sub = s[i]

#             if s[j] not in sub:
#                 sub += s[j]
#                 print(f"sub: {sub}")
#                 j += 1
#                 if len(sub) > max_sequence:
#                     max_sequence = len(sub)
#             else:
#                 i += 1
#                 j = i + 1
#                 sub = ""

#         return max_sequence


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:

#         sub = ""
#         max_lenght = 1

#         length = 0

#         for c in s:

#             if c not in sub:
#                 sub += c
#             else:
#                 index = sub.find(c)
#                 length = len(sub)
#                 print("sub:", sub)
#                 sub = sub[index+1:]
#                 sub += c
#                 if length > max_lenght:
#                     max_lenght = length

#         return max_lenght


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_lenght = 1

        left = 0

        leng = 0

        seen = set()

        for right in range(len(s)):

            print("right:", s[right])

            if s[right] not in seen:
                seen.add(s[right])
                leng = right - left + 1
            else:
                while s[right] in seen:
                    seen.remove(s[left])
                    left += 1
                seen.add(s[right])
                leng = right - left + 1

            if leng > max_lenght:
                max_lenght = leng

        return max_lenght


s = "zxyzxyz"


sol = Solution()
print(sol.lengthOfLongestSubstring(s))



# s = "wp"

# index = s.find('p')

# print(s[2:])

# s += "a"

# print(s)

