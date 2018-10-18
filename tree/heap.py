class Node(object):
    def __init__(self ,  data = None , parent = None , right_child = None , left_child = None):
        self.data = data
        self.parent = parent
        self.right_child = right_child
        self.left_child = left_child

class Heap(object):
    def __init__(self):
        self.root = Node()

    def traverse(self , current = None):
        if(current == None):
            current = self.root
        if(current.data):
            if(current.left_child or current.right_child):
                self.traverse(current.left_child)
                self.traverse(current.right_child)
                print current.left_child.data
                print current.right_child.data
        if(current == self.root):
            print current.data

    def plant(self , data):
        if not self.root.data:
            self.root.data = data
        else:
            current = self.root
            while(1):
                if not current.left_child:
                    current.left_child = Node()
                if not current.right_child:
                    current.right_child = Node()

                lchild = current.left_child
                rchild = current.right_child
                if not lchild.data:
                    lchild.data = data
                    lchild.parent = current
                    self.heapify(lchild)
                    break
                elif not rchild.data:
                    rchild.data = data
                    rchild.parent = current
                    self.heapify(rchild)
                    break
                else:
                    current = lchild
                    if(not lchild.left_child or not lchild.right_child):
                        current = lchild
                        continue
                    elif not lchild.left_child.data or not lchild.right_child.data:
                        current = lchild
                        continue
                    if(not rchild.left_child or not rchild.right_child):
                        current = rchild
                    elif not rchild.left_child.data or not rchild.right_child.data:
                        current = rchild




    def heapify(self , child):
        if not child.parent:
            return
        if(child.data > child.parent.data):
            temp = child.data
            child.data = child.parent.data
            child.parent.data = temp
            self.heapify(child.parent)
        else:
            return

heap = Heap()
data = [35, 33 , 42 , 10 , 14 , 19 , 27 , 44 , 26 , 31]
for d in data:
    heap.plant(d)
heap.traverse()
