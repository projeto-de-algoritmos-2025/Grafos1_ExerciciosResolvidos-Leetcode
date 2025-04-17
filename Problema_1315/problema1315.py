# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node, parent, grandparent):
            if not node:
                return 0

            total = 0

            # Se o avô existe e é par, soma o valor do nó atual
            if grandparent and grandparent.val % 2 == 0:
                total += node.val

            # Chamada recursiva para os filhos, atualizando pai e avô
            total += dfs(node.left, node, parent)
            total += dfs(node.right, node, parent)

            return total

        return dfs(root, None, None)