# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: openapiv3/annotations.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..openapiv3 import OpenAPIv3_pb2 as openapiv3_dot_OpenAPIv3__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bopenapiv3/annotations.proto\x12\nopenapi.v3\x1a\x19openapiv3/OpenAPIv3.proto\x1a google/protobuf/descriptor.proto:E\n\x08\x64ocument\x12\x1c.google.protobuf.FileOptions\x18\xf7\x08 \x01(\x0b\x32\x14.openapi.v3.Document:I\n\toperation\x12\x1e.google.protobuf.MethodOptions\x18\xf7\x08 \x01(\x0b\x32\x15.openapi.v3.Operation:D\n\x06schema\x12\x1f.google.protobuf.MessageOptions\x18\xf7\x08 \x01(\x0b\x32\x12.openapi.v3.Schema:D\n\x08property\x12\x1d.google.protobuf.FieldOptions\x18\xf7\x08 \x01(\x0b\x32\x12.openapi.v3.SchemaBZ\n\x0eorg.openapi_v3B\x10\x41nnotationsProtoP\x01Z.github.com/google/gnostic/openapiv3;openapi_v3\xa2\x02\x03OASb\x06proto3')


DOCUMENT_FIELD_NUMBER = 1143
document = DESCRIPTOR.extensions_by_name['document']
OPERATION_FIELD_NUMBER = 1143
operation = DESCRIPTOR.extensions_by_name['operation']
SCHEMA_FIELD_NUMBER = 1143
schema = DESCRIPTOR.extensions_by_name['schema']
PROPERTY_FIELD_NUMBER = 1143
property = DESCRIPTOR.extensions_by_name['property']

if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(document)
  google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(operation)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(schema)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(property)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\016org.openapi_v3B\020AnnotationsProtoP\001Z.github.com/google/gnostic/openapiv3;openapi_v3\242\002\003OAS'
# @@protoc_insertion_point(module_scope)
