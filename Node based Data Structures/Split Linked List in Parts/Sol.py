# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length=0
        temp=head
        while temp:
            length=length+1
            temp=temp.next
        width,r=divmod(length,k)
        result,current=[],head
        for i in range(k):
            dummy=write=ListNode(0)
            for i in range(width+(i<r)):
                if current:
                    write.next=write=ListNode(current.val)
                    current=current.next
            result.append(dummy.next)
        return result
