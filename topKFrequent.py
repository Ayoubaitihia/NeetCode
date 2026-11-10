class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashMap = {}

        for num in nums:

            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        result = []

        for h in hashMap:

            if hashMap[h] >= k:
                result.append(h)

        return result


print(result)
