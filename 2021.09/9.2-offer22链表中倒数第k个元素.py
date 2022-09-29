# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        linknode=head
        n=0
        while(linknode):
            n+=1
            linknode=linknode.next
        while(n>k):
            n-=1
            head=head.next
        return head

if __name__ == '__main__':
    num=[1,2,3,4,5]
    k=2
    head=ListNode(num[0])
    rear=head
    for i,item in enumerate(num[1:]):
        new_node=ListNode(item)
        rear.next=new_node
        rear=rear.next

    s=Solution()
    head=(s.getKthFromEnd(head, k))
    while(head):
        print(head.val,end=" ")
        head=head.next

