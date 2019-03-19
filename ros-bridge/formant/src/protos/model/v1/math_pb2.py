# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/model/v1/math.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/model/v1/math.proto',
  package='v1.model',
  syntax='proto3',
  serialized_options=_b('Z)github.com/FormantIO/genproto/go/v1/model'),
  serialized_pb=_b('\n\x1aprotos/model/v1/math.proto\x12\x08v1.model\"\x18\n\x07Numeric\x12\r\n\x05value\x18\x01 \x01(\x01\".\n\tMetricSet\x12!\n\x07metrics\x18\x01 \x03(\x0b\x32\x10.v1.model.Metric\"%\n\x06Metric\x12\r\n\x05value\x18\x01 \x01(\x01\x12\x0c\n\x04unit\x18\x02 \x01(\t\"!\n\x03\x42it\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08\"%\n\x06\x42itSet\x12\x1b\n\x04\x62its\x18\x01 \x03(\x0b\x32\r.v1.model.Bit\"N\n\x05Twist\x12!\n\x06linear\x18\x01 \x01(\x0b\x32\x11.v1.model.Vector3\x12\"\n\x07\x61ngular\x18\x02 \x01(\x0b\x32\x11.v1.model.Vector3\"[\n\tTransform\x12&\n\x0btranslation\x18\x01 \x01(\x0b\x32\x11.v1.model.Vector3\x12&\n\x08rotation\x18\x02 \x01(\x0b\x32\x14.v1.model.Quaternion\"*\n\x07Vector3\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\"8\n\nQuaternion\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\t\n\x01w\x18\x04 \x01(\x01\x42+Z)github.com/FormantIO/genproto/go/v1/modelb\x06proto3')
)




_NUMERIC = _descriptor.Descriptor(
  name='Numeric',
  full_name='v1.model.Numeric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.model.Numeric.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=40,
  serialized_end=64,
)


_METRICSET = _descriptor.Descriptor(
  name='MetricSet',
  full_name='v1.model.MetricSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics', full_name='v1.model.MetricSet.metrics', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=66,
  serialized_end=112,
)


_METRIC = _descriptor.Descriptor(
  name='Metric',
  full_name='v1.model.Metric',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.model.Metric.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit', full_name='v1.model.Metric.unit', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=114,
  serialized_end=151,
)


_BIT = _descriptor.Descriptor(
  name='Bit',
  full_name='v1.model.Bit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v1.model.Bit.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.model.Bit.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=153,
  serialized_end=186,
)


_BITSET = _descriptor.Descriptor(
  name='BitSet',
  full_name='v1.model.BitSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bits', full_name='v1.model.BitSet.bits', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=188,
  serialized_end=225,
)


_TWIST = _descriptor.Descriptor(
  name='Twist',
  full_name='v1.model.Twist',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='linear', full_name='v1.model.Twist.linear', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='angular', full_name='v1.model.Twist.angular', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=227,
  serialized_end=305,
)


_TRANSFORM = _descriptor.Descriptor(
  name='Transform',
  full_name='v1.model.Transform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='translation', full_name='v1.model.Transform.translation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='v1.model.Transform.rotation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=307,
  serialized_end=398,
)


_VECTOR3 = _descriptor.Descriptor(
  name='Vector3',
  full_name='v1.model.Vector3',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='v1.model.Vector3.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='v1.model.Vector3.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='v1.model.Vector3.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=400,
  serialized_end=442,
)


_QUATERNION = _descriptor.Descriptor(
  name='Quaternion',
  full_name='v1.model.Quaternion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='v1.model.Quaternion.x', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='v1.model.Quaternion.y', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='v1.model.Quaternion.z', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='w', full_name='v1.model.Quaternion.w', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=444,
  serialized_end=500,
)

_METRICSET.fields_by_name['metrics'].message_type = _METRIC
_BITSET.fields_by_name['bits'].message_type = _BIT
_TWIST.fields_by_name['linear'].message_type = _VECTOR3
_TWIST.fields_by_name['angular'].message_type = _VECTOR3
_TRANSFORM.fields_by_name['translation'].message_type = _VECTOR3
_TRANSFORM.fields_by_name['rotation'].message_type = _QUATERNION
DESCRIPTOR.message_types_by_name['Numeric'] = _NUMERIC
DESCRIPTOR.message_types_by_name['MetricSet'] = _METRICSET
DESCRIPTOR.message_types_by_name['Metric'] = _METRIC
DESCRIPTOR.message_types_by_name['Bit'] = _BIT
DESCRIPTOR.message_types_by_name['BitSet'] = _BITSET
DESCRIPTOR.message_types_by_name['Twist'] = _TWIST
DESCRIPTOR.message_types_by_name['Transform'] = _TRANSFORM
DESCRIPTOR.message_types_by_name['Vector3'] = _VECTOR3
DESCRIPTOR.message_types_by_name['Quaternion'] = _QUATERNION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Numeric = _reflection.GeneratedProtocolMessageType('Numeric', (_message.Message,), dict(
  DESCRIPTOR = _NUMERIC,
  __module__ = 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Numeric)
  ))
_sym_db.RegisterMessage(Numeric)

MetricSet = _reflection.GeneratedProtocolMessageType('MetricSet', (_message.Message,), dict(
  DESCRIPTOR = _METRICSET,
  __module__ = 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.MetricSet)
  ))
_sym_db.RegisterMessage(MetricSet)

Metric = _reflection.GeneratedProtocolMessageType('Metric', (_message.Message,), dict(
  DESCRIPTOR = _METRIC,
  __module__ = 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Metric)
  ))
_sym_db.RegisterMessage(Metric)

Bit = _reflection.GeneratedProtocolMessageType('Bit', (_message.Message,), dict(
  DESCRIPTOR = _BIT,
  __module__ = 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Bit)
  ))
_sym_db.RegisterMessage(Bit)

BitSet = _reflection.GeneratedProtocolMessageType('BitSet', (_message.Message,), dict(
  DESCRIPTOR = _BITSET,
  __module__ = 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.BitSet)
  ))
_sym_db.RegisterMessage(BitSet)

Twist = _reflection.GeneratedProtocolMessageType('Twist', (_message.Message,), dict(
  DESCRIPTOR = _TWIST,
  __module__ = 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Twist)
  ))
_sym_db.RegisterMessage(Twist)

Transform = _reflection.GeneratedProtocolMessageType('Transform', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFORM,
  __module__ = 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Transform)
  ))
_sym_db.RegisterMessage(Transform)

Vector3 = _reflection.GeneratedProtocolMessageType('Vector3', (_message.Message,), dict(
  DESCRIPTOR = _VECTOR3,
  __module__ = 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Vector3)
  ))
_sym_db.RegisterMessage(Vector3)

Quaternion = _reflection.GeneratedProtocolMessageType('Quaternion', (_message.Message,), dict(
  DESCRIPTOR = _QUATERNION,
  __module__ = 'protos.model.v1.math_pb2'
  # @@protoc_insertion_point(class_scope:v1.model.Quaternion)
  ))
_sym_db.RegisterMessage(Quaternion)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
