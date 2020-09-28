from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def bfs(root):
    que = deque([root])

    while len(que) > 0:
        element = que.popleft()
        print(element.data)
        if element.left:
            que.append(element.left)

        if element.right:
            que.append(element.right)


if __name__ == '__main__':

    b = Node('B', left=Node('D'), right=Node('E'))
    c = Node('C')
    root_node = Node('A', left=b, right=c)
    bfs(root_node)
