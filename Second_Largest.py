class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        max_1=-1
        max_2=-1
        
        for i,x in enumerate(arr):
            if x>max_1:
                max_1 = x
        
        for k in range(0,len(arr)):
            if arr[k] > max_2 and arr[k] != max_1:
                max_2 = arr[k]
        
        return max_2
