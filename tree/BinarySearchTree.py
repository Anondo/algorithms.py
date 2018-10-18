class node(object):
    def __init__(self , data = None , left_child = None , right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

class tree(object):
    def __init__(self):
        self.root = node()
    def plant(self , data):
        if(self.root.data == None):
            self.root.data = data
        else:
            parent = self.root
            current = parent
            while(1):
                if(parent.left_child == None or parent.right_child == None):
                    parent.left_child = node()
                    parent.right_child = node()
                if(data < parent.data):
                    current = parent.left_child
                else:
                    current  = parent.right_child
                if( current.data == None):
                    current.data = data
                    break
                else:
                    parent = current
    def searchWithSimulation(self , data):
        current = self.root
        while(1):
            print "Comparing {} with {}".format(data , current.data)
            if(current.data == data):
                print "{} found".format(data)
                break
            else:
                if(data < current.data):
                    print "Moving Left"
                    current = current.left_child
                else:
                    print "Moving Right"
                    current = current.right_child
            if(current == None):
                print "Data not found"
                break
    def search(self , data):
        current = self.root
        while(1):
            if(current.data == data):
                print "{} found".format(data)
                break
            else:
                if(data < current.data):
                    current = current.left_child
                else:
                    current = current.right_child
            if(current == None):
                print "Data not found"
                break
    def postOrderTraversal(self , current = " "):
        if(current == " "):
            current = self.root
        if(current.data != None):
            if(current.left_child != None or current.right_child != None):
                self.postOrderTraversal(current.left_child)
                self.postOrderTraversal(current.right_child)
                print current.left_child.data
                print current.right_child.data
        if(current == self.root):
            print current.data
    def preOrderTraversal(self , current = " "):
        if(current == " "):
            current = self.root
        if(current.data != None):
            print current.data
            if(current.left_child != None or current.right_child != None):
                self.preOrderTraversal(current.left_child)
                self.preOrderTraversal(current.right_child)

t = tree()
t.plant(27)
t.plant(14)
t.plant(35)
t.plant(10)
t.plant(19)
t.plant(31)
t.plant(42)
#t.searchWithSimulation(10)
#t.postOrderTraversal()
t.postOrderTraversal()
