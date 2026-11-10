# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

nums = [1, 1, 1, 2, 3, 3]
k = 2

hashMap = {}

for num in nums:

    if num in hashMap:
        hashMap[num] += 1
    else:
        hashMap[num] = 1

result = []


# sor_hashmap = dict(sorted(hashMap.items(), key=lambda item: item[1], reverse=True))

print(hashMap)

# print(sor_hashmap)

# result = list(sor_hashmap.keys())

# print(result[:k])

        # for h in hashMap:

        #     if hashMap[h] >= k:
        #         result.append(h)

        # return result


# print(result)
