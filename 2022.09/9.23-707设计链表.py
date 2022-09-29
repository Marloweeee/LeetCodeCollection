class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):

        self.size=0
        self.head=ListNode(0)


    def get(self, index: int) -> int:

        if  index<0 or index>=self.size:
            return -1
        tmp=self.head
        for i in range(index+1):
            tmp=tmp.next
        return tmp.val


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)


    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)




    def addAtIndex(self, index: int, val: int) -> None:
        if index>self.size:
            return

        index=max(0,index)
        insert_node,tmp=ListNode(val),self.head
        for i in range(index):
            tmp=tmp.next
        insert_node.next=tmp.next
        tmp.next=insert_node
        self.size+=1


    def deleteAtIndex(self, index: int) -> None:
        if index>=0 and index<self.size:
            tmp=self.head
            for i in range(index):
                tmp=tmp.next
            delete_node=tmp.next
            tmp.next=delete_node.next
            self.size-=1




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)