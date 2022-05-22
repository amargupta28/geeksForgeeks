
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        count=0
        maxi=arr[0]
        for i in arr:
            count+=i
            maxi=max(count,maxi)
            if count <0:
                count=0
        return maxi
            
            
