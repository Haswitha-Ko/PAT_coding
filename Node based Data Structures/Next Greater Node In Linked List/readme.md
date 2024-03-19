# Next Greater Node In Linked List

You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

 

### Example 1:
![linkedlistnext1](https://github.com/Haswitha-Ko/PAT_coding/assets/119152181/1e0af1e0-a6bb-4270-be22-45b9a5d5af3c)

```
Input: head = [2,1,5]
Output: [5,5,0]
```
### Example 2:
![linkedlistnext2](https://github.com/Haswitha-Ko/PAT_coding/assets/119152181/ebe58f5a-c244-4b6b-a491-720034164a10)

```
Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]
```

**Constraints**:

The number of nodes in the list is n.
1 <= n <= 104
1 <= Node.val <= 109
