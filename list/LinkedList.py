class node(object):
    def __init__(self , data = None , next = None):
        self.next = next
        self.data = data
class LinkedList(object):
    def __init__(self):
        self.head = node()
    def enlist(self , data):
        temp_node = node(data , self.head)
        self.head = temp_node
    def showList(self):
        cur = self.head
        print '[',
        while(cur.data != None):
            print cur.data,
            cur = cur.next
            if(cur.data!=None):
                print ',',
        print ']'
    def index(self , indx):
        try:
            assert (indx <= (self.getSize() - 1))
        except AssertionError:
            print "Error!: Linked List index out of range"
            return
        cur = self.head
        for i in range(0 , indx):
            cur = cur.next
        return cur.data
    def push(self , indx , data):
        try:
            assert (indx <= (self.getSize() - 1))
        except AssertionError:
            print "Error!: Linked List index out of range"
            return
        cur = self.head
        if(indx == 0):
            temp = node(data , self.head)
            self.head = temp
            return
        for i in range(0,indx-1):
            cur = cur.next
        temp = node(data , cur.next)
        cur.next = temp
    def getSize(self):
        cur = self.head
        count = 0
        while(cur.data != None):
            cur = cur.next
            count += 1
        return count
    def del_data(self , indx):
        try:
            assert (indx <= (self.getSize() - 1))
        except AssertionError:
            print "Error!: Linked List index out of range"
            return
        cur = self.head
        if(indx == 0):
            self.head = cur.next
            return
        for i in range(0, indx - 1):
            cur = cur.next
        cur.next = cur.next.next
lst = LinkedList()
map(lambda x : lst.enlist(x) , range(0 , 11))
lst.showList()
