# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='protobuf/message.proto',
  package='message',
  serialized_pb='\n\x16protobuf/message.proto\x12\x07message\"\xc7\x01\n\x06Header\x12\x16\n\x0emessage_length\x18\x01 \x02(\r\x12\x41\n\x12hmac_hash_function\x18\x03 \x01(\x0e\x32 .message.Header.HmacHashFunction:\x03MD5\x12\x13\n\x0bhmac_signer\x18\x04 \x01(\t\x12\x18\n\x10hmac_key_version\x18\x05 \x01(\r\x12\x0c\n\x04hmac\x18\x06 \x01(\x0c\"%\n\x10HmacHashFunction\x12\x07\n\x03MD5\x10\x00\x12\x08\n\x04SHA1\x10\x01\"\xa2\x02\n\x05\x46ield\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x34\n\nvalue_type\x18\x02 \x01(\x0e\x32\x18.message.Field.ValueType:\x06STRING\x12\x16\n\x0erepresentation\x18\x03 \x01(\t\x12\x14\n\x0cvalue_string\x18\x04 \x03(\t\x12\x13\n\x0bvalue_bytes\x18\x05 \x03(\x0c\x12\x19\n\rvalue_integer\x18\x06 \x03(\x03\x42\x02\x10\x01\x12\x18\n\x0cvalue_double\x18\x07 \x03(\x01\x42\x02\x10\x01\x12\x16\n\nvalue_bool\x18\x08 \x03(\x08\x42\x02\x10\x01\"E\n\tValueType\x12\n\n\x06STRING\x10\x00\x12\t\n\x05\x42YTES\x10\x01\x12\x0b\n\x07INTEGER\x10\x02\x12\n\n\x06\x44OUBLE\x10\x03\x12\x08\n\x04\x42OOL\x10\x04\"\xbf\x01\n\x07Message\x12\x0c\n\x04uuid\x18\x01 \x02(\x0c\x12\x11\n\ttimestamp\x18\x02 \x02(\x03\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0e\n\x06logger\x18\x04 \x01(\t\x12\x10\n\x08severity\x18\x05 \x01(\x05\x12\x0f\n\x07payload\x18\x06 \x01(\t\x12\x13\n\x0b\x65nv_version\x18\x07 \x01(\t\x12\x0b\n\x03pid\x18\x08 \x01(\x05\x12\x10\n\x08hostname\x18\t \x01(\t\x12\x1e\n\x06\x66ields\x18\n \x03(\x0b\x32\x0e.message.Field')



_HEADER_HMACHASHFUNCTION = descriptor.EnumDescriptor(
  name='HmacHashFunction',
  full_name='message.Header.HmacHashFunction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='MD5', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SHA1', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=198,
  serialized_end=235,
)

_FIELD_VALUETYPE = descriptor.EnumDescriptor(
  name='ValueType',
  full_name='message.Field.ValueType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='STRING', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='BYTES', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='INTEGER', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='DOUBLE', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='BOOL', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=459,
  serialized_end=528,
)


_HEADER = descriptor.Descriptor(
  name='Header',
  full_name='message.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='message_length', full_name='message.Header.message_length', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hmac_hash_function', full_name='message.Header.hmac_hash_function', index=1,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hmac_signer', full_name='message.Header.hmac_signer', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hmac_key_version', full_name='message.Header.hmac_key_version', index=3,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hmac', full_name='message.Header.hmac', index=4,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _HEADER_HMACHASHFUNCTION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=36,
  serialized_end=235,
)


_FIELD = descriptor.Descriptor(
  name='Field',
  full_name='message.Field',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='message.Field.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value_type', full_name='message.Field.value_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='representation', full_name='message.Field.representation', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value_string', full_name='message.Field.value_string', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value_bytes', full_name='message.Field.value_bytes', index=4,
      number=5, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value_integer', full_name='message.Field.value_integer', index=5,
      number=6, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='value_double', full_name='message.Field.value_double', index=6,
      number=7, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='value_bool', full_name='message.Field.value_bool', index=7,
      number=8, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FIELD_VALUETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=238,
  serialized_end=528,
)


_MESSAGE = descriptor.Descriptor(
  name='Message',
  full_name='message.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='uuid', full_name='message.Message.uuid', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timestamp', full_name='message.Message.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='message.Message.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='logger', full_name='message.Message.logger', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='severity', full_name='message.Message.severity', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='payload', full_name='message.Message.payload', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='env_version', full_name='message.Message.env_version', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='pid', full_name='message.Message.pid', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hostname', full_name='message.Message.hostname', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fields', full_name='message.Message.fields', index=9,
      number=10, type=11, cpp_type=10, label=3,
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
  serialized_start=531,
  serialized_end=722,
)

_HEADER.fields_by_name['hmac_hash_function'].enum_type = _HEADER_HMACHASHFUNCTION
_HEADER_HMACHASHFUNCTION.containing_type = _HEADER;
_FIELD.fields_by_name['value_type'].enum_type = _FIELD_VALUETYPE
_FIELD_VALUETYPE.containing_type = _FIELD;
_MESSAGE.fields_by_name['fields'].message_type = _FIELD
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['Field'] = _FIELD
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE

class Header(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _HEADER
  
  # @@protoc_insertion_point(class_scope:message.Header)

class Field(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FIELD
  
  # @@protoc_insertion_point(class_scope:message.Field)

class Message(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MESSAGE
  
  # @@protoc_insertion_point(class_scope:message.Message)

# @@protoc_insertion_point(module_scope)
