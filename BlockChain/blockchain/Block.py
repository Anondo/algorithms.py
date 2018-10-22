from datetime import datetime

class Block(object):

    blockCount = 0

    def __init__(self , data = None , prevHash = None ,  nextBlock = None ):
        self.__nextBlock = nextBlock
        self.__data = data
        self.__prevHash = prevHash
        Block.blockCount += 1
        self.__timestamp = datetime.now()
        self.__hash = self.generateHash(self.__data)

    def generateHash(self , data):
        hsh = str(hash(data))
        if hsh == str(hash(None)):
            return hsh
        dt = str(self.__timestamp).split()
        dt[0] = "".join(dt[0].split("-"))
        dt[1] = "".join(dt[1].split(":"))
        dt = "".join(dt)
        hsh += str(dt)
        return hsh
    def getNextBlock(self):
        return self.__nextBlock
    def getData(self):
        return self.__data
    def getHash(self):
        return self.__hash
    def getPrevHash(self):
        return self.__prevHash
    def getTimeStamp(self):
        return self.__timestamp
    def setNextBlock(self , block):
        pass
    def setData(self , data):
        if self.__hash == str(hash(None)):
            self.__data = data
        else:
            testHash = self.generateHash(data)
            assert testHash == self.__hash , "Blockchain is immutable"
            self.__data == data
    def setPrevHash(self):
        pass
