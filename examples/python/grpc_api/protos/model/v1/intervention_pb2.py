# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/model/v1/intervention.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.model.v1 import media_pb2 as protos_dot_model_dot_v1_dot_media__pb2
from protos.model.v1 import event_pb2 as protos_dot_model_dot_v1_dot_event__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"protos/model/v1/intervention.proto\x12\x08v1.model\x1a\x1bprotos/model/v1/media.proto\x1a\x1bprotos/model/v1/event.proto\"\x84\x04\n\x13InterventionRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1c\n\ttimestamp\x18\x02 \x01(\x03R\ttimestamp\x12.\n\x08severity\x18\x03 \x01(\x0e\x32\x12.v1.model.SeverityR\x08severity\x12I\n\x11selection_request\x18\x04 \x01(\x0b\x32\x1a.v1.model.SelectionRequestH\x00R\x10selectionRequest\x12\x46\n\x10labeling_request\x18\x05 \x01(\x0b\x32\x19.v1.model.LabelingRequestH\x00R\x0flabelingRequest\x12@\n\x0eteleop_request\x18\x08 \x01(\x0b\x32\x17.v1.model.TeleopRequestH\x00R\rteleopRequest\x12;\n\x04tags\x18\x06 \x03(\x0b\x32\'.v1.model.InterventionRequest.TagsEntryR\x04tags\x12<\n\tresponses\x18\x07 \x03(\x0b\x32\x1e.v1.model.InterventionResponseR\tresponses\x1a\x37\n\tTagsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\x06\n\x04\x64\x61ta\"\xc9\x02\n\x14InterventionResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\nrequest_id\x18\x02 \x01(\tR\trequestId\x12\x1c\n\ttimestamp\x18\x03 \x01(\x03R\ttimestamp\x12L\n\x12selection_response\x18\x04 \x01(\x0b\x32\x1b.v1.model.SelectionResponseH\x00R\x11selectionResponse\x12I\n\x11labeling_response\x18\x05 \x01(\x0b\x32\x1a.v1.model.LabelingResponseH\x00R\x10labelingResponse\x12\x43\n\x0fteleop_response\x18\x06 \x01(\x0b\x32\x18.v1.model.TeleopResponseH\x00R\x0eteleopResponseB\x06\n\x04\x64\x61ta\"@\n\x05Label\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\"V\n\x0eLabeledPolygon\x12,\n\x08vertices\x18\x01 \x03(\x0b\x32\x10.v1.model.VertexR\x08vertices\x12\x16\n\x06labels\x18\x02 \x03(\tR\x06labels\"$\n\x06Vertex\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\"\xc7\x01\n\x0fLabelingRequest\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0binstruction\x18\x02 \x01(\tR\x0binstruction\x12%\n\x05image\x18\x03 \x01(\x0b\x32\x0f.v1.model.ImageR\x05image\x12\'\n\x06labels\x18\x04 \x03(\x0b\x32\x0f.v1.model.LabelR\x06labels\x12,\n\x04hint\x18\x05 \x03(\x0b\x32\x18.v1.model.LabeledPolygonR\x04hint\"B\n\x10LabelingResponse\x12.\n\x05value\x18\x01 \x03(\x0b\x32\x18.v1.model.LabeledPolygonR\x05value\"\xa9\x01\n\x10SelectionRequest\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12\'\n\x05image\x18\x02 \x01(\x0b\x32\x0f.v1.model.ImageH\x00R\x05image\x12 \n\x0binstruction\x18\x03 \x01(\tR\x0binstruction\x12\x18\n\x07options\x18\x04 \x03(\tR\x07options\x12\x12\n\x04hint\x18\x05 \x01(\rR\x04hintB\x06\n\x04\x64\x61ta\")\n\x11SelectionResponse\x12\x14\n\x05value\x18\x01 \x01(\rR\x05value\"1\n\rTeleopRequest\x12 \n\x0binstruction\x18\x01 \x01(\tR\x0binstruction\"<\n\x0eTeleopResponse\x12\x14\n\x05state\x18\x01 \x01(\tR\x05state\x12\x14\n\x05notes\x18\x02 \x01(\tR\x05notesB+Z)github.com/FormantIO/genproto/go/v1/modelb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.model.v1.intervention_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z)github.com/FormantIO/genproto/go/v1/model'
  _INTERVENTIONREQUEST_TAGSENTRY._options = None
  _INTERVENTIONREQUEST_TAGSENTRY._serialized_options = b'8\001'
  _INTERVENTIONREQUEST._serialized_start=107
  _INTERVENTIONREQUEST._serialized_end=623
  _INTERVENTIONREQUEST_TAGSENTRY._serialized_start=560
  _INTERVENTIONREQUEST_TAGSENTRY._serialized_end=615
  _INTERVENTIONRESPONSE._serialized_start=626
  _INTERVENTIONRESPONSE._serialized_end=955
  _LABEL._serialized_start=957
  _LABEL._serialized_end=1021
  _LABELEDPOLYGON._serialized_start=1023
  _LABELEDPOLYGON._serialized_end=1109
  _VERTEX._serialized_start=1111
  _VERTEX._serialized_end=1147
  _LABELINGREQUEST._serialized_start=1150
  _LABELINGREQUEST._serialized_end=1349
  _LABELINGRESPONSE._serialized_start=1351
  _LABELINGRESPONSE._serialized_end=1417
  _SELECTIONREQUEST._serialized_start=1420
  _SELECTIONREQUEST._serialized_end=1589
  _SELECTIONRESPONSE._serialized_start=1591
  _SELECTIONRESPONSE._serialized_end=1632
  _TELEOPREQUEST._serialized_start=1634
  _TELEOPREQUEST._serialized_end=1683
  _TELEOPRESPONSE._serialized_start=1685
  _TELEOPRESPONSE._serialized_end=1745
# @@protoc_insertion_point(module_scope)
