class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        deque = collections.deque()

        l = r = 0

        while r < len(nums):
            while deque and nums[deque[-1]] < nums[r]:
                deque.pop()
            deque.append(r)


            if deque and l > deque[0]:
                deque.popleft()
            if  (r - l + 1) == k:
                output.append(nums[deque[0]])

                l += 1 

            r+=1

        
        return output


        





        