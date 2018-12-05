# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: isolated.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='isolated.proto',
  package='isolated',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0eisolated.proto\x12\x08isolated\x1a\x1fgoogle/protobuf/timestamp.proto\"w\n\x0cStatsRequest\x12*\n\x06latest\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\nresolution\x18\x02 \x01(\x0e\x32\x14.isolated.Resolution\x12\x11\n\tpage_size\x18\x03 \x01(\x05\">\n\rStatsResponse\x12-\n\x0cmeasurements\x18\x01 \x03(\x0b\x32\x17.isolated.StatsSnapshot\"\xe4\x01\n\rStatsSnapshot\x12&\n\x02ts\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07uploads\x18\x02 \x01(\x03\x12\x15\n\ruploads_bytes\x18\x03 \x01(\x03\x12\x11\n\tdownloads\x18\x04 \x01(\x03\x12\x17\n\x0f\x64ownloads_bytes\x18\x05 \x01(\x03\x12\x19\n\x11\x63ontains_requests\x18\x06 \x01(\x03\x12\x18\n\x10\x63ontains_lookups\x18\x07 \x01(\x03\x12\x10\n\x08requests\x18\x08 \x01(\x03\x12\x10\n\x08\x66\x61ilures\x18\t \x01(\x03*G\n\nResolution\x12\x1a\n\x16RESOLUTION_UNSPECIFIED\x10\x00\x12\n\n\x06MINUTE\x10\x01\x12\x08\n\x04HOUR\x10\x02\x12\x07\n\x03\x44\x41Y\x10\x03\x32\x46\n\x08Isolated\x12:\n\x05Stats\x12\x16.isolated.StatsRequest\x1a\x17.isolated.StatsResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_RESOLUTION = _descriptor.EnumDescriptor(
  name='Resolution',
  full_name='isolated.Resolution',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESOLUTION_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MINUTE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOUR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DAY', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=477,
  serialized_end=548,
)
_sym_db.RegisterEnumDescriptor(_RESOLUTION)

Resolution = enum_type_wrapper.EnumTypeWrapper(_RESOLUTION)
RESOLUTION_UNSPECIFIED = 0
MINUTE = 1
HOUR = 2
DAY = 3



_STATSREQUEST = _descriptor.Descriptor(
  name='StatsRequest',
  full_name='isolated.StatsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latest', full_name='isolated.StatsRequest.latest', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resolution', full_name='isolated.StatsRequest.resolution', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='isolated.StatsRequest.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=61,
  serialized_end=180,
)


_STATSRESPONSE = _descriptor.Descriptor(
  name='StatsResponse',
  full_name='isolated.StatsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='measurements', full_name='isolated.StatsResponse.measurements', index=0,
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
  serialized_start=182,
  serialized_end=244,
)


_STATSSNAPSHOT = _descriptor.Descriptor(
  name='StatsSnapshot',
  full_name='isolated.StatsSnapshot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ts', full_name='isolated.StatsSnapshot.ts', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uploads', full_name='isolated.StatsSnapshot.uploads', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uploads_bytes', full_name='isolated.StatsSnapshot.uploads_bytes', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='downloads', full_name='isolated.StatsSnapshot.downloads', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='downloads_bytes', full_name='isolated.StatsSnapshot.downloads_bytes', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contains_requests', full_name='isolated.StatsSnapshot.contains_requests', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contains_lookups', full_name='isolated.StatsSnapshot.contains_lookups', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requests', full_name='isolated.StatsSnapshot.requests', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='failures', full_name='isolated.StatsSnapshot.failures', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=247,
  serialized_end=475,
)

_STATSREQUEST.fields_by_name['latest'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_STATSREQUEST.fields_by_name['resolution'].enum_type = _RESOLUTION
_STATSRESPONSE.fields_by_name['measurements'].message_type = _STATSSNAPSHOT
_STATSSNAPSHOT.fields_by_name['ts'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['StatsRequest'] = _STATSREQUEST
DESCRIPTOR.message_types_by_name['StatsResponse'] = _STATSRESPONSE
DESCRIPTOR.message_types_by_name['StatsSnapshot'] = _STATSSNAPSHOT
DESCRIPTOR.enum_types_by_name['Resolution'] = _RESOLUTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StatsRequest = _reflection.GeneratedProtocolMessageType('StatsRequest', (_message.Message,), dict(
  DESCRIPTOR = _STATSREQUEST,
  __module__ = 'isolated_pb2'
  # @@protoc_insertion_point(class_scope:isolated.StatsRequest)
  ))
_sym_db.RegisterMessage(StatsRequest)

StatsResponse = _reflection.GeneratedProtocolMessageType('StatsResponse', (_message.Message,), dict(
  DESCRIPTOR = _STATSRESPONSE,
  __module__ = 'isolated_pb2'
  # @@protoc_insertion_point(class_scope:isolated.StatsResponse)
  ))
_sym_db.RegisterMessage(StatsResponse)

StatsSnapshot = _reflection.GeneratedProtocolMessageType('StatsSnapshot', (_message.Message,), dict(
  DESCRIPTOR = _STATSSNAPSHOT,
  __module__ = 'isolated_pb2'
  # @@protoc_insertion_point(class_scope:isolated.StatsSnapshot)
  ))
_sym_db.RegisterMessage(StatsSnapshot)



_ISOLATED = _descriptor.ServiceDescriptor(
  name='Isolated',
  full_name='isolated.Isolated',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=550,
  serialized_end=620,
  methods=[
  _descriptor.MethodDescriptor(
    name='Stats',
    full_name='isolated.Isolated.Stats',
    index=0,
    containing_service=None,
    input_type=_STATSREQUEST,
    output_type=_STATSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ISOLATED)

DESCRIPTOR.services_by_name['Isolated'] = _ISOLATED

# @@protoc_insertion_point(module_scope)
