# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum=0
        unit_pos1=1
        unit_pos2=1
        while(l1!=None):
            sum+=l1.val*unit_pos1
            unit_pos1*=10
            l1=l1.next
        while(l2!=None):
            sum+=l2.val*unit_pos2
            unit_pos2*=10
            l2=l2.next
        res=list(map(int,str(sum)))[::-1]
        print(res)
        res_list=ListNode(res[0])
        p=res_list
        for index in range(1,len(res)):
            temp_node=ListNode(res[index])
            p.next=temp_node
            p=temp_node
        return res_list

if __name__ == '__main__':
    l1=ListNode(val=825)
    l2=ListNode(val=156)
    s=Solution()
    a=s.addTwoNumbers(l1,l2)
    while(a!=None):
        print(a.val)
        a=a.next