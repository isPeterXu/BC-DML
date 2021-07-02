from enum import Enum

class Block(Enum):
    QUERY_BLOCK_LATEST = 0
    QUERY_BLOCK_FROM_HEIGHT = 1
    RESPONSE_BLOCKCHAIN = 2

class Chain(Enum):
    LOAD_SUCCESS = 1
    HEIGHT_TOO_LOW = 2
    LOAD_FAILS = 3
    NOTNEXTBLOCK = 4

class Service(Enum):
    SERVICE = 1000

class Network(Enum):
    DESCOVERY = 1
    SYNCHRONIZATION = 2
    CONSENSUS = 3

class Synchronization(Enum):
    EXCHANGENODE = 1
    BLOCKFROM = 1
    BLOCKTO = 2
    TRANSACTIONFROM = 3
    TRANSACTIONTO = 4
    EXCHANGEBLOCK = 5

class Block_Verify(Enum):
    SUCCESS_VERTIFY = 1
    ERROR_BLOCK_HASH_VERTIFY = 2
    WARNING_PREVIOUS_HASH_NOT_EQUAL = 3
    NOT_FOUND_BLOCK = 4