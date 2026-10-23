class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        output = []
        i=0
        while i<len(s):
            num = []
            j=i
            while s[j] != "#":
                num.append(s[j])
                j+=1
            length = int("".join(num))
            output.append(s[i+len(num)+1 : i+len(num)+1+length])
            i += (len(num) + 1 + length) #skip num + skip "#" + skip word

        return output

