class Solution:
    def getAlternates(self, arr):
        # Code Here
        new=[]
        for i in range(0,len(arr),2):
            new.append(arr[i])
        return new
