

class Solution:
    def factorial (self, N):
        # code here
        temp=1
        for i in range(1,N+1):
            temp*=i
        return temp
