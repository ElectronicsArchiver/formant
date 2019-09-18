# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/model/v1/intervention.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.model.v1 import media_pb2 as protos_dot_model_dot_v1_dot_media__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/model/v1/intervention.proto',
  package='v1.model',
  syntax='proto3',
  serialized_options=_b('Z)github.com/FormantIO/genproto/go/v1/model'),
  serialized_pb=_b('\n\"protos/model/v1/intervention.proto\x12\x08v1.model\x1a\x1bprotos/model/v1/media.proto\"\xc2\x03\n\x13InterventionRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1c\n\ttimestamp\x18\x02 \x01(\x03R\ttimestamp\x12.\n\x08severity\x18\x03 \x01(\x0e\x32\x12.v1.model.SeverityR\x08severity\x12I\n\x11selection_request\x18\x04 \x01(\x0b\x32\x1a.v1.model.SelectionRequestH\x00R\x10selectionRequest\x12\x46\n\x10labeling_request\x18\x05 \x01(\x0b\x32\x19.v1.model.LabelingRequestH\x00R\x0flabelingRequest\x12;\n\x04tags\x18\x06 \x03(\x0b\x32\'.v1.model.InterventionRequest.TagsEntryR\x04tags\x12<\n\tresponses\x18\x07 \x03(\x0b\x32\x1e.v1.model.InterventionResponseR\tresponses\x1a\x37\n\tTagsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\x42\x06\n\x04\x64\x61ta\"\x84\x02\n\x14InterventionResponse\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x1d\n\nrequest_id\x18\x02 \x01(\tR\trequestId\x12\x1c\n\ttimestamp\x18\x03 \x01(\x03R\ttimestamp\x12L\n\x12selection_response\x18\x04 \x01(\x0b\x32\x1b.v1.model.SelectionResponseH\x00R\x11selectionResponse\x12I\n\x11labeling_response\x18\x05 \x01(\x0b\x32\x1a.v1.model.LabelingResponseH\x00R\x10labelingResponseB\x06\n\x04\x64\x61ta\"@\n\x05Label\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\x12!\n\x0c\x64isplay_name\x18\x02 \x01(\tR\x0b\x64isplayName\"V\n\x0eLabeledPolygon\x12,\n\x08vertices\x18\x01 \x03(\x0b\x32\x10.v1.model.VertexR\x08vertices\x12\x16\n\x06labels\x18\x02 \x03(\tR\x06labels\"$\n\x06Vertex\x12\x0c\n\x01x\x18\x01 \x01(\x01R\x01x\x12\x0c\n\x01y\x18\x02 \x01(\x01R\x01y\"\xc7\x01\n\x0fLabelingRequest\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12 \n\x0binstruction\x18\x02 \x01(\tR\x0binstruction\x12%\n\x05image\x18\x03 \x01(\x0b\x32\x0f.v1.model.ImageR\x05image\x12\'\n\x06labels\x18\x04 \x03(\x0b\x32\x0f.v1.model.LabelR\x06labels\x12,\n\x04hint\x18\x05 \x03(\x0b\x32\x18.v1.model.LabeledPolygonR\x04hint\"B\n\x10LabelingResponse\x12.\n\x05value\x18\x01 \x03(\x0b\x32\x18.v1.model.LabeledPolygonR\x05value\"\xa9\x01\n\x10SelectionRequest\x12\x14\n\x05title\x18\x01 \x01(\tR\x05title\x12\'\n\x05image\x18\x02 \x01(\x0b\x32\x0f.v1.model.ImageH\x00R\x05image\x12 \n\x0binstruction\x18\x03 \x01(\tR\x0binstruction\x12\x18\n\x07options\x18\x04 \x03(\tR\x07options\x12\x12\n\x04hint\x18\x05 \x01(\rR\x04hintB\x06\n\x04\x64\x61ta\")\n\x11SelectionResponse\x12\x14\n\x05value\x18\x01 \x01(\rR\x05value*:\n\x08Severity\x12\x08\n\x04INFO\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x0c\n\x08\x43RITICAL\x10\x03\x42+Z)github.com/FormantIO/genproto/go/v1/modelb\x06proto3')
  ,
  dependencies=[protos_dot_model_dot_v1_dot_media__pb2.DESCRIPTOR,])

