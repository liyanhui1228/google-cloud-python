# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/bigquery/storage_v1beta1/proto/avro.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/bigquery/storage_v1beta1/proto/avro.proto",
    package="google.cloud.bigquery.storage.v1beta1",
    syntax="proto3",
    serialized_pb=_b(
        '\n6google/cloud/bigquery/storage_v1beta1/proto/avro.proto\x12%google.cloud.bigquery.storage.v1beta1"\x1c\n\nAvroSchema\x12\x0e\n\x06schema\x18\x01 \x01(\t"=\n\x08\x41vroRows\x12\x1e\n\x16serialized_binary_rows\x18\x01 \x01(\x0c\x12\x11\n\trow_count\x18\x02 \x01(\x03\x42\x84\x01\n)com.google.cloud.bigquery.storage.v1beta1B\tAvroProtoZLgoogle.golang.org/genproto/googleapis/cloud/bigquery/storage/v1beta1;storageb\x06proto3'
    ),
)


_AVROSCHEMA = _descriptor.Descriptor(
    name="AvroSchema",
    full_name="google.cloud.bigquery.storage.v1beta1.AvroSchema",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="schema",
            full_name="google.cloud.bigquery.storage.v1beta1.AvroSchema.schema",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=97,
    serialized_end=125,
)


_AVROROWS = _descriptor.Descriptor(
    name="AvroRows",
    full_name="google.cloud.bigquery.storage.v1beta1.AvroRows",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="serialized_binary_rows",
            full_name="google.cloud.bigquery.storage.v1beta1.AvroRows.serialized_binary_rows",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="row_count",
            full_name="google.cloud.bigquery.storage.v1beta1.AvroRows.row_count",
            index=1,
            number=2,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=127,
    serialized_end=188,
)

DESCRIPTOR.message_types_by_name["AvroSchema"] = _AVROSCHEMA
DESCRIPTOR.message_types_by_name["AvroRows"] = _AVROROWS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AvroSchema = _reflection.GeneratedProtocolMessageType(
    "AvroSchema",
    (_message.Message,),
    dict(
        DESCRIPTOR=_AVROSCHEMA,
        __module__="google.cloud.bigquery.storage_v1beta1.proto.avro_pb2",
        __doc__="""Avro schema.
  
  
  Attributes:
      schema:
          Json serialized schema, as described at
          https://avro.apache.org/docs/1.8.1/spec.html
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.bigquery.storage.v1beta1.AvroSchema)
    ),
)
_sym_db.RegisterMessage(AvroSchema)

AvroRows = _reflection.GeneratedProtocolMessageType(
    "AvroRows",
    (_message.Message,),
    dict(
        DESCRIPTOR=_AVROROWS,
        __module__="google.cloud.bigquery.storage_v1beta1.proto.avro_pb2",
        __doc__="""Avro rows.
  
  
  Attributes:
      serialized_binary_rows:
          Binary serialized rows in a block.
      row_count:
          The count of rows in the returning block.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.bigquery.storage.v1beta1.AvroRows)
    ),
)
_sym_db.RegisterMessage(AvroRows)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(
    descriptor_pb2.FileOptions(),
    _b(
        "\n)com.google.cloud.bigquery.storage.v1beta1B\tAvroProtoZLgoogle.golang.org/genproto/googleapis/cloud/bigquery/storage/v1beta1;storage"
    ),
)
# @@protoc_insertion_point(module_scope)
