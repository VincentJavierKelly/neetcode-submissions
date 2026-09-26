class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count how many times each number appears
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Pair each number with its count as [count, number]
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])

        # Sort from lowest count to highest count
        arr.sort()

        # Pop the k largest counts from the back of the list
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res

        