class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictt = {}
        for word in strs:
            alphabetVector = [0] * 26
            for char in word:
                alphabetVector[ord(char) - ord('a')]+=1
            if tuple(alphabetVector) in dictt:
                dictt[tuple(alphabetVector)].append(word)
            else:
                dictt[tuple(alphabetVector)] = [word]
        return dictt.values()



