#coding:utf-8
import grpc_pb2
import grpc_pb2_grpc
import threading
import time
import re
import bc_enum

_compiNum = re.compile("^\d+$")  #判斷全數字用
_compiW = re.compile("^\w{64}")

class Synchronization(grpc_pb2_grpc.SynchronizationServicer):
    def ExchangeBlock(self, request, context):
        import block
        print("=> [ExchangeBlock]")
        print (request)
        box=block.Block()
        box.pb2=request
        block.Chain.addBlock(request.blockhash,box)
        box = block.Chain.getBlockFromHeight(block.Chain.getHeight()).pb2
        print("<= [ExchangeBlock]")
        print (box)
        return box
    def BlockFrom(self, request, context):
        import block
        # => 請求(依據高度或Hash)
        # <= 區塊
        print ("=> [BlockFrom] info:%s " % request.value)
        try:
            if _compiNum.search(request.value) != None:
                box=block.Chain.getBlockFromHeight(int(request.value)).pb2
                print ("<= [BlockFrom] Block")
                print (box)
                return box
            elif _compiW.search(request.value)!= None:
                box=block.Chain.getBlockFromHash(request.value).pb2
                print ("<= [BlockFrom] Block")
                return box
        except Exception as e:
            print(e)
    def BlockTo(self, request, context):
        import block
        # => Block
        # <= 如果高度增加 回傳 SYNCHRONIZATION ,否則 NOT_SYNCHRONIZATION
        box=block.Block()
        box.pb2=request
        response=block.Chain.addBlock(request.blockhash,box)
        return grpc_pb2.Message(value=response)
    def TransactionTo(self, request, context):
        import transaction
        # => 交易
        # <= Hash
        print ("=> unixtime:%s\tbody:%s" % (request.unixtime,request.body))
        tx=transaction.Transaction()
        tx.txload(request)
        print ("<= txhash:%s" % request.txhash)
        return grpc_pb2.Message(value=request.txhash)
    def TransactionFrom(self, request, context):
        import transaction
        # => 請求(Hash)
        # <= 交易
        print ("=> txhash:%s" % request.value)
        if request.value in transaction.Transaction.Transactions:
            if transaction.Transaction.Transactions[request.value]!="":
                pb2=transaction.Transaction.Transactions[request.value].pb2
                print ("<= unixtime:%s\tbody:%s" % (pb2.unixtime,pb2.body))
                return pb2
        print("<= not found tx")
        return grpc_pb2.Transaction()
__BranchTarget = ""
flag = False

def setBranchTarget(hashvalue):
    global flag,__BranchTarget
    __BranchTarget,flag = hashvalue,True
    print("Status => Sync")
    threading.Thread(target = unlock).start()
def unlock():
    global flag,__BranchTarget
    time.sleep(600);
    __BranchTarget,flag = "",False
def Task(stub,task,message):
    import block
    import transaction
    if task == bc_enum.Synchronization.TRANSACTIONFROM:
        response = stub.TransactionFrom(message)
        transaction.Transaction.TransactionFromRecv(response)
    elif task == bc_enum.Synchronization.TRANSACTIONTO:
        return stub.TransactionTo(message)
    elif task == bc_enum.Synchronization.BLOCKFROM:
        response = stub.BlockFrom(message)
        block.Block.FromRecv(response)
    elif task == bc_enum.Synchronization.BLOCKTO:
        response = stub.BlockTo(message)
        block.Block.ToRecv(response)
    elif task == bc_enum.Synchronization.EXCHANGEBLOCK:
        response = stub.ExchangeBlock(message)
        block.Block.ExchangeBlockRecv(response)