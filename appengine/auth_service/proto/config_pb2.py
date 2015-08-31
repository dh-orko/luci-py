# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='config.proto',
  package='auth_service',
  serialized_pb='\n\x0c\x63onfig.proto\x12\x0c\x61uth_service\"\xd3\x02\n\x13GroupImporterConfig\x12?\n\x07tarball\x18\x01 \x03(\x0b\x32..auth_service.GroupImporterConfig.TarballEntry\x12\x43\n\tplainlist\x18\x02 \x03(\x0b\x32\x30.auth_service.GroupImporterConfig.PlainlistEntry\x1a\x62\n\x0cTarballEntry\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x14\n\x0coauth_scopes\x18\x02 \x03(\t\x12\x0e\n\x06\x64omain\x18\x03 \x01(\t\x12\x0f\n\x07systems\x18\x04 \x03(\t\x12\x0e\n\x06groups\x18\x05 \x03(\t\x1aR\n\x0ePlainlistEntry\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x14\n\x0coauth_scopes\x18\x02 \x03(\t\x12\x0e\n\x06\x64omain\x18\x03 \x01(\t\x12\r\n\x05group\x18\x04 \x01(\t\"[\n\x0bOAuthConfig\x12\x19\n\x11primary_client_id\x18\x01 \x01(\t\x12\x1d\n\x15primary_client_secret\x18\x02 \x01(\t\x12\x12\n\nclient_ids\x18\x03 \x03(\t\"\x81\x02\n\x11IPWhitelistConfig\x12\x42\n\rip_whitelists\x18\x01 \x03(\x0b\x32+.auth_service.IPWhitelistConfig.IPWhitelist\x12?\n\x0b\x61ssignments\x18\x02 \x03(\x0b\x32*.auth_service.IPWhitelistConfig.Assignment\x1a,\n\x0bIPWhitelist\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07subnets\x18\x02 \x03(\t\x1a\x39\n\nAssignment\x12\x10\n\x08identity\x18\x01 \x01(\t\x12\x19\n\x11ip_whitelist_name\x18\x02 \x01(\t\"\xb6\x01\n\x10\x44\x65legationConfig\x12\x32\n\x05rules\x18\x01 \x03(\x0b\x32#.auth_service.DelegationConfig.Rule\x1an\n\x04Rule\x12\x0f\n\x07user_id\x18\x01 \x03(\t\x12\x16\n\x0etarget_service\x18\x02 \x03(\t\x12\x1d\n\x15max_validity_duration\x18\x03 \x01(\x05\x12\x1e\n\x16\x61llowed_to_impersonate\x18\x04 \x03(\t')




_GROUPIMPORTERCONFIG_TARBALLENTRY = _descriptor.Descriptor(
  name='TarballEntry',
  full_name='auth_service.GroupImporterConfig.TarballEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='auth_service.GroupImporterConfig.TarballEntry.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='oauth_scopes', full_name='auth_service.GroupImporterConfig.TarballEntry.oauth_scopes', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domain', full_name='auth_service.GroupImporterConfig.TarballEntry.domain', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='systems', full_name='auth_service.GroupImporterConfig.TarballEntry.systems', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='groups', full_name='auth_service.GroupImporterConfig.TarballEntry.groups', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=188,
  serialized_end=286,
)

_GROUPIMPORTERCONFIG_PLAINLISTENTRY = _descriptor.Descriptor(
  name='PlainlistEntry',
  full_name='auth_service.GroupImporterConfig.PlainlistEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='auth_service.GroupImporterConfig.PlainlistEntry.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='oauth_scopes', full_name='auth_service.GroupImporterConfig.PlainlistEntry.oauth_scopes', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domain', full_name='auth_service.GroupImporterConfig.PlainlistEntry.domain', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group', full_name='auth_service.GroupImporterConfig.PlainlistEntry.group', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=288,
  serialized_end=370,
)

_GROUPIMPORTERCONFIG = _descriptor.Descriptor(
  name='GroupImporterConfig',
  full_name='auth_service.GroupImporterConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tarball', full_name='auth_service.GroupImporterConfig.tarball', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='plainlist', full_name='auth_service.GroupImporterConfig.plainlist', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GROUPIMPORTERCONFIG_TARBALLENTRY, _GROUPIMPORTERCONFIG_PLAINLISTENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=31,
  serialized_end=370,
)


_OAUTHCONFIG = _descriptor.Descriptor(
  name='OAuthConfig',
  full_name='auth_service.OAuthConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='primary_client_id', full_name='auth_service.OAuthConfig.primary_client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='primary_client_secret', full_name='auth_service.OAuthConfig.primary_client_secret', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_ids', full_name='auth_service.OAuthConfig.client_ids', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=372,
  serialized_end=463,
)


_IPWHITELISTCONFIG_IPWHITELIST = _descriptor.Descriptor(
  name='IPWhitelist',
  full_name='auth_service.IPWhitelistConfig.IPWhitelist',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='auth_service.IPWhitelistConfig.IPWhitelist.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subnets', full_name='auth_service.IPWhitelistConfig.IPWhitelist.subnets', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=620,
  serialized_end=664,
)

