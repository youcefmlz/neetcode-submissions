class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        words_dict = defaultdict(list)
        for word in strs:
            key= "".join(sorted(word))
            words_dict[key].append(word)
        return list(words_dict.values())




