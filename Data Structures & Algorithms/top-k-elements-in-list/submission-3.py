class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {} # num: freq

        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num] += 1
        buckets = [[] for _ in range(len(nums))]
        for num, freq in freqs.items():
            buckets[freq - 1].append(num)
        res = []
        i = len(nums) - 1
        while i >= 0 and k > 0:
            for elem in buckets[i]:
                if k == 0:
                    break
                res.append(elem)
                k -= 1
            i -= 1

        return res