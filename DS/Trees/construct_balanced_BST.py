'''
construct_tree(): Given a sorted (increasing order) array with unique integer elements, algorithm to create a binary search tree with minimal height.
ShowTree(): Prints nodes level by level.
'''

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class MinimalBST:

    def __init__(self):
        self.root = None

    def construct_tree(self, sorted_values, start, end):
        if(start>end):
            return None
        else:
            mid = int((start+end)/2)
            n = Node(sorted_values[mid])
            n.left = self.construct_tree(sorted_values, start, mid-1)
            n.right = self.construct_tree(sorted_values, mid+1, end)
            self.root = n
            return n

    #Level wise printing nodes
    def show_tree(self):
        node_list = []
        self.get_nodes_by_level(self.root, node_list, 0)
        height = len(node_list)
        for i in range(height):
            print("Nodes at level {} are:".format(i))
            for value in node_list[i]:
                print(value),
            print

    #Level wise storing nodes
    def get_nodes_by_level(self, temp, node_list, depth):
        if(temp != None):
            if(len(node_list) == depth):
                new_list = []
                new_list.append(temp.val)
                node_list.append(new_list)
                self.get_nodes_by_level(temp.left, node_list, depth+1)
                self.get_nodes_by_level(temp.right, node_list, depth+1)
            else:
                node_list[depth].append(temp.val)
                self.get_nodes_by_level(temp.left, node_list, depth+1)
                self.get_nodes_by_level(temp.right, node_list, depth+1)
                
def main():
    tree = MinimalBST()
    tree.construct_tree([1,2,3,4,5], 0, 4)
    tree.show_tree()

if __name__ == '__main__':
    main()