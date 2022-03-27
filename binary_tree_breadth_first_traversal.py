class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
    #     a
    #   /   \
    #   b   c
    #  /\    \
    # d  e    f
    # [a b c d e f]

def BFS(root):
    if root == None:
        return list()
    queue = [root]
    solution = []
    while len(queue) > 0:
        node = queue.pop(0)
        solution.append(node.value)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    return solution
   

if __name__ == '__main__':
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    print(BFS(a))
