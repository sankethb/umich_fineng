# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tick.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tick.proto',
  package='ncllc.protos',
  serialized_pb='\n\ntick.proto\x12\x0cncllc.protos\"\x8c\x02\n\x04Tick\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x0c\n\x04last\x18\x02 \x01(\x01\x12\x10\n\x08lastSize\x18\x03 \x01(\x03\x12\x13\n\x0btotalVolume\x18\x04 \x01(\x03\x12\x0b\n\x03\x62id\x18\x05 \x01(\x01\x12\x0b\n\x03\x61sk\x18\x06 \x01(\x01\x12\x0e\n\x06tickId\x18\x07 \x01(\x03\x12\x0f\n\x07\x62idSize\x18\x08 \x01(\x03\x12\x0f\n\x07\x61skSize\x18\t \x01(\x03\x12\x14\n\x0c\x62\x61sisForLast\x18\n \x01(\t\x12\x30\n\x0ctickPosition\x18\x0b \x01(\x0e\x32\x1a.ncllc.protos.TickPosition\x12\x12\n\ninstrument\x18\x0c \x01(\t\x12\x14\n\x0ctimestampStr\x18\r \x01(\t\"v\n\nOptionMeta\x12,\n\noptionType\x18\x01 \x01(\x0e\x32\x18.ncllc.protos.OptionType\x12\x16\n\x0e\x65xpirationDate\x18\x02 \x01(\x03\x12\x0e\n\x06strike\x18\x04 \x01(\x01\x12\x12\n\ninstrument\x18\x05 \x01(\t\"\xcf\x01\n\nPairedTick\x12&\n\noptionTick\x18\x01 \x01(\x0b\x32\x12.ncllc.protos.Tick\x12*\n\x0eunderlyingTick\x18\x02 \x01(\x0b\x32\x12.ncllc.protos.Tick\x12,\n\noptionMeta\x18\x03 \x01(\x0b\x32\x18.ncllc.protos.OptionMeta\x12\x14\n\x0cinterestRate\x18\x04 \x01(\x01\x12\x14\n\x0c\x64\x61ysToExpire\x18\x05 \x01(\x03\x12\x13\n\x0bisPriceable\x18\x06 \x01(\x08\"\x1b\n\x02Id\x12\x15\n\rnumDataPoints\x18\x06 \x01(\x05\"I\n\x0bTheoretical\x12\x1c\n\x02Id\x18\x01 \x01(\x0b\x32\x10.ncllc.protos.Id\x12\r\n\x05price\x18\x02 \x01(\x01\x12\r\n\x05\x64\x65lta\x18\x03 \x01(\x01\"m\n\x0cPricedRecord\x12,\n\npairedTick\x18\x01 \x01(\x0b\x32\x18.ncllc.protos.PairedTick\x12/\n\x0ctheoreticals\x18\x02 \x03(\x0b\x32\x19.ncllc.protos.Theoretical*\x1f\n\nOptionType\x12\x08\n\x04\x43\x41LL\x10\x01\x12\x07\n\x03PUT\x10\x02*.\n\x0cTickPosition\x12\t\n\x05START\x10\x01\x12\x07\n\x03\x45ND\x10\x02\x12\n\n\x06\x41\x43TIVE\x10\x03\x42\x1a\n\x10\x63om.ncllc.protosB\x06Protos')

_OPTIONTYPE = _descriptor.EnumDescriptor(
  name='OptionType',
  full_name='ncllc.protos.OptionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CALL', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PUT', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=844,
  serialized_end=875,
)

OptionType = enum_type_wrapper.EnumTypeWrapper(_OPTIONTYPE)
_TICKPOSITION = _descriptor.EnumDescriptor(
  name='TickPosition',
  full_name='ncllc.protos.TickPosition',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='START', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='END', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=877,
  serialized_end=923,
)

TickPosition = enum_type_wrapper.EnumTypeWrapper(_TICKPOSITION)
CALL = 1
PUT = 2
START = 1
END = 2
ACTIVE = 3



_TICK = _descriptor.Descriptor(
  name='Tick',
  full_name='ncllc.protos.Tick',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ncllc.protos.Tick.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last', full_name='ncllc.protos.Tick.last', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastSize', full_name='ncllc.protos.Tick.lastSize', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='totalVolume', full_name='ncllc.protos.Tick.totalVolume', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid', full_name='ncllc.protos.Tick.bid', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask', full_name='ncllc.protos.Tick.ask', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tickId', full_name='ncllc.protos.Tick.tickId', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bidSize', full_name='ncllc.protos.Tick.bidSize', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='askSize', full_name='ncllc.protos.Tick.askSize', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basisForLast', full_name='ncllc.protos.Tick.basisForLast', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tickPosition', full_name='ncllc.protos.Tick.tickPosition', index=10,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instrument', full_name='ncllc.protos.Tick.instrument', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestampStr', full_name='ncllc.protos.Tick.timestampStr', index=12,
      number=13, type=9, cpp_type=9, label=1,
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
  serialized_start=29,
  serialized_end=297,
)


