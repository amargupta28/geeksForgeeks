# Remove Duplicates Sorted Array
# Difficulty: EasyAccuracy: 38.18%Submissions: 291K+Points: 2Average Time: 20m
# Given a sorted array arr. Return the size of the modified array which contains only distinct elements.
# Note:
# 1. Don't use set or HashMap to solve the problem.
# 2. You must return the modified array size only where distinct elements are present and modify the original array such that all the distinct elements come at the beginning of the original array.


class Solution:
    def removeDuplicates(self, arr):
        #Code Here
        i=1
        j=1
        
        while j<len(arr):
                
            if arr[j] != arr[j-1] :
                arr[i]=arr[j]
                i+=1
            j+=1
            
        return i