_SEVERITY = _descriptor.EnumDescriptor(
  name='Severity',
  full_name='v1.model.Severity',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INFO', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRITICAL', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1470,
  serialized_end=1528,
)
_sym_db.RegisterEnumDescriptor(_SEVERITY)

Severity = enum_type_wrapper.EnumTypeWrapper(_SEVERITY)
INFO = 0
WARNING = 1
ERROR = 2
CRITICAL = 3



_INTERVENTIONREQUEST_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='v1.model.InterventionRequest.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v1.model.InterventionRequest.TagsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='key', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.model.InterventionRequest.TagsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=465,
  serialized_end=520,
)

_INTERVENTIONREQUEST = _descriptor.Descriptor(
  name='InterventionRequest',
  full_name='v1.model.InterventionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.model.InterventionRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='v1.model.InterventionRequest.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='timestamp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='severity', full_name='v1.model.InterventionRequest.severity', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='severity', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selection_request', full_name='v1.model.InterventionRequest.selection_request', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='selectionRequest', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labeling_request', full_name='v1.model.InterventionRequest.labeling_request', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labelingRequest', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tags', full_name='v1.model.InterventionRequest.tags', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tags', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='responses', full_name='v1.model.InterventionRequest.responses', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='responses', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_INTERVENTIONREQUEST_TAGSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='data', full_name='v1.model.InterventionRequest.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=78,
  serialized_end=528,
)


_INTERVENTIONRESPONSE = _descriptor.Descriptor(
  name='InterventionResponse',
  full_name='v1.model.InterventionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.model.InterventionResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='v1.model.InterventionResponse.request_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='requestId', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='v1.model.InterventionResponse.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='timestamp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selection_response', full_name='v1.model.InterventionResponse.selection_response', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='selectionResponse', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labeling_response', full_name='v1.model.InterventionResponse.labeling_response', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labelingResponse', file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='data', full_name='v1.model.InterventionResponse.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=531,
  serialized_end=791,
)


_LABEL = _descriptor.Descriptor(
  name='Label',
  full_name='v1.model.Label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.model.Label.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='v1.model.Label.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='displayName', file=DESCRIPTOR),
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
  serialized_start=793,
  serialized_end=857,
)


_LABELEDPOLYGON = _descriptor.Descriptor(
  name='LabeledPolygon',
  full_name='v1.model.LabeledPolygon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vertices', full_name='v1.model.LabeledPolygon.vertices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='vertices', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='v1.model.LabeledPolygon.labels', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labels', file=DESCRIPTOR),
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
  serialized_start=859,
  serialized_end=945,
)


_VERTEX = _descriptor.Descriptor(
  name='Vertex',
  full_name='v1.model.Vertex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='v1.model.Vertex.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='x', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='v1.model.Vertex.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='y', file=DESCRIPTOR),
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
  serialized_start=947,
  serialized_end=983,
)


_LABELINGREQUEST = _descriptor.Descriptor(
  name='LabelingRequest',
  full_name='v1.model.LabelingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='v1.model.LabelingRequest.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='title', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instruction', full_name='v1.model.LabelingRequest.instruction', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='instruction', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='v1.model.LabelingRequest.image', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='image', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labels', full_name='v1.model.LabelingRequest.labels', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='labels', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hint', full_name='v1.model.LabelingRequest.hint', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hint', file=DESCRIPTOR),
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
  serialized_start=986,
  serialized_end=1185,
)


_LABELINGRESPONSE = _descriptor.Descriptor(
  name='LabelingResponse',
  full_name='v1.model.LabelingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.model.LabelingResponse.value', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR),
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
  serialized_start=1187,
  serialized_end=1253,
)


