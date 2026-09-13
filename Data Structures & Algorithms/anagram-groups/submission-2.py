class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for word in strs:
            alphabetoccurence = [0]*26
            for c in word:
                alphabetoccurence[ord(c)-ord('a')]+=1
            hash_map[tuple(alphabetoccurence)].append(word)
        return hash_map.values()



