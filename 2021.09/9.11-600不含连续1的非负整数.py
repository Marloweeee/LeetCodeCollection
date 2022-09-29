class Solution:
    def findIntegers(self, n: int) -> int:
        for i in range(n,0,-1):
            item=bin(i)[2:]
            length,idx=len(item),0
            flag=True
            

if __name__ == '__main__':
    n=5
    print(Solution().findIntegers(n))