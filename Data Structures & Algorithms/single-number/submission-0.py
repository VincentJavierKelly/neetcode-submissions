class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = set()
        res = 0
        
        for n in nums:
            if n in hashset:
                hashset.remove(n)
            
            else: hashset.add(n)

        return hashset.pop()