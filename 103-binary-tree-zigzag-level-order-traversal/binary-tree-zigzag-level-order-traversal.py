# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty, return an empty list
        if not root:
            return []

        result = []  # Final result list to hold each level's node values
        queue = deque([root])  # Queue for BFS traversal starting with root node
        left_to_right = True   # Flag to control zigzag direction
        

        # Perform level-order traversal (BFS)
        while queue:
            level_size = len(queue)    # Number of nodes at current level
            # Deque to hold node values for this level in the correct order
            current_level = deque()   
            

            # Process all nodes at the current level
            for _ in range(level_size):
                # Get the next node from the queue
                node = queue.popleft()

                # Add node value to current level list:
                # - from left if direction is left_to_right
                # - from right if direction is right_to_left
                if left_to_right:
                    current_level.append(node.val)
                else:
                    current_level.appendleft(node.val)

                # Add the child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Append the current level's result to the final result list
            result.append(list(current_level))

            # Flip the direction for the next level
            left_to_right = not left_to_right

        return result