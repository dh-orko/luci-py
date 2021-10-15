# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/config/bots.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/config/bots.proto',
  package='swarming.config',
  syntax='proto3',
  serialized_options=b'Z3go.chromium.org/luci/swarming/proto/config;configpb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17proto/config/bots.proto\x12\x0fswarming.config\"S\n\x07\x42otsCfg\x12\x1a\n\x12trusted_dimensions\x18\x01 \x03(\t\x12,\n\tbot_group\x18\x02 \x03(\x0b\x32\x19.swarming.config.BotGroup\"\x80\x02\n\x08\x42otGroup\x12\x0e\n\x06\x62ot_id\x18\x01 \x03(\t\x12\x15\n\rbot_id_prefix\x18\x02 \x03(\t\x12&\n\x04\x61uth\x18\x14 \x03(\x0b\x32\x18.swarming.config.BotAuth\x12\x0e\n\x06owners\x18\x15 \x03(\t\x12\x12\n\ndimensions\x18\x16 \x03(\t\x12\x19\n\x11\x62ot_config_script\x18\x17 \x01(\t\x12\x1d\n\x15\x62ot_config_script_rev\x18\x1a \x01(\t\x12!\n\x19\x62ot_config_script_content\x18\x19 \x01(\x0c\x12\x1e\n\x16system_service_account\x18\x18 \x01(\tJ\x04\x08\x03\x10\x04\"\xcf\x01\n\x07\x42otAuth\x12\x15\n\rlog_if_failed\x18\x05 \x01(\x08\x12\"\n\x1arequire_luci_machine_token\x18\x01 \x01(\x08\x12\x1f\n\x17require_service_account\x18\x02 \x03(\t\x12:\n\x14require_gce_vm_token\x18\x04 \x01(\x0b\x32\x1c.swarming.config.BotAuth.GCE\x12\x14\n\x0cip_whitelist\x18\x03 \x01(\t\x1a\x16\n\x03GCE\x12\x0f\n\x07project\x18\x01 \x01(\tB5Z3go.chromium.org/luci/swarming/proto/config;configpbb\x06proto3'
)




_BOTSCFG = _descriptor.Descriptor(
  name='BotsCfg',
  full_name='swarming.config.BotsCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='trusted_dimensions', full_name='swarming.config.BotsCfg.trusted_dimensions', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bot_group', full_name='swarming.config.BotsCfg.bot_group', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=44,
  serialized_end=127,
)


_BOTGROUP = _descriptor.Descriptor(
  name='BotGroup',
  full_name='swarming.config.BotGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bot_id', full_name='swarming.config.BotGroup.bot_id', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bot_id_prefix', full_name='swarming.config.BotGroup.bot_id_prefix', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auth', full_name='swarming.config.BotGroup.auth', index=2,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owners', full_name='swarming.config.BotGroup.owners', index=3,
      number=21, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dimensions', full_name='swarming.config.BotGroup.dimensions', index=4,
      number=22, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bot_config_script', full_name='swarming.config.BotGroup.bot_config_script', index=5,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bot_config_script_rev', full_name='swarming.config.BotGroup.bot_config_script_rev', index=6,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bot_config_script_content', full_name='swarming.config.BotGroup.bot_config_script_content', index=7,
      number=25, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='system_service_account', full_name='swarming.config.BotGroup.system_service_account', index=8,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=130,
  serialized_end=386,
)


_BOTAUTH_GCE = _descriptor.Descriptor(
  name='GCE',
  full_name='swarming.config.BotAuth.GCE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='project', full_name='swarming.config.BotAuth.GCE.project', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=574,
  serialized_end=596,
)

_BOTAUTH = _descriptor.Descriptor(
  name='BotAuth',
  full_name='swarming.config.BotAuth',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_if_failed', full_name='swarming.config.BotAuth.log_if_failed', index=0,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='require_luci_machine_token', full_name='swarming.config.BotAuth.require_luci_machine_token', index=1,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='require_service_account', full_name='swarming.config.BotAuth.require_service_account', index=2,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='require_gce_vm_token', full_name='swarming.config.BotAuth.require_gce_vm_token', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip_whitelist', full_name='swarming.config.BotAuth.ip_whitelist', index=4,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BOTAUTH_GCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=389,
  serialized_end=596,
)

_BOTSCFG.fields_by_name['bot_group'].message_type = _BOTGROUP
_BOTGROUP.fields_by_name['auth'].message_type = _BOTAUTH
_BOTAUTH_GCE.containing_type = _BOTAUTH
_BOTAUTH.fields_by_name['require_gce_vm_token'].message_type = _BOTAUTH_GCE
DESCRIPTOR.message_types_by_name['BotsCfg'] = _BOTSCFG
DESCRIPTOR.message_types_by_name['BotGroup'] = _BOTGROUP
DESCRIPTOR.message_types_by_name['BotAuth'] = _BOTAUTH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BotsCfg = _reflection.GeneratedProtocolMessageType('BotsCfg', (_message.Message,), {
  'DESCRIPTOR' : _BOTSCFG,
  '__module__' : 'proto.config.bots_pb2'
  # @@protoc_insertion_point(class_scope:swarming.config.BotsCfg)
  })
_sym_db.RegisterMessage(BotsCfg)

BotGroup = _reflection.GeneratedProtocolMessageType('BotGroup', (_message.Message,), {
  'DESCRIPTOR' : _BOTGROUP,
  '__module__' : 'proto.config.bots_pb2'
  # @@protoc_insertion_point(class_scope:swarming.config.BotGroup)
  })
_sym_db.RegisterMessage(BotGroup)

BotAuth = _reflection.GeneratedProtocolMessageType('BotAuth', (_message.Message,), {

  'GCE' : _reflection.GeneratedProtocolMessageType('GCE', (_message.Message,), {
    'DESCRIPTOR' : _BOTAUTH_GCE,
    '__module__' : 'proto.config.bots_pb2'
    # @@protoc_insertion_point(class_scope:swarming.config.BotAuth.GCE)
    })
  ,
  'DESCRIPTOR' : _BOTAUTH,
  '__module__' : 'proto.config.bots_pb2'
  # @@protoc_insertion_point(class_scope:swarming.config.BotAuth)
  })
_sym_db.RegisterMessage(BotAuth)
_sym_db.RegisterMessage(BotAuth.GCE)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
