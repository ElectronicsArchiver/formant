# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/model/v1/commands.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from protos.model.v1 import datapoint_pb2 as protos_dot_model_dot_v1_dot_datapoint__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eprotos/model/v1/commands.proto\x12\x08v1.model\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1fprotos/model/v1/datapoint.proto\"\xc8\x01\n\x0e\x43ommandRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x18\n\x07\x63ommand\x18\x02 \x01(\tR\x07\x63ommand\x12\x14\n\x04text\x18\x03 \x01(\tH\x00R\x04text\x12?\n\rscrubber_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0cscrubberTime\x12(\n\x05\x66iles\x18\x05 \x03(\x0b\x32\x12.v1.model.FileInfoR\x05\x66ilesB\x0b\n\tparameter\"\x89\x01\n\x0f\x43ommandResponse\x12\x1d\n\nrequest_id\x18\x01 \x01(\tR\trequestId\x12\x18\n\x07success\x18\x02 \x01(\x08R\x07success\x12\x33\n\tdatapoint\x18\x03 \x01(\x0b\x32\x13.v1.model.DatapointH\x00R\tdatapointB\x08\n\x06result\"@\n\x08\x46ileInfo\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x10\n\x03url\x18\x03 \x01(\tR\x03urlB+Z)github.com/FormantIO/genproto/go/v1/modelb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.model.v1.commands_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/FormantIO/genproto/go/v1/model'
  _COMMANDREQUEST._serialized_start=111
  _COMMANDREQUEST._serialized_end=311
  _COMMANDRESPONSE._serialized_start=314
  _COMMANDRESPONSE._serialized_end=451
  _FILEINFO._serialized_start=453
  _FILEINFO._serialized_end=517
# @@protoc_insertion_point(module_scope)
