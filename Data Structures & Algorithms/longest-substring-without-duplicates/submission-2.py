class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # window +1, if new in old, chop right till not, update len

        longest = 0
        size = 0
        head = 0
        while head + size < len(s)-1:
            size += 1
            if s[head+size] not in s[head:head+size]:
                longest = max(longest, size)
            else:
                while s[head+size] in s[head:head+size]:
                    head += 1
                    size -= 1

        if s and s[-1] not in s[head:head+size]:
            longest += 1

        return longest
            
            