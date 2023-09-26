class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        for char in t:
            if char in char_count and char_count[char] > 0:
                char_count[char] -= 1
            else:
                return char

        return ''  #Adarsh
        