_SELECTIONREQUEST = _descriptor.Descriptor(
  name='SelectionRequest',
  full_name='v1.model.SelectionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='v1.model.SelectionRequest.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='title', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='v1.model.SelectionRequest.image', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='image', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instruction', full_name='v1.model.SelectionRequest.instruction', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='instruction', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='v1.model.SelectionRequest.options', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='options', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hint', full_name='v1.model.SelectionRequest.hint', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hint', file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='data', full_name='v1.model.SelectionRequest.data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1256,
  serialized_end=1425,
)


_SELECTIONRESPONSE = _descriptor.Descriptor(
  name='SelectionResponse',
  full_name='v1.model.SelectionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.model.SelectionResponse.value', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR),
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
  serialized_start=1427,
  serialized_end=1468,
)

_INTERVENTIONREQUEST_TAGSENTRY.containing_type = _INTERVENTIONREQUEST
_INTERVENTIONREQUEST.fields_by_name['severity'].enum_type = _SEVERITY
_INTERVENTIONREQUEST.fields_by_name['selection_request'].message_type = _SELECTIONREQUEST
_INTERVENTIONREQUEST.fields_by_name['labeling_request'].message_type = _LABELINGREQUEST
_INTERVENTIONREQUEST.fields_by_name['tags'].message_type = _INTERVENTIONREQUEST_TAGSENTRY
_INTERVENTIONREQUEST.fields_by_name['responses'].message_type = _INTERVENTIONRESPONSE
_INTERVENTIONREQUEST.oneofs_by_name['data'].fields.append(
  _INTERVENTIONREQUEST.fields_by_name['selection_request'])
_INTERVENTIONREQUEST.fields_by_name['selection_request'].containing_oneof = _INTERVENTIONREQUEST.oneofs_by_name['data']
_INTERVENTIONREQUEST.oneofs_by_name['data'].fields.append(
  _INTERVENTIONREQUEST.fields_by_name['labeling_request'])
_INTERVENTIONREQUEST.fields_by_name['labeling_request'].containing_oneof = _INTERVENTIONREQUEST.oneofs_by_name['data']
_INTERVENTIONRESPONSE.fields_by_name['selection_response'].message_type = _SELECTIONRESPONSE
_INTERVENTIONRESPONSE.fields_by_name['labeling_response'].message_type = _LABELINGRESPONSE
_INTERVENTIONRESPONSE.oneofs_by_name['data'].fields.append(
  _INTERVENTIONRESPONSE.fields_by_name['selection_response'])
_INTERVENTIONRESPONSE.fields_by_name['selection_response'].containing_oneof = _INTERVENTIONRESPONSE.oneofs_by_name['data']
_INTERVENTIONRESPONSE.oneofs_by_name['data'].fields.append(
  _INTERVENTIONRESPONSE.fields_by_name['labeling_response'])
_INTERVENTIONRESPONSE.fields_by_name['labeling_response'].containing_oneof = _INTERVENTIONRESPONSE.oneofs_by_name['data']
_LABELEDPOLYGON.fields_by_name['vertices'].message_type = _VERTEX
_LABELINGREQUEST.fields_by_name['image'].message_type = protos_dot_model_dot_v1_dot_media__pb2._IMAGE
_LABELINGREQUEST.fields_by_name['labels'].message_type = _LABEL
_LABELINGREQUEST.fields_by_name['hint'].message_type = _LABELEDPOLYGON
_LABELINGRESPONSE.fields_by_name['value'].message_type = _LABELEDPOLYGON
_SELECTIONREQUEST.fields_by_name['image'].message_type = protos_dot_model_dot_v1_dot_media__pb2._IMAGE
_SELECTIONREQUEST.oneofs_by_name['data'].fields.append(
  _SELECTIONREQUEST.fields_by_name['image'])
