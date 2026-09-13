class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for char in s:
            if char.isalnum(): new_s+=char.lower()
        for i in range(int(len(new_s)/2)):
            if(new_s[i] == new_s[len(new_s)-i-1]): continue
            else:
                return False
        return True

