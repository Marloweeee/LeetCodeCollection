
from typing import Optional,List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        sum_sub,start_flag,nums=0,True,set(nums)
        while head:
            if head.val in nums and start_flag:
                sum_sub+=1
                start_flag=False
                head=head.next
            elif head.val in nums:
                head=head.next
            else:
                start_flag=True
                head=head.next

        return sum_sub
if __name__ == '__main__':
    head = [0, 1, 2, 3, 4]
    nums = [0, 3, 1, 4]
    print(Solution().numComponents(head,nums))