_IPWHITELISTCONFIG_ASSIGNMENT = _descriptor.Descriptor(
  name='Assignment',
  full_name='auth_service.IPWhitelistConfig.Assignment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identity', full_name='auth_service.IPWhitelistConfig.Assignment.identity', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip_whitelist_name', full_name='auth_service.IPWhitelistConfig.Assignment.ip_whitelist_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=666,
  serialized_end=723,
)

_IPWHITELISTCONFIG = _descriptor.Descriptor(
  name='IPWhitelistConfig',
  full_name='auth_service.IPWhitelistConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_whitelists', full_name='auth_service.IPWhitelistConfig.ip_whitelists', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='assignments', full_name='auth_service.IPWhitelistConfig.assignments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_IPWHITELISTCONFIG_IPWHITELIST, _IPWHITELISTCONFIG_ASSIGNMENT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=466,
  serialized_end=723,
)


_DELEGATIONCONFIG_RULE = _descriptor.Descriptor(
  name='Rule',
  full_name='auth_service.DelegationConfig.Rule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='auth_service.DelegationConfig.Rule.user_id', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target_service', full_name='auth_service.DelegationConfig.Rule.target_service', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_validity_duration', full_name='auth_service.DelegationConfig.Rule.max_validity_duration', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='allowed_to_impersonate', full_name='auth_service.DelegationConfig.Rule.allowed_to_impersonate', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=798,
  serialized_end=908,
)

_DELEGATIONCONFIG = _descriptor.Descriptor(
  name='DelegationConfig',
  full_name='auth_service.DelegationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rules', full_name='auth_service.DelegationConfig.rules', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DELEGATIONCONFIG_RULE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=726,
  serialized_end=908,
)

_GROUPIMPORTERCONFIG_TARBALLENTRY.containing_type = _GROUPIMPORTERCONFIG;
_GROUPIMPORTERCONFIG_PLAINLISTENTRY.containing_type = _GROUPIMPORTERCONFIG;
_GROUPIMPORTERCONFIG.fields_by_name['tarball'].message_type = _GROUPIMPORTERCONFIG_TARBALLENTRY
_GROUPIMPORTERCONFIG.fields_by_name['plainlist'].message_type = _GROUPIMPORTERCONFIG_PLAINLISTENTRY
_IPWHITELISTCONFIG_IPWHITELIST.containing_type = _IPWHITELISTCONFIG;
_IPWHITELISTCONFIG_ASSIGNMENT.containing_type = _IPWHITELISTCONFIG;
_IPWHITELISTCONFIG.fields_by_name['ip_whitelists'].message_type = _IPWHITELISTCONFIG_IPWHITELIST
_IPWHITELISTCONFIG.fields_by_name['assignments'].message_type = _IPWHITELISTCONFIG_ASSIGNMENT
_DELEGATIONCONFIG_RULE.containing_type = _DELEGATIONCONFIG;
_DELEGATIONCONFIG.fields_by_name['rules'].message_type = _DELEGATIONCONFIG_RULE
DESCRIPTOR.message_types_by_name['GroupImporterConfig'] = _GROUPIMPORTERCONFIG
DESCRIPTOR.message_types_by_name['OAuthConfig'] = _OAUTHCONFIG
DESCRIPTOR.message_types_by_name['IPWhitelistConfig'] = _IPWHITELISTCONFIG
DESCRIPTOR.message_types_by_name['DelegationConfig'] = _DELEGATIONCONFIG

class GroupImporterConfig(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class TarballEntry(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _GROUPIMPORTERCONFIG_TARBALLENTRY

    # @@protoc_insertion_point(class_scope:auth_service.GroupImporterConfig.TarballEntry)

  class PlainlistEntry(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _GROUPIMPORTERCONFIG_PLAINLISTENTRY

    # @@protoc_insertion_point(class_scope:auth_service.GroupImporterConfig.PlainlistEntry)
  DESCRIPTOR = _GROUPIMPORTERCONFIG

  # @@protoc_insertion_point(class_scope:auth_service.GroupImporterConfig)

class OAuthConfig(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OAUTHCONFIG

  # @@protoc_insertion_point(class_scope:auth_service.OAuthConfig)

class IPWhitelistConfig(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class IPWhitelist(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _IPWHITELISTCONFIG_IPWHITELIST

    # @@protoc_insertion_point(class_scope:auth_service.IPWhitelistConfig.IPWhitelist)

  class Assignment(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _IPWHITELISTCONFIG_ASSIGNMENT

    # @@protoc_insertion_point(class_scope:auth_service.IPWhitelistConfig.Assignment)
  DESCRIPTOR = _IPWHITELISTCONFIG

  # @@protoc_insertion_point(class_scope:auth_service.IPWhitelistConfig)

class DelegationConfig(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Rule(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _DELEGATIONCONFIG_RULE

    # @@protoc_insertion_point(class_scope:auth_service.DelegationConfig.Rule)
  DESCRIPTOR = _DELEGATIONCONFIG

  # @@protoc_insertion_point(class_scope:auth_service.DelegationConfig)


# @@protoc_insertion_point(module_scope)
