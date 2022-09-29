

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={')':'(',']':'[','}':'{'}

        for item in s:
            if stack and item in dic:
                if stack[-1]==dic[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)

        return not stack

if __name__ == '__main__':
    s = "()"
    print(Solution().isValid(s))
