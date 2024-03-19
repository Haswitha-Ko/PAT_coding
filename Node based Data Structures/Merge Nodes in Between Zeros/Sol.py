# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''temp1=head
        temp2=head.next
        while temp2.val!=0:
            temp1.val=temp1.val+temp2.val
            temp2.next=temp2.next.next
        return temp1.val'''
        d=ListNode()
        d.next=head
        cur=d
        while cur.next:
            prev=cur
            if cur.next.val==0:
                cur=cur.next
            if cur.next:
                cur.val+=cur.next.val
                cur.next=cur.next.next
        prev.next=None
        return head
