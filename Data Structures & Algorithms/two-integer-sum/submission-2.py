class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = defaultdict(int)
        for i, num in enumerate(nums): # (num, index)
            indices[num] = i
        for j, num in enumerate(nums):
            need = target - num
            if need in indices and j != indices[need]:
                return [j, indices[need]]

