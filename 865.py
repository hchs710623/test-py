
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def subtreeWithAllDeepest(self, root):

        def find_deep_tree(node):
            """
            :type node: TreeNode
            :rtype: (depth, node)
            """
            left_d = right_d = 0
            left_node = right_node = None

            if node.left != None:
                left_d, left_node = find_deep_tree(node.left)
            
            if node.right != None:
                right_d, right_node = find_deep_tree(node.right)

            if left_d == right_d:
                return (left_d + 1), node
            elif left_d > right_d:
                return (left_d + 1), left_node
            else:
                return (right_d + 1), right_node

        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        
        _, node = find_deep_tree(root)

        return node

if __name__ == "__main__":

    T3 = TreeNode(3)
    T5 = TreeNode(5)
    T1 = TreeNode(1)
    T6 = TreeNode(6)
    T2 = TreeNode(2)
    T0 = TreeNode(0)
    T8 = TreeNode(8)
    T7 = TreeNode(7)
    T4 = TreeNode(4)
    
    T3.left = T5
    T3.right = T1

    T5.left = T6
    T5.right = T2

    T1.left = T0
    T1.right = T8

    T2.left = T7
    T2.right = T4

    A = Solution()
    ans = A.subtreeWithAllDeepest(T3)

    print(ans.val)