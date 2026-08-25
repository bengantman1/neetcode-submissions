class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        deque = [] # holds indices of window
        print(deque)
        for r in range(len(nums)):
            # idx of largest number in window always at deque[0]
            
            # remove first entry if idx is outside of window
            if deque and deque[0] <= r - k:
                deque.pop(0)
            # replace all indices in deque for nums that are less than nums[r]
            i = len(deque) - 1
            while deque and nums[r] > nums[deque[i]] and i >= 0:
                deque.pop()
                i -= 1
            deque.append(r)
            if r >= k - 1:
                res.append(nums[deque[0]])

        return res
            
            