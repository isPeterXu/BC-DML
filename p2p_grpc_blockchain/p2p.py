#coding:utf-8
import threading
import time
import os
import socket
import random
import re
from concurrent import futures
import grpc
import block
import synchronization
import transaction
import grpc_pb2
import grpc_pb2_grpc
import bc_enum

PORT = ""
GET_SELFNODE_FALG = False
selfipport = ""
linkBroadcastFlag=False

class Node:
    __Nodes = set()
    #add nodes
    @staticmethod
    def add(target):
        if type(target) == str:
            if not (target in Node.__Nodes):
                print( "=> get new Node %s" % target )
                Node.__Nodes.add(target)
                def linkBroadcast():
                    global linkBroadcastFlag
                    if linkBroadcastFlag == False:
                        linkBroadcastFlag = True
                        while linkBroadcastFlag:
                            time.sleep(random.randint(1, 60));
                            linkBroadcastBlock = block.Chain.getBlockFromHeight(block.Chain.getHeight())
                            linkBroadcastBlock.ExchangeBlock()
                threading.Thread(target=linkBroadcast).start()
        elif type(target) == list:
            for i in target:
                Node.add(i)
        elif type(target) == tuple:
            Node.add("%s:%s" % target )
    #get full node list
    @staticmethod
    def getNodesList():
        result = list()
        try:
            nodes = Node.__Nodes
            for i in nodes:
                result.append(i)
            return result
        except Exception as e:
            print (e)
    #broadcast
    @staticmethod
    def broadcast(task, message=""):
        global selfipport
        try:
            nodes = set()
            nodes.add(selfipport)
            nodes = Node.__Nodes-nodes
            for i in nodes:
                Node.send(i,task,message)
        except Exception as e:
            print (e)
    @staticmethod
    def passBroadcast(node,task,message):
        global selfipport
        try:
            nodes = set((node, selfipport))
            nodes = Node.__Nodes - nodes
            for i in temp:
                Node.send(i,task,message)
        except Exception as e:
            pass
    #??????
    @staticmethod
    def send(node, task, message = ""):
        try:
            channel = grpc.insecure_channel(node )
            taskType,task =task / bc_enum.Service.SERVICE, task % bc_enum.Service.SERVICE
            if taskType == bc_enum.Network.DESCOVERY:
                stub = grpc_pb2_grpc.DiscoveryStub(channel)
                if task == bc_enum.Synchronization.EXCHANGENODE:
                    response = stub.ExchangeNode(grpc_pb2.Node(number = len(Node.__Nodes),ipport = Node.getNodesList() ))
                    for node in response.ipport :
                        Node.__Nodes.add(node)
            elif taskType == bc_enum.Network.SYNCHRONIZATION:
                stub = grpc_pb2_grpc.SynchronizationStub(channel)
                synchronization.Task(stub,task,message)
        except Exception as e :
            Node.delNode(node)
        return
    @staticmethod
    def delNode(node):
        Node.__Nodes.remove(node)
    #?????? ???????????????
    @staticmethod
    def getLenght():
        return len(Node.__Nodes)
tempPort = 0

def __tempSocket(nodePort):
    # ???????????????????????? ??????Socket ???????????????IP
    global tempPort
    while tempPort == 0:
        port = int(PORT) + 1
        sock = ""
        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            sock.bind(("0.0.0.0",port))
            sock.listen(1)
            tempPort = port
            (conn, client_addr) = sock.accept()
            tempPort = 0
            print("=> Node IP:%s" % client_addr[0])
            conn.send(client_addr[0])
            conn.close()
            sock.close()
            Node.add((client_addr[0],nodePort)) #???????????? "ip:port"
        except Exception as e:
            pass
            
#????????????????????? port 
def talkYouIP(nodePort):
    global tempPort
    if tempPort == 0:
        threading.Thread(target = __tempSocket, args = (nodePort,)).start()
    while tempPort == 0:
        time.sleep(1)
    return tempPort

class Discovery(grpc_pb2_grpc.DiscoveryServicer):
    # ??????????????????
    def ExchangeNode(self, request, context):
        nodelist = Node.getNodesList()
        Node.add(list(request.ipport))
        return grpc_pb2.Node(number = Node.getLenght(),ipport = nodelist)
    # ??????????????????ip,???????????? grpc port,
    # ?????????????????????port ->???????????????????????????ip
    def Hello(self , request , context):
        global PORT,selfipport
        selfIP = request.value[0:request.value.index('|')]
        Node.add((selfIP,PORT))
        selfipport= "%s:%s" % (selfIP,PORT)
        nodePort = request.value[request.value.index('|')+1:len(request.value)]
        print("=> Node Port:%s" % nodePort)
        port = talkYouIP(nodePort)
        return grpc_pb2.Message(value = str(port))

#????????????????????????
def exchangeLoop():
    while True :
        print("<= exchange list broadcast %s" %Node.getNodesList())
        Node.broadcast(bc_enum.Service.SERVICE*bc_enum.Network.DESCOVERY+bc_enum.Synchronization.EXCHANGENODE)
        time.sleep(30)

def __grpcNetworkStart():
    global PORT
    try:
        PORT = os.environ["GRPC_PORT"]
    except:
        PORT = "8001"
    print("grpc listen port:"+PORT)
    # grpc server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
    grpc_pb2_grpc.add_DiscoveryServicer_to_server(Discovery(),server)
    # grpc_pb2_grpc.add_ConsensusServicer_to_server(Discovery(),server)
    grpc_pb2_grpc.add_SynchronizationServicer_to_server(synchronization.Synchronization(),server)
    server.add_insecure_port("[::]:%s" % PORT)
    server.start()
    threading.Thread(target = exchangeLoop).start()
    try:
        ROOT_TARGET = os.environ["ROOT_TARGET"]
    except:
        ROOT_TARGET = "35.185.134.104:8001"
    threading.Thread(target = grpcJoinNode ,args=(ROOT_TARGET,)).start()
    while True:
        time.sleep(1)

def grpcNetworkStart():
    # grpc ????????????????????? ??????Thread????????????
    threading.Thread(target = __grpcNetworkStart).start()

def grpcJoinNode(target):
    global PORT ,GET_SELFNODE_FALG,selfipport
    target = str(target)
    compi = re.compile('^(\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}):(\d{1,5})$')
    result = compi.match(target)
    # ?????????????????????????????????
    if result ==None or (target in Node.getNodesList() ):
        return False
    Node.add(target)
    # ???????????????????????????IP
    if GET_SELFNODE_FALG:
        return True
    # Discovery.Hello()
    ip = result.group(1)
    print("<= grpc link to %s" % target)
    channel = grpc.insecure_channel( target )
    stub = grpc_pb2_grpc.DiscoveryStub(channel)
    HelloResponse = None
    try:
        HelloResponse = stub.Hello(grpc_pb2.Message(value = "%s|%s" % (ip,PORT) )) #target ip & self port
    except:
        return False
    helloPort = HelloResponse.value
    time.sleep(1)
    # ??????????????????IP ??????????????????????????????
    # socket get my ip
    print("=> hello port:%s" % helloPort)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("<= connect to socket will get myIP")
    sock.connect( (ip,int(helloPort)) )
    myIP = sock.recv(1024)
    print("=> get myIP:%s" % myIP)
    Node.add((myIP,PORT))
    selfipport= "%s:%s" % (myIP,PORT)
    GET_SELFNODE_FALG = True
    return True