_SELECTIONREQUEST.fields_by_name['image'].containing_oneof = _SELECTIONREQUEST.oneofs_by_name['data']
DESCRIPTOR.message_types_by_name['InterventionRequest'] = _INTERVENTIONREQUEST
DESCRIPTOR.message_types_by_name['InterventionResponse'] = _INTERVENTIONRESPONSE
DESCRIPTOR.message_types_by_name['Label'] = _LABEL
DESCRIPTOR.message_types_by_name['LabeledPolygon'] = _LABELEDPOLYGON
DESCRIPTOR.message_types_by_name['Vertex'] = _VERTEX
DESCRIPTOR.message_types_by_name['LabelingRequest'] = _LABELINGREQUEST
DESCRIPTOR.message_types_by_name['LabelingResponse'] = _LABELINGRESPONSE
DESCRIPTOR.message_types_by_name['SelectionRequest'] = _SELECTIONREQUEST
DESCRIPTOR.message_types_by_name['SelectionResponse'] = _SELECTIONRESPONSE
DESCRIPTOR.enum_types_by_name['Severity'] = _SEVERITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InterventionRequest = _reflection.GeneratedProtocolMessageType('InterventionRequest', (_message.Message,), dict(

  TagsEntry = _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), dict(
    DESCRIPTOR = _INTERVENTIONREQUEST_TAGSENTRY,
    __module__ = 'protos.model.v1.intervention_pb2'
    # @@protoc_insertion_point(class_scope:v1.model.InterventionRequest.TagsEntry)
    ))
  ,
  DESCRIPTOR = _INTERVENTIONREQUEST,
  __module__ = 'protos.model.v1.intervention_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.InterventionRequest)
  ))
_sym_db.RegisterMessage(InterventionRequest)
_sym_db.RegisterMessage(InterventionRequest.TagsEntry)

InterventionResponse = _reflection.GeneratedProtocolMessageType('InterventionResponse', (_message.Message,), dict(
  DESCRIPTOR = _INTERVENTIONRESPONSE,
  __module__ = 'protos.model.v1.intervention_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.InterventionResponse)
  ))
_sym_db.RegisterMessage(InterventionResponse)

Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), dict(
  DESCRIPTOR = _LABEL,
  __module__ = 'protos.model.v1.intervention_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Label)
  ))
_sym_db.RegisterMessage(Label)

LabeledPolygon = _reflection.GeneratedProtocolMessageType('LabeledPolygon', (_message.Message,), dict(
  DESCRIPTOR = _LABELEDPOLYGON,
  __module__ = 'protos.model.v1.intervention_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.LabeledPolygon)
  ))
_sym_db.RegisterMessage(LabeledPolygon)

Vertex = _reflection.GeneratedProtocolMessageType('Vertex', (_message.Message,), dict(
  DESCRIPTOR = _VERTEX,
  __module__ = 'protos.model.v1.intervention_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Vertex)
  ))
_sym_db.RegisterMessage(Vertex)

LabelingRequest = _reflection.GeneratedProtocolMessageType('LabelingRequest', (_message.Message,), dict(
  DESCRIPTOR = _LABELINGREQUEST,
  __module__ = 'protos.model.v1.intervention_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.LabelingRequest)
  ))
_sym_db.RegisterMessage(LabelingRequest)

LabelingResponse = _reflection.GeneratedProtocolMessageType('LabelingResponse', (_message.Message,), dict(
  DESCRIPTOR = _LABELINGRESPONSE,
  __module__ = 'protos.model.v1.intervention_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.LabelingResponse)
  ))
_sym_db.RegisterMessage(LabelingResponse)

SelectionRequest = _reflection.GeneratedProtocolMessageType('SelectionRequest', (_message.Message,), dict(
  DESCRIPTOR = _SELECTIONREQUEST,
  __module__ = 'protos.model.v1.intervention_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.SelectionRequest)
  ))
_sym_db.RegisterMessage(SelectionRequest)

SelectionResponse = _reflection.GeneratedProtocolMessageType('SelectionResponse', (_message.Message,), dict(
  DESCRIPTOR = _SELECTIONRESPONSE,
  __module__ = 'protos.model.v1.intervention_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.SelectionResponse)
  ))
_sym_db.RegisterMessage(SelectionResponse)


DESCRIPTOR._options = None
_INTERVENTIONREQUEST_TAGSENTRY._options = None
# @@protoc_insertion_point(module_scope)