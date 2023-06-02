# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server/v1/auth.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ...openapiv3 import annotations_pb2 as openapiv3_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14server/v1/auth.proto\x12\x12tigrisdata.auth.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1bopenapiv3/annotations.proto\"\x8b\x01\n\x15GetAccessTokenRequest\x12\x31\n\ngrant_type\x18\x01 \x01(\x0e\x32\x1d.tigrisdata.auth.v1.GrantType\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x11\n\tclient_id\x18\x03 \x01(\t\x12\x15\n\rclient_secret\x18\x04 \x01(\t\"Y\n\x16GetAccessTokenResponse\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\x12\x12\n\nexpires_in\x18\x03 \x01(\x05\"N\n\x0eInvitationInfo\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0c\n\x04role\x18\x02 \x01(\t\x12\x1f\n\x17invitation_sent_by_name\x18\x03 \x01(\t\"S\n\x18\x43reateInvitationsRequest\x12\x37\n\x0binvitations\x18\x01 \x03(\x0b\x32\".tigrisdata.auth.v1.InvitationInfo\"\x1b\n\x19\x43reateInvitationsResponse\"I\n\x18\x44\x65leteInvitationsRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x13\n\x06status\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_status\"\x1b\n\x19\x44\x65leteInvitationsResponse\"\xb8\x01\n\nInvitation\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0c\n\x04role\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x18\n\x10tigris_namespace\x18\x04 \x01(\t\x12\x1d\n\x15tigris_namespace_name\x18\x05 \x01(\t\x12\x12\n\ncreated_by\x18\x06 \x01(\t\x12\x17\n\x0f\x63reated_by_name\x18\x07 \x01(\t\x12\x17\n\x0f\x65xpiration_time\x18\x08 \x01(\x03\"8\n\x16ListInvitationsRequest\x12\x13\n\x06status\x18\x01 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_status\"N\n\x17ListInvitationsResponse\x12\x33\n\x0binvitations\x18\x01 \x03(\x0b\x32\x1e.tigrisdata.auth.v1.Invitation\"6\n\x17VerifyInvitationRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\"a\n\x18VerifyInvitationResponse\x12\x18\n\x10tigris_namespace\x18\x01 \x01(\t\x12\x1d\n\x15tigris_namespace_name\x18\x02 \x01(\t\x12\x0c\n\x04role\x18\x03 \x01(\t\"\x12\n\x10ListUsersRequest\"<\n\x11ListUsersResponse\x12\'\n\x05users\x18\x01 \x03(\x0b\x32\x18.tigrisdata.auth.v1.User\"V\n\x04User\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\ncreated_at\x18\x03 \x01(\x03\x12\x0f\n\x07picture\x18\x04 \x01(\t\x12\x0c\n\x04role\x18\x05 \x01(\t*6\n\tGrantType\x12\x11\n\rREFRESH_TOKEN\x10\x00\x12\x16\n\x12\x43LIENT_CREDENTIALS\x10\x01\x32\xc0\t\n\x04\x41uth\x12\xa3\x01\n\x0eGetAccessToken\x12).tigrisdata.auth.v1.GetAccessTokenRequest\x1a*.tigrisdata.auth.v1.GetAccessTokenResponse\":\x82\xd3\xe4\x93\x02\x13\"\x0e/v1/auth/token:\x01*\xbaG\x1e\n\x0e\x41uthentication\x12\x0c\x41\x63\x63\x65ss Token\x12\xdc\x01\n\x11\x43reateInvitations\x12,.tigrisdata.auth.v1.CreateInvitationsRequest\x1a-.tigrisdata.auth.v1.CreateInvitationsResponse\"j\x82\xd3\xe4\x93\x02*\"%/v1/auth/namespace/invitations/create:\x01*\xbaG7\n\nManagement\x12)Creates invitations to join the namespace\x12\xdc\x01\n\x11\x44\x65leteInvitations\x12,.tigrisdata.auth.v1.DeleteInvitationsRequest\x1a-.tigrisdata.auth.v1.DeleteInvitationsResponse\"j\x82\xd3\xe4\x93\x02**%/v1/auth/namespace/invitations/delete:\x01*\xbaG7\n\nManagement\x12)Deletes invitations to join the namespace\x12\xd7\x01\n\x0fListInvitations\x12*.tigrisdata.auth.v1.ListInvitationsRequest\x1a+.tigrisdata.auth.v1.ListInvitationsResponse\"k\x82\xd3\xe4\x93\x02%\x12#/v1/auth/namespace/invitations/list\xbaG=\n\nManagement\x12/Lists all the invitations to join the namespace\x12\xc7\x01\n\x10VerifyInvitation\x12+.tigrisdata.auth.v1.VerifyInvitationRequest\x1a,.tigrisdata.auth.v1.VerifyInvitationResponse\"X\x82\xd3\xe4\x93\x02*\"%/v1/auth/namespace/invitations/verify:\x01*\xbaG%\n\nManagement\x12\x17Verifies the invitation\x12\xaf\x01\n\tListUsers\x12$.tigrisdata.auth.v1.ListUsersRequest\x1a%.tigrisdata.auth.v1.ListUsersResponse\"U\x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/auth/namespace/users\xbaG2\n\nManagement\x12$Lists the users in current namespaceBA\n\x1d\x63om.tigrisdata.db.api.v1.grpcZ github.com/tigrisdata/tigris/apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'server.v1.auth_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.tigrisdata.db.api.v1.grpcZ github.com/tigrisdata/tigris/api'
  _AUTH.methods_by_name['GetAccessToken']._options = None
  _AUTH.methods_by_name['GetAccessToken']._serialized_options = b'\202\323\344\223\002\023\"\016/v1/auth/token:\001*\272G\036\n\016Authentication\022\014Access Token'
  _AUTH.methods_by_name['CreateInvitations']._options = None
  _AUTH.methods_by_name['CreateInvitations']._serialized_options = b'\202\323\344\223\002*\"%/v1/auth/namespace/invitations/create:\001*\272G7\n\nManagement\022)Creates invitations to join the namespace'
  _AUTH.methods_by_name['DeleteInvitations']._options = None
  _AUTH.methods_by_name['DeleteInvitations']._serialized_options = b'\202\323\344\223\002**%/v1/auth/namespace/invitations/delete:\001*\272G7\n\nManagement\022)Deletes invitations to join the namespace'
  _AUTH.methods_by_name['ListInvitations']._options = None
  _AUTH.methods_by_name['ListInvitations']._serialized_options = b'\202\323\344\223\002%\022#/v1/auth/namespace/invitations/list\272G=\n\nManagement\022/Lists all the invitations to join the namespace'
  _AUTH.methods_by_name['VerifyInvitation']._options = None
  _AUTH.methods_by_name['VerifyInvitation']._serialized_options = b'\202\323\344\223\002*\"%/v1/auth/namespace/invitations/verify:\001*\272G%\n\nManagement\022\027Verifies the invitation'
  _AUTH.methods_by_name['ListUsers']._options = None
  _AUTH.methods_by_name['ListUsers']._serialized_options = b'\202\323\344\223\002\032\022\030/v1/auth/namespace/users\272G2\n\nManagement\022$Lists the users in current namespace'
  _GRANTTYPE._serialized_start=1284
  _GRANTTYPE._serialized_end=1338
  _GETACCESSTOKENREQUEST._serialized_start=104
  _GETACCESSTOKENREQUEST._serialized_end=243
  _GETACCESSTOKENRESPONSE._serialized_start=245
  _GETACCESSTOKENRESPONSE._serialized_end=334
  _INVITATIONINFO._serialized_start=336
  _INVITATIONINFO._serialized_end=414
  _CREATEINVITATIONSREQUEST._serialized_start=416
  _CREATEINVITATIONSREQUEST._serialized_end=499
  _CREATEINVITATIONSRESPONSE._serialized_start=501
  _CREATEINVITATIONSRESPONSE._serialized_end=528
  _DELETEINVITATIONSREQUEST._serialized_start=530
  _DELETEINVITATIONSREQUEST._serialized_end=603
  _DELETEINVITATIONSRESPONSE._serialized_start=605
  _DELETEINVITATIONSRESPONSE._serialized_end=632
  _INVITATION._serialized_start=635
  _INVITATION._serialized_end=819
  _LISTINVITATIONSREQUEST._serialized_start=821
  _LISTINVITATIONSREQUEST._serialized_end=877
  _LISTINVITATIONSRESPONSE._serialized_start=879
  _LISTINVITATIONSRESPONSE._serialized_end=957
  _VERIFYINVITATIONREQUEST._serialized_start=959
  _VERIFYINVITATIONREQUEST._serialized_end=1013
  _VERIFYINVITATIONRESPONSE._serialized_start=1015
  _VERIFYINVITATIONRESPONSE._serialized_end=1112
  _LISTUSERSREQUEST._serialized_start=1114
  _LISTUSERSREQUEST._serialized_end=1132
  _LISTUSERSRESPONSE._serialized_start=1134
  _LISTUSERSRESPONSE._serialized_end=1194
  _USER._serialized_start=1196
  _USER._serialized_end=1282
  _AUTH._serialized_start=1341
  _AUTH._serialized_end=2557
# @@protoc_insertion_point(module_scope)