class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = Counter(s)
        odd = 0#max
        even = 101#min

        for num in freqs:
            if freqs[num] % 2 == 0:
                if freqs[num] < even:
                    even = freqs[num]
            if freqs[num] % 2 == 1:
                if freqs[num] > odd:
                    odd = freqs[num]

        return odd - even
            
            

