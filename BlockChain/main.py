from blockchain import BlockChain

myChain = BlockChain()
myChain.addBlock("first block")
myChain.addBlock("second block")
myChain.addBlock("third block")
myChain.addBlock("forth block")


for block in myChain.getBlocks():
    print block.getData()

print myChain.getBlock(1).getData()
