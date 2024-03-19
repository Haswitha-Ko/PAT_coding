# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h1=odd=ListNode(0)
        h2=even=ListNode(0)
        temp=head
        i=0
        while temp:
            if i%2==0:
                even.next=temp
                even=even.next
            else:
                odd.next=temp
                odd=odd.next
            temp=temp.next
            i+=1
        odd.next=None
        even.next=h1.next
        return h2.next
