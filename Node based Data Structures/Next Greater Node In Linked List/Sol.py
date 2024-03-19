# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        pos=-1
        s,ans=[],[]
        while head:
            pos+=1
            ans.append(0)
            while s and s[-1][1]<head.val:
                i,v=s.pop()
                ans[i]=head.val
            s.append((pos,head.val))
            head=head.next
        return ans
