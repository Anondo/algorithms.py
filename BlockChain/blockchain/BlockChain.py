from Block import Block

class BlockChain(object):

    def __init__(self):
        self.head = Block()

    def addBlock(self , data):
        if not self.head.getData():
            self.head.setData(data)
            self.head.generateHash(data)
        else:
            temp = Block(data , self.head.getHash() ,  self.head)
            self.head = temp

    def getBlocks(self):
        chain  = []
        current = self.head
        while(current):
            chain.append(current)
            current = current.getNextBlock()
        return chain
    def getBlock(self , index):
        count = 0
        current  = self.head
        while(current):
            if(count == index):
                break
            current = current.getNextBlock()
            count += 1
        assert current , "Index out of range"
        return current
    def getChainLength(self):
        return Block.blockCount
