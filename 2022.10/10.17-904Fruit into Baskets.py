from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        left,right=0,len(fruits)
        max_len=0
        for left in range(len(fruits)):

            curr=set(fruits[left:right])

            while len(curr)>2:
                right-=1
                curr = set(fruits[left:right])

            max_len=max(max_len,len(fruits[left:right]))
            if right==left:
                break
            right=len(fruits)


        return max_len

if __name__ == '__main__':
    print(Solution().totalFruit([0,1,2,2]))


