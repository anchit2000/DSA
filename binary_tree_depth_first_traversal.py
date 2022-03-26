class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
def DFT(root):
    if root == None:
        return None
    result = []
    stack = [root]
    while len(stack) > 0:
        res = stack.pop()
        result.append(res.value)
        if res.right:
            stack.append(res.right)
        if res.left:
            stack.append(res.left)
    return result
  
def DFT_reccur(root,solution):
    solution.append(root.value)
    if root.left:
        DFT_reccur(root.left,solution)
    if root.right:
        DFT_reccur(root.right,solution)
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
    
    print(DFT(a))
    print(DFT_reccur(a,list()))
