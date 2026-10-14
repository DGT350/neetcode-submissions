class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # n = number of elements, res = len(nums),0 - stores the longest sequence
        n, res = len(nums), 0
        # for loop that traverse through the array
        for i in range(n):
            #counter to keep track of consecutive 1s
            cnt = 0 
            #for loop that starts at index i, counts consective 1s from that position 
            for j in range(i,n):
                #if a number found that is not 1 then break the count 
                if nums[j] == 0: break 
                #updates the count after broken 
                cnt += 1 
                #chooses the maximum count 
                res = max(res,cnt)
        
        return res    

    