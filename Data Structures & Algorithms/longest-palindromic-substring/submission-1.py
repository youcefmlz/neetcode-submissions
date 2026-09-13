class Solution:
    def longestPalindrome(self, s: str) -> str:
        #solve it using two pointers

        longest_res = 0
        res = ""

        for i in range(len(s)):
            #odd
            left,right = i,i
            #check if it is inbound and palindrom

            while(left>=0 and right<len(s) and s[left]==s[right]):
                if longest_res < (right-left +1):
                    #if the substring that we found is greater than what we have before we update
                    longest_res = (right-left +1)
                    res = s[left:right+1]
                #update our pointers
                left-=1
                right+=1
            
            #even
            even_left , even_right = i,i+1
            #check if pointers are inbound and if their characters are eq
            while(even_left>=0 and even_right<len(s) and s[even_left] == s[even_right]):

                if(even_right - even_left+1 )> longest_res:
                    #if the substring that we found is greater than what we have before we update
                    longest_res = (even_right - even_left+1)
                    res = s[even_left:even_right+1]
                #update our pointers
                even_left-=1
                even_right+=1
        
        return res
