class Solution:
    def findRollOut(self, s, roll, n):
        # Your code goes here
        maxChar=26
        brr= {i:0 for i in range(n+1)}
        temp=""
        ch = [ 'a', 'b', 'c', 'd', 'e','f','g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x',
'y', 'z' ];

        # print(brr)
        for i in range(n):
            brr[0]+=1
            brr[roll[i]] -= 1
        for i in range(1,n):
            brr[i] += brr[i - 1]
        # print(brr)
        
        for i in range(n):
            x= brr[i]%maxChar
            y=ord(s[i]) - ord('a')
            temp+= ch[(x+y)%maxChar]
        return temp
        
