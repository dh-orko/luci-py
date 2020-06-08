# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import realms_pb2 as realms__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='config.proto',
  package='swarming.config',
  syntax='proto3',
  serialized_options=b'Z3go.chromium.org/luci/swarming/proto/config;configpb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x63onfig.proto\x12\x0fswarming.config\x1a\x0crealms.proto\"\xf3\x04\n\x0bSettingsCfg\x12\x18\n\x10google_analytics\x18\x01 \x01(\t\x12\x1e\n\x16reusable_task_age_secs\x18\x02 \x01(\x05\x12\x1e\n\x16\x62ot_death_timeout_secs\x18\x03 \x01(\x05\x12\x1c\n\x14\x65nable_ts_monitoring\x18\x04 \x01(\x08\x12\x31\n\x07isolate\x18\x05 \x01(\x0b\x32 .swarming.config.IsolateSettings\x12+\n\x04\x63ipd\x18\x06 \x01(\x0b\x32\x1d.swarming.config.CipdSettings\x12,\n$force_bots_to_sleep_and_not_run_task\x18\x08 \x01(\x08\x12\x14\n\x0cui_client_id\x18\t \x01(\t\x12#\n\x1b\x64isplay_server_url_template\x18\x0b \x01(\t\x12\x1a\n\x12max_bot_sleep_time\x18\x0c \x01(\x05\x12+\n\x04\x61uth\x18\r \x01(\x0b\x32\x1d.swarming.config.AuthSettings\x12\x1e\n\x16\x62ot_isolate_grpc_proxy\x18\x0e \x01(\t\x12\x1f\n\x17\x62ot_swarming_grpc_proxy\x18\x0f \x01(\t\x12\x1f\n\x17\x65xtra_child_src_csp_url\x18\x10 \x03(\t\x12\x10\n\x08use_lifo\x18\x11 \x01(\x08\x12%\n\x1d\x65nable_batch_es_notifications\x18\x12 \x01(\x08\x12\x33\n\x08resultdb\x18\x13 \x01(\x0b\x32!.swarming.config.ResultDBSettingsJ\x04\x08\x07\x10\x08J\x04\x08\n\x10\x0b\"D\n\x0fIsolateSettings\x12\x16\n\x0e\x64\x65\x66\x61ult_server\x18\x01 \x01(\t\x12\x19\n\x11\x64\x65\x66\x61ult_namespace\x18\x02 \x01(\t\"4\n\x0b\x43ipdPackage\x12\x14\n\x0cpackage_name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"d\n\x0c\x43ipdSettings\x12\x16\n\x0e\x64\x65\x66\x61ult_server\x18\x01 \x01(\t\x12<\n\x16\x64\x65\x66\x61ult_client_package\x18\x02 \x01(\x0b\x32\x1c.swarming.config.CipdPackage\"\xf7\x01\n\x0c\x41uthSettings\x12\x14\n\x0c\x61\x64mins_group\x18\x01 \x01(\t\x12\x1b\n\x13\x62ot_bootstrap_group\x18\x02 \x01(\t\x12\x1e\n\x16privileged_users_group\x18\x03 \x01(\t\x12\x13\n\x0busers_group\x18\x04 \x01(\t\x12\x1b\n\x13view_all_bots_group\x18\x05 \x01(\t\x12\x1c\n\x14view_all_tasks_group\x18\x06 \x01(\t\x12\x44\n\x1a\x65nforced_realm_permissions\x18\x07 \x03(\x0e\x32 .swarming.config.RealmPermission\"\"\n\x10ResultDBSettings\x12\x0e\n\x06server\x18\x01 \x01(\tB5Z3go.chromium.org/luci/swarming/proto/config;configpbb\x06proto3'
  ,
  dependencies=[realms__pb2.DESCRIPTOR,])




_SETTINGSCFG = _descriptor.Descriptor(
  name='SettingsCfg',
  full_name='swarming.config.SettingsCfg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='google_analytics', full_name='swarming.config.SettingsCfg.google_analytics', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reusable_task_age_secs', full_name='swarming.config.SettingsCfg.reusable_task_age_secs', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bot_death_timeout_secs', full_name='swarming.config.SettingsCfg.bot_death_timeout_secs', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_ts_monitoring', full_name='swarming.config.SettingsCfg.enable_ts_monitoring', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isolate', full_name='swarming.config.SettingsCfg.isolate', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cipd', full_name='swarming.config.SettingsCfg.cipd', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='force_bots_to_sleep_and_not_run_task', full_name='swarming.config.SettingsCfg.force_bots_to_sleep_and_not_run_task', index=6,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ui_client_id', full_name='swarming.config.SettingsCfg.ui_client_id', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_server_url_template', full_name='swarming.config.SettingsCfg.display_server_url_template', index=8,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_bot_sleep_time', full_name='swarming.config.SettingsCfg.max_bot_sleep_time', index=9,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='auth', full_name='swarming.config.SettingsCfg.auth', index=10,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bot_isolate_grpc_proxy', full_name='swarming.config.SettingsCfg.bot_isolate_grpc_proxy', index=11,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bot_swarming_grpc_proxy', full_name='swarming.config.SettingsCfg.bot_swarming_grpc_proxy', index=12,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra_child_src_csp_url', full_name='swarming.config.SettingsCfg.extra_child_src_csp_url', index=13,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_lifo', full_name='swarming.config.SettingsCfg.use_lifo', index=14,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enable_batch_es_notifications', full_name='swarming.config.SettingsCfg.enable_batch_es_notifications', index=15,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resultdb', full_name='swarming.config.SettingsCfg.resultdb', index=16,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=48,
  serialized_end=675,
)


