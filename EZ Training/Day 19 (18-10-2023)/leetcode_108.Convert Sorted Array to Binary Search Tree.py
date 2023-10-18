# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def fun(si,li):
            if si<=li:
                mid=(si+li)//2
                root=TreeNode(nums[mid])
                root.left=fun(si,mid-1)
                root.right=fun(mid+1,li)
                return root
        return fun(0,len(nums)-1)
