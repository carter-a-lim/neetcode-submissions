class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # word: alphabetic word
        # if words[word] in list, list.append(word)

        d = {}
        output = []

        for word in strs:
            alphWord = "".join(sorted(word))
            if alphWord not in d:
                d[alphWord] = [word]
            else: 
                d[alphWord].append(word)

        for alphWord in d:
            output.append(d[alphWord])
        
        return output

                    