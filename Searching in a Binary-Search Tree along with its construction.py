class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
        
def insertIntoBST(root,ele):
    if root == None:
        newBlock=TreeNode(ele)
        return newBlock
    
    if root.data<ele:
        root.right=insertIntoBST(root.right,ele)
    else:
        root.left=insertIntoBST(root.left,ele)
    return root

def searchInBST(root,target):
    if root == None:
        return False
    elif root.data == target:
        return True
    elif root.data<target:
        return searchInBST(root.right,target)
    return searchInBST(root.left,target)
    
def printInOrderTraversal(root):
    if root == None:
        return
 
    printInOrderTraversal(root.left)
    print(root.data, end = " ")
    printPreOrder(root.right)
    
n=int(input())
l=list(map(int,input().split()))
target1=int(input())
root=None
for ele in l:
    root= insertIntoBST(root,ele)
if searchInBST(root,target1)==True:
    print("Target element is found")
else:
    print("Target element is not found")

 
    
