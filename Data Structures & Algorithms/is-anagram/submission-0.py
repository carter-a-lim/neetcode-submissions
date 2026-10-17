class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def toArray(string: str) -> dict:
            d = {}
            for char in string:
                d[char] = d.get(char, 0) + 1
            return d

        d1 = toArray(s)
        d2 = toArray(t)

        if len(d1) != len(d2):
            return False

        for letter in d1:
            if d1[letter] != d2.get(letter, -1):
                return False
        return True