_ISOLATESETTINGS = _descriptor.Descriptor(
  name='IsolateSettings',
  full_name='swarming.config.IsolateSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='default_server', full_name='swarming.config.IsolateSettings.default_server', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_namespace', full_name='swarming.config.IsolateSettings.default_namespace', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=677,
  serialized_end=745,
)


_CIPDPACKAGE = _descriptor.Descriptor(
  name='CipdPackage',
  full_name='swarming.config.CipdPackage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='package_name', full_name='swarming.config.CipdPackage.package_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='swarming.config.CipdPackage.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=747,
  serialized_end=799,
)


_CIPDSETTINGS = _descriptor.Descriptor(
  name='CipdSettings',
  full_name='swarming.config.CipdSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='default_server', full_name='swarming.config.CipdSettings.default_server', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='default_client_package', full_name='swarming.config.CipdSettings.default_client_package', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=801,
  serialized_end=901,
)


_AUTHSETTINGS = _descriptor.Descriptor(
  name='AuthSettings',
  full_name='swarming.config.AuthSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='admins_group', full_name='swarming.config.AuthSettings.admins_group', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bot_bootstrap_group', full_name='swarming.config.AuthSettings.bot_bootstrap_group', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='privileged_users_group', full_name='swarming.config.AuthSettings.privileged_users_group', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='users_group', full_name='swarming.config.AuthSettings.users_group', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='view_all_bots_group', full_name='swarming.config.AuthSettings.view_all_bots_group', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='view_all_tasks_group', full_name='swarming.config.AuthSettings.view_all_tasks_group', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enforced_realm_permissions', full_name='swarming.config.AuthSettings.enforced_realm_permissions', index=6,
      number=7, type=14, cpp_type=8, label=3,
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
  serialized_start=904,
  serialized_end=1151,
)


_RESULTDBSETTINGS = _descriptor.Descriptor(
  name='ResultDBSettings',
  full_name='swarming.config.ResultDBSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='server', full_name='swarming.config.ResultDBSettings.server', index=0,
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
  serialized_start=1153,
  serialized_end=1187,
)

_SETTINGSCFG.fields_by_name['isolate'].message_type = _ISOLATESETTINGS
_SETTINGSCFG.fields_by_name['cipd'].message_type = _CIPDSETTINGS
_SETTINGSCFG.fields_by_name['auth'].message_type = _AUTHSETTINGS
_SETTINGSCFG.fields_by_name['resultdb'].message_type = _RESULTDBSETTINGS
_CIPDSETTINGS.fields_by_name['default_client_package'].message_type = _CIPDPACKAGE
_AUTHSETTINGS.fields_by_name['enforced_realm_permissions'].enum_type = realms__pb2._REALMPERMISSION
DESCRIPTOR.message_types_by_name['SettingsCfg'] = _SETTINGSCFG
DESCRIPTOR.message_types_by_name['IsolateSettings'] = _ISOLATESETTINGS
DESCRIPTOR.message_types_by_name['CipdPackage'] = _CIPDPACKAGE
DESCRIPTOR.message_types_by_name['CipdSettings'] = _CIPDSETTINGS
DESCRIPTOR.message_types_by_name['AuthSettings'] = _AUTHSETTINGS
DESCRIPTOR.message_types_by_name['ResultDBSettings'] = _RESULTDBSETTINGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SettingsCfg = _reflection.GeneratedProtocolMessageType('SettingsCfg', (_message.Message,), {
  'DESCRIPTOR' : _SETTINGSCFG,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:swarming.config.SettingsCfg)
  })
_sym_db.RegisterMessage(SettingsCfg)

IsolateSettings = _reflection.GeneratedProtocolMessageType('IsolateSettings', (_message.Message,), {
  'DESCRIPTOR' : _ISOLATESETTINGS,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:swarming.config.IsolateSettings)
  })
_sym_db.RegisterMessage(IsolateSettings)

CipdPackage = _reflection.GeneratedProtocolMessageType('CipdPackage', (_message.Message,), {
  'DESCRIPTOR' : _CIPDPACKAGE,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:swarming.config.CipdPackage)
  })
_sym_db.RegisterMessage(CipdPackage)

CipdSettings = _reflection.GeneratedProtocolMessageType('CipdSettings', (_message.Message,), {
  'DESCRIPTOR' : _CIPDSETTINGS,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:swarming.config.CipdSettings)
  })
_sym_db.RegisterMessage(CipdSettings)

AuthSettings = _reflection.GeneratedProtocolMessageType('AuthSettings', (_message.Message,), {
  'DESCRIPTOR' : _AUTHSETTINGS,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:swarming.config.AuthSettings)
  })
_sym_db.RegisterMessage(AuthSettings)

ResultDBSettings = _reflection.GeneratedProtocolMessageType('ResultDBSettings', (_message.Message,), {
  'DESCRIPTOR' : _RESULTDBSETTINGS,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:swarming.config.ResultDBSettings)
  })
_sym_db.RegisterMessage(ResultDBSettings)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
