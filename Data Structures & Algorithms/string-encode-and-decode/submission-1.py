class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # find the '#' that separates the length prefix from the string
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # read exactly `length` characters as the next string
            result.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return result
