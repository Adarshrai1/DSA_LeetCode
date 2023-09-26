class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        stack_set = set()
        for char in s:
            char_count[char] -= 1
            if char in stack_set:
                continue
            while stack and char < stack[-1] and char_count[stack[-1]] > 0:
                removed_char = stack.pop()
                stack_set.remove(removed_char)
            stack.append(char)
            stack_set.add(char)
        return ''.join(stack)         #AdarshRai
