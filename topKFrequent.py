# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

nums = [5, 2, 2, 5, 3, 3, 4]
k = 2

hashMap = {}

for num in nums:

    if num in hashMap:
        hashMap[num] += 1
    else:
        hashMap[num] = 1

result = []

sor_hashmap = dict(sorted(hashMap.items(), key=lambda item: item[1]))

print(sor_hashmap)

        # for h in hashMap:

        #     if hashMap[h] >= k:
        #         result.append(h)

        # return result


# print(result)
