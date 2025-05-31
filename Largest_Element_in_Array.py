class Solution:
    def largest(self, arr):
        # code here
        max=0
        for i in arr:
            if i > max:
                max = i
        return max
