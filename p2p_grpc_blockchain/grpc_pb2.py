# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='grpc.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ngrpc.proto\"=\n\x0bTransaction\x12\x10\n\x08unixtime\x18\x01 \x01(\t\x12\x0c\n\x04\x62ody\x18\x02 \x01(\x0c\x12\x0e\n\x06txhash\x18\x03 \x03(\t\"\x87\x01\n\x05\x42lock\x12\x0e\n\x06height\x18\x01 \x01(\x04\x12\x10\n\x08unixtime\x18\x02 \x01(\t\x12\x14\n\x0cprevioushash\x18\x03 \x01(\t\x12\x11\n\tblockhash\x18\x04 \x01(\t\x12\x12\n\ndifficulty\x18\x05 \x01(\t\x12\x0e\n\x06\x61nswer\x18\x06 \x01(\t\x12\x0f\n\x07txshash\x18\x07 \x03(\t\"&\n\x04Node\x12\x0e\n\x06number\x18\x01 \x01(\x05\x12\x0e\n\x06ipport\x18\x02 \x03(\x0c\"\x18\n\x07Message\x12\r\n\x05value\x18\x01 \x01(\x0c\x32\x46\n\tDiscovery\x12\x1c\n\x0c\x45xchangeNode\x12\x05.Node\x1a\x05.Node\x12\x1b\n\x05Hello\x12\x08.Message\x1a\x08.Message2\xc2\x01\n\x0fSynchronization\x12\x1d\n\tBlockFrom\x12\x08.Message\x1a\x06.Block\x12\x1b\n\x07\x42lockTo\x12\x06.Block\x1a\x08.Message\x12\x1f\n\rExchangeBlock\x12\x06.Block\x1a\x06.Block\x12\'\n\rTransactionTo\x12\x0c.Transaction\x1a\x08.Message\x12)\n\x0fTransactionFrom\x12\x08.Message\x1a\x0c.Transactionb\x06proto3'
)




_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='unixtime', full_name='Transaction.unixtime', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='body', full_name='Transaction.body', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='txhash', full_name='Transaction.txhash', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=75,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='Block.height', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unixtime', full_name='Block.unixtime', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='previoushash', full_name='Block.previoushash', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='blockhash', full_name='Block.blockhash', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='difficulty', full_name='Block.difficulty', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='answer', full_name='Block.answer', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='txshash', full_name='Block.txshash', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=78,
  serialized_end=213,
)


_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='Node.number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ipport', full_name='Node.ipport', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=253,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Message.value', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=255,
  serialized_end=279,
)

DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), {
  'DESCRIPTOR' : _TRANSACTION,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:Transaction)
  })
_sym_db.RegisterMessage(Transaction)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:Block)
  })
_sym_db.RegisterMessage(Block)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {
  'DESCRIPTOR' : _NODE,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:Node)
  })
_sym_db.RegisterMessage(Node)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'grpc_pb2'
  # @@protoc_insertion_point(class_scope:Message)
  })
_sym_db.RegisterMessage(Message)



_DISCOVERY = _descriptor.ServiceDescriptor(
  name='Discovery',
  full_name='Discovery',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=281,
  serialized_end=351,
  methods=[
  _descriptor.MethodDescriptor(
    name='ExchangeNode',
    full_name='Discovery.ExchangeNode',
    index=0,
    containing_service=None,
    input_type=_NODE,
    output_type=_NODE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Hello',
    full_name='Discovery.Hello',
    index=1,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DISCOVERY)

DESCRIPTOR.services_by_name['Discovery'] = _DISCOVERY


_SYNCHRONIZATION = _descriptor.ServiceDescriptor(
  name='Synchronization',
  full_name='Synchronization',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=354,
  serialized_end=548,
  methods=[
  _descriptor.MethodDescriptor(
    name='BlockFrom',
    full_name='Synchronization.BlockFrom',
    index=0,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_BLOCK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BlockTo',
    full_name='Synchronization.BlockTo',
    index=1,
    containing_service=None,
    input_type=_BLOCK,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ExchangeBlock',
    full_name='Synchronization.ExchangeBlock',
    index=2,
    containing_service=None,
    input_type=_BLOCK,
    output_type=_BLOCK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TransactionTo',
    full_name='Synchronization.TransactionTo',
    index=3,
    containing_service=None,
    input_type=_TRANSACTION,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TransactionFrom',
    full_name='Synchronization.TransactionFrom',
    index=4,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_TRANSACTION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SYNCHRONIZATION)

DESCRIPTOR.services_by_name['Synchronization'] = _SYNCHRONIZATION

# @@protoc_insertion_point(module_scope)
