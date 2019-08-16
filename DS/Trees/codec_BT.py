from collections import deque
from typing import Optional, Tuple

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def BFS(root: TreeNode):
    """
    This function is just for the testing purpose. It will print nodes in BFS fashion.

    :param root: root node of a tree
    """

    queue = deque()
    queue.append(root)
    elements = []
    while len(queue) > 0:
        ele = queue.popleft()
        elements.append(ele.val)
        if ele.left:
           queue.append(ele.left)
        if ele.right:
           queue.append(ele.right)

    print(elements)

class Codec:


    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Encodes a tree to a single string. We will save an array representation of the BT.
        
        :param root: TreeNode
        :rtype: str
        """
        
        # For storing values
        encode = []
        self._serialize_helper(root, encode)
        return ",".join(encode)

    def _serialize_helper(self, node: Optional[TreeNode], encode: list):
        """
        Helper function for serialization. We will perform pre-order traversal for storing the values.

        :param root: cuurent TreeNode
        :param encode: list with values as strings
        """

        if not node:
            encode.append("null")

        else:
            encode.append(str(node.val))
            self._serialize_helper(node.left, encode)
            self._serialize_helper(node.right, encode)


    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Decodes the encoded data to tree.
        
        :param data: str
        :rtype: TreeNode
        """
        
        # Decoding the data
        data = data.split(",")
        return self._deserialize_helper(data, 0)[0]

    def _deserialize_helper(self, data: list, pos: int) -> Tuple[Optional[TreeNode], int]:
        """
        Helper function for decoding the data. It will again follow pre-order traversal to generate the tree.

        :param data: decoded data
        :rtype: TreeNode and current position in the decoded string
        """

        # Checking if there is a node or not
        if data[pos] == "null":
            return None, pos

        else:
            node = TreeNode(int(data[pos]))
            node.left, pos = self._deserialize_helper(data, pos+1)
            node.right, pos = self._deserialize_helper(data, pos+1)
            return node, pos

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    codec = Codec()
    encode = codec.serialize(root)
    print(encode)
    root = codec.deserialize(encode)
    if root:
        BFS(root)
    else:
        print("Empty Tree")