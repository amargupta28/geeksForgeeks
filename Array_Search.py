#User function Template for python3

class Solution:
    #Complete the below function
    def search(self,arr, x):
        #Your code here
        for i,y in enumerate(arr):
            if y == x:
                return i
        return -1
