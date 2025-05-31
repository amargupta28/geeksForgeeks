
class Solution:
    def MissingNumber(self,array,n):
        # code here'
        return sum([i for i in range(1,n+1)]) -sum(array)