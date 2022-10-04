class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack=[]
        for letter in s:
            if letter=='(':
                stack.append(letter)
            elif stack!=[] and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(letter)
        return len(stack)

if __name__ == '__main__':
    s = "))()"
    print(Solution().minAddToMakeValid(s))