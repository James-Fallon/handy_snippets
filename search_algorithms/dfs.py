

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def dfs(root):

    if root:
        print(root.data)
        dfs(root.left)
        dfs(root.right)


if __name__ == '__main__':

    b = Node('B', left=Node('D'), right=Node('E'))
    c = Node('C')
    root_node = Node('A', left=b, right=c)
    dfs(root_node)
