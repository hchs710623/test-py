import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):

        def findleaflist(stack):

            result = []

            while len(stack) > 0:
                node = stack.pop()
                
                if node.left == None and node.right == None:
                    result.append(node.val)
                else:
                    if node.right != None:
                        stack.append(node.right)
                    if node.left != None:
                        stack.append(node.left)

            print(result)
            
            return result

        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        if root1 == None:
            ans1 = None
        else:
            stack1 = []
            stack1.append(root1)
            ans1 = findleaflist(stack1)

        if root2 == None:
            ans2 == None
        else:
            stack2 = []
            stack2.append(root2)
            ans2 = findleaflist(stack2)

        if ans1 == ans2:
            return True
        else:
            return False




if __name__ == "__main__":
    
    a = Solution()
