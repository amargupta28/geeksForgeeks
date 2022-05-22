
class Solution:
    def sort012(self,arr,n):
        # code here
        i=0
        mid=0
        last=len(arr)-1
        while mid <= last:
            if arr[mid] == 0:
                arr[mid],arr[i] =arr[i],arr[mid]
                mid+=1
                i+=1
            elif arr[mid] == 2:
                arr[mid],arr[last] = arr[last],arr[mid]
                last-=1
            else:
                mid+=1
                

     