_OPTIONMETA = _descriptor.Descriptor(
  name='OptionMeta',
  full_name='ncllc.protos.OptionMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='optionType', full_name='ncllc.protos.OptionMeta.optionType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expirationDate', full_name='ncllc.protos.OptionMeta.expirationDate', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strike', full_name='ncllc.protos.OptionMeta.strike', index=2,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='instrument', full_name='ncllc.protos.OptionMeta.instrument', index=3,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=299,
  serialized_end=417,
)


_PAIREDTICK = _descriptor.Descriptor(
  name='PairedTick',
  full_name='ncllc.protos.PairedTick',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='optionTick', full_name='ncllc.protos.PairedTick.optionTick', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='underlyingTick', full_name='ncllc.protos.PairedTick.underlyingTick', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='optionMeta', full_name='ncllc.protos.PairedTick.optionMeta', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interestRate', full_name='ncllc.protos.PairedTick.interestRate', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='daysToExpire', full_name='ncllc.protos.PairedTick.daysToExpire', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='isPriceable', full_name='ncllc.protos.PairedTick.isPriceable', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=420,
  serialized_end=627,
)


_ID = _descriptor.Descriptor(
  name='Id',
  full_name='ncllc.protos.Id',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numDataPoints', full_name='ncllc.protos.Id.numDataPoints', index=0,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=629,
  serialized_end=656,
)


_THEORETICAL = _descriptor.Descriptor(
  name='Theoretical',
  full_name='ncllc.protos.Theoretical',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='ncllc.protos.Theoretical.Id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='ncllc.protos.Theoretical.price', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delta', full_name='ncllc.protos.Theoretical.delta', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=658,
  serialized_end=731,
)


_PRICEDRECORD = _descriptor.Descriptor(
  name='PricedRecord',
  full_name='ncllc.protos.PricedRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pairedTick', full_name='ncllc.protos.PricedRecord.pairedTick', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='theoreticals', full_name='ncllc.protos.PricedRecord.theoreticals', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=733,
  serialized_end=842,
)

_TICK.fields_by_name['tickPosition'].enum_type = _TICKPOSITION
_OPTIONMETA.fields_by_name['optionType'].enum_type = _OPTIONTYPE
_PAIREDTICK.fields_by_name['optionTick'].message_type = _TICK
_PAIREDTICK.fields_by_name['underlyingTick'].message_type = _TICK
_PAIREDTICK.fields_by_name['optionMeta'].message_type = _OPTIONMETA
_THEORETICAL.fields_by_name['Id'].message_type = _ID
_PRICEDRECORD.fields_by_name['pairedTick'].message_type = _PAIREDTICK
_PRICEDRECORD.fields_by_name['theoreticals'].message_type = _THEORETICAL
DESCRIPTOR.message_types_by_name['Tick'] = _TICK
DESCRIPTOR.message_types_by_name['OptionMeta'] = _OPTIONMETA
DESCRIPTOR.message_types_by_name['PairedTick'] = _PAIREDTICK
DESCRIPTOR.message_types_by_name['Id'] = _ID
DESCRIPTOR.message_types_by_name['Theoretical'] = _THEORETICAL
DESCRIPTOR.message_types_by_name['PricedRecord'] = _PRICEDRECORD

class Tick(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TICK

  # @@protoc_insertion_point(class_scope:ncllc.protos.Tick)

class OptionMeta(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _OPTIONMETA

  # @@protoc_insertion_point(class_scope:ncllc.protos.OptionMeta)

class PairedTick(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PAIREDTICK

  # @@protoc_insertion_point(class_scope:ncllc.protos.PairedTick)

class Id(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ID

  # @@protoc_insertion_point(class_scope:ncllc.protos.Id)

class Theoretical(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _THEORETICAL

  # @@protoc_insertion_point(class_scope:ncllc.protos.Theoretical)

class PricedRecord(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PRICEDRECORD

  # @@protoc_insertion_point(class_scope:ncllc.protos.PricedRecord)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), '\n\020com.ncllc.protosB\006Protos')
# @@protoc_insertion_point(module_scope)
