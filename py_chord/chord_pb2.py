# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: chord.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'chord.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x63hord.proto\x12\x05\x63hord\"\x07\n\x05\x45mpty\"\x1a\n\tBoolValue\x12\r\n\x05value\x18\x01 \x01(\x08\",\n\x04Node\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\n\n\x02id\x18\x03 \x01(\x03\"\x17\n\tIdRequest\x12\n\n\x02id\x18\x01 \x01(\x03\"D\n\x18UpdateFingerTableRequest\x12\x19\n\x04node\x18\x01 \x01(\x0b\x32\x0b.chord.Node\x12\r\n\x05index\x18\x02 \x01(\x05\"\x1d\n\x0cStoreRequest\x12\r\n\x05value\x18\x01 \x01(\x0c\"\x1a\n\x0bKeyResponse\x12\x0b\n\x03key\x18\x01 \x01(\x03\"\x19\n\nKeyRequest\x12\x0b\n\x03key\x18\x01 \x01(\x03\"\x1e\n\rValueResponse\x12\r\n\x05value\x18\x01 \x01(\x0c\x32\x9d\x04\n\x0c\x43hordService\x12)\n\x07IsAlive\x12\x0c.chord.Empty\x1a\x10.chord.BoolValue\x12+\n\x0eGetPredecessor\x12\x0c.chord.Empty\x1a\x0b.chord.Node\x12+\n\x0eSetPredecessor\x12\x0b.chord.Node\x1a\x0c.chord.Empty\x12)\n\x0cGetSuccessor\x12\x0c.chord.Empty\x1a\x0b.chord.Node\x12)\n\x0cSetSuccessor\x12\x0b.chord.Node\x1a\x0c.chord.Empty\x12.\n\rFindSuccessor\x12\x10.chord.IdRequest\x1a\x0b.chord.Node\x12\x42\n\x11UpdateFingerTable\x12\x1f.chord.UpdateFingerTableRequest\x1a\x0c.chord.Empty\x12\x30\n\x05Store\x12\x13.chord.StoreRequest\x1a\x12.chord.KeyResponse\x12.\n\x03Get\x12\x11.chord.KeyRequest\x1a\x14.chord.ValueResponse\x12\x37\n\x16\x43losestPrecedingFinger\x12\x10.chord.IdRequest\x1a\x0b.chord.Node\x12#\n\x06Notify\x12\x0b.chord.Node\x1a\x0c.chord.Emptyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chord_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=22
  _globals['_EMPTY']._serialized_end=29
  _globals['_BOOLVALUE']._serialized_start=31
  _globals['_BOOLVALUE']._serialized_end=57
  _globals['_NODE']._serialized_start=59
  _globals['_NODE']._serialized_end=103
  _globals['_IDREQUEST']._serialized_start=105
  _globals['_IDREQUEST']._serialized_end=128
  _globals['_UPDATEFINGERTABLEREQUEST']._serialized_start=130
  _globals['_UPDATEFINGERTABLEREQUEST']._serialized_end=198
  _globals['_STOREREQUEST']._serialized_start=200
  _globals['_STOREREQUEST']._serialized_end=229
  _globals['_KEYRESPONSE']._serialized_start=231
  _globals['_KEYRESPONSE']._serialized_end=257
  _globals['_KEYREQUEST']._serialized_start=259
  _globals['_KEYREQUEST']._serialized_end=284
  _globals['_VALUERESPONSE']._serialized_start=286
  _globals['_VALUERESPONSE']._serialized_end=316
  _globals['_CHORDSERVICE']._serialized_start=319
  _globals['_CHORDSERVICE']._serialized_end=860
# @@protoc_insertion_point(module_scope)
