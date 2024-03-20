# Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.

 

### Example 1:
![btree1](https://github.com/Haswitha-Ko/PAT_coding/assets/119152181/4ebb130d-4e49-44bb-b59e-f676dbb05fbb)

```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
```
**Explanation**: [0,-10,5,null,-3,null,9] is also accepted:
![btree2](https://github.com/Haswitha-Ko/PAT_coding/assets/119152181/b2d79339-23c8-4909-9186-bc3f2f0d5d5b)

### Example 2:
![btree](https://github.com/Haswitha-Ko/PAT_coding/assets/119152181/9d2fea7a-ae39-4807-95ea-e7739f06a4db)

```
Input: nums = [1,3]
Output: [3,1]
```
**Explanation**: [1,null,3] and [3,1] are both height-balanced BSTs.
 

**Constraints**:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order
