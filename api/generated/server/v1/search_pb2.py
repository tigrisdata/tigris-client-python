# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server/v1/search.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ...google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ...openapiv3 import annotations_pb2 as openapiv3_dot_annotations__pb2
from ...server.v1 import observability_pb2 as server_dot_v1_dot_observability__pb2
from ...server.v1 import api_pb2 as server_dot_v1_dot_api__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16server/v1/search.proto\x12\x14tigrisdata.search.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1bopenapiv3/annotations.proto\x1a\x1dserver/v1/observability.proto\x1a\x13server/v1/api.proto\"`\n\x1a\x43reateOrUpdateIndexRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06schema\x18\x03 \x01(\x0c\x12\x13\n\x0bonly_create\x18\x04 \x01(\x08\"?\n\x0bIndexSource\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x12\n\ncollection\x18\x02 \x01(\t\x12\x0e\n\x06\x62ranch\x18\x03 \x01(\t\">\n\x1b\x43reateOrUpdateIndexResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"0\n\x0fGetIndexRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"B\n\x10GetIndexResponse\x12.\n\x05index\x18\x01 \x01(\x0b\x32\x1f.tigrisdata.search.v1.IndexInfo\"3\n\x12\x44\x65leteIndexRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"6\n\x13\x44\x65leteIndexResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"X\n\x12ListIndexesRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\x31\n\x06\x66ilter\x18\x02 \x01(\x0b\x32!.tigrisdata.search.v1.IndexSource\")\n\tIndexInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\x0c\"G\n\x13ListIndexesResponse\x12\x30\n\x07indexes\x18\x01 \x03(\x0b\x32\x1f.tigrisdata.search.v1.IndexInfo\"J\n\tDocStatus\x12\n\n\x02id\x18\x01 \x01(\t\x12\x31\n\x05\x65rror\x18\x03 \x01(\x0b\x32\".tigrisdata.observability.v1.Error\"A\n\x12GetDocumentRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\t\x12\x0b\n\x03ids\x18\x03 \x03(\t\"B\n\x13GetDocumentResponse\x12+\n\tdocuments\x18\x01 \x03(\x0b\x32\x18.tigrisdata.v1.SearchHit\"Q\n\x11\x43reateByIdRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x10\n\x08\x64ocument\x18\x04 \x01(\x0c\" \n\x12\x43reateByIdResponse\x12\n\n\x02id\x18\x01 \x01(\t\"J\n\x15\x43reateDocumentRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\t\x12\x11\n\tdocuments\x18\x03 \x03(\x0c\"I\n\x16\x43reateDocumentResponse\x12/\n\x06status\x18\x01 \x03(\x0b\x32\x1f.tigrisdata.search.v1.DocStatus\"S\n\x1e\x43reateOrReplaceDocumentRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\t\x12\x11\n\tdocuments\x18\x03 \x03(\x0c\"R\n\x1f\x43reateOrReplaceDocumentResponse\x12/\n\x06status\x18\x01 \x03(\x0b\x32\x1f.tigrisdata.search.v1.DocStatus\"J\n\x15UpdateDocumentRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\t\x12\x11\n\tdocuments\x18\x03 \x03(\x0c\"I\n\x16UpdateDocumentResponse\x12/\n\x06status\x18\x01 \x03(\x0b\x32\x1f.tigrisdata.search.v1.DocStatus\"D\n\x15\x44\x65leteDocumentRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\t\x12\x0b\n\x03ids\x18\x03 \x03(\t\"I\n\x16\x44\x65leteDocumentResponse\x12/\n\x06status\x18\x01 \x03(\x0b\x32\x1f.tigrisdata.search.v1.DocStatus\"F\n\x14\x44\x65leteByQueryRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x03 \x01(\x0c\"&\n\x15\x44\x65leteByQueryResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x05\"\xa3\x02\n\x12SearchIndexRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\t\x12\t\n\x01q\x18\x03 \x01(\t\x12\x15\n\rsearch_fields\x18\x04 \x03(\t\x12\x0e\n\x06\x66ilter\x18\x05 \x01(\x0c\x12\r\n\x05\x66\x61\x63\x65t\x18\x06 \x01(\x0c\x12\x0c\n\x04sort\x18\x07 \x01(\x0c\x12\x16\n\x0einclude_fields\x18\x08 \x03(\t\x12\x16\n\x0e\x65xclude_fields\x18\t \x03(\t\x12\x11\n\tpage_size\x18\n \x01(\x05\x12\x0c\n\x04page\x18\x0b \x01(\x05\x12+\n\tcollation\x18\x0c \x01(\x0b\x32\x18.tigrisdata.v1.Collation\x12\x10\n\x08group_by\x18\r \x01(\x0c\x12\x0e\n\x06vector\x18\x0e \x01(\x0c\"\xad\x02\n\x13SearchIndexResponse\x12&\n\x04hits\x18\x01 \x03(\x0b\x32\x18.tigrisdata.v1.SearchHit\x12\x45\n\x06\x66\x61\x63\x65ts\x18\x02 \x03(\x0b\x32\x35.tigrisdata.search.v1.SearchIndexResponse.FacetsEntry\x12+\n\x04meta\x18\x03 \x01(\x0b\x32\x1d.tigrisdata.v1.SearchMetadata\x12/\n\x05group\x18\x04 \x03(\x0b\x32 .tigrisdata.v1.GroupedSearchHits\x1aI\n\x0b\x46\x61\x63\x65tsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b\x32\x1a.tigrisdata.v1.SearchFacet:\x02\x38\x01\x32\xd5\x13\n\x06Search\x12\xdf\x01\n\x13\x43reateOrUpdateIndex\x12\x30.tigrisdata.search.v1.CreateOrUpdateIndexRequest\x1a\x31.tigrisdata.search.v1.CreateOrUpdateIndexResponse\"c\x82\xd3\xe4\x93\x02\x31\x1a,/v1/projects/{project}/search/indexes/{name}:\x01*\xbaG)\n\x06Search\x12\x1f\x43reates or updates search index\x12\xc0\x01\n\x08GetIndex\x12%.tigrisdata.search.v1.GetIndexRequest\x1a&.tigrisdata.search.v1.GetIndexResponse\"e\x82\xd3\xe4\x93\x02.\x12,/v1/projects/{project}/search/indexes/{name}\xbaG.\n\x06Search\x12$Get information about a search index\x12\xbc\x01\n\x0b\x44\x65leteIndex\x12(.tigrisdata.search.v1.DeleteIndexRequest\x1a).tigrisdata.search.v1.DeleteIndexResponse\"X\x82\xd3\xe4\x93\x02\x31*,/v1/projects/{project}/search/indexes/{name}:\x01*\xbaG\x1e\n\x06Search\x12\x14\x44\x65letes search index\x12\xb1\x01\n\x0bListIndexes\x12(.tigrisdata.search.v1.ListIndexesRequest\x1a).tigrisdata.search.v1.ListIndexesResponse\"M\x82\xd3\xe4\x93\x02\'\x12%/v1/projects/{project}/search/indexes\xbaG\x1d\n\x06Search\x12\x13List search indexes\x12\xca\x01\n\x03Get\x12(.tigrisdata.search.v1.GetDocumentRequest\x1a).tigrisdata.search.v1.GetDocumentResponse\"n\x82\xd3\xe4\x93\x02\x39\x12\x37/v1/projects/{project}/search/indexes/{index}/documents\xbaG,\n\x06Search\x12\"Get a single or multiple documents\x12\xcd\x01\n\nCreateById\x12\'.tigrisdata.search.v1.CreateByIdRequest\x1a(.tigrisdata.search.v1.CreateByIdResponse\"l\x82\xd3\xe4\x93\x02\x41\"</v1/projects/{project}/search/indexes/{index}/documents/{id}:\x01*\xbaG\"\n\x06Search\x12\x18\x43reate a single document\x12\xcd\x01\n\x06\x43reate\x12+.tigrisdata.search.v1.CreateDocumentRequest\x1a,.tigrisdata.search.v1.CreateDocumentResponse\"h\x82\xd3\xe4\x93\x02<\"7/v1/projects/{project}/search/indexes/{index}/documents:\x01*\xbaG#\n\x06Search\x12\x19\x43reate multiple documents\x12\xf6\x01\n\x0f\x43reateOrReplace\x12\x34.tigrisdata.search.v1.CreateOrReplaceDocumentRequest\x1a\x35.tigrisdata.search.v1.CreateOrReplaceDocumentResponse\"v\x82\xd3\xe4\x93\x02<\x1a\x37/v1/projects/{project}/search/indexes/{index}/documents:\x01*\xbaG1\n\x06Search\x12\'Create or replace documents in an index\x12\xd0\x01\n\x06Update\x12+.tigrisdata.search.v1.UpdateDocumentRequest\x1a,.tigrisdata.search.v1.UpdateDocumentResponse\"k\x82\xd3\xe4\x93\x02<27/v1/projects/{project}/search/indexes/{index}/documents:\x01*\xbaG&\n\x06Search\x12\x1cUpdate documents in an index\x12\xcb\x01\n\x06\x44\x65lete\x12+.tigrisdata.search.v1.DeleteDocumentRequest\x1a,.tigrisdata.search.v1.DeleteDocumentResponse\"f\x82\xd3\xe4\x93\x02<*7/v1/projects/{project}/search/indexes/{index}/documents:\x01*\xbaG!\n\x06Search\x12\x17\x44\x65lete documents by ids\x12\xe0\x01\n\rDeleteByQuery\x12*.tigrisdata.search.v1.DeleteByQueryRequest\x1a+.tigrisdata.search.v1.DeleteByQueryResponse\"v\x82\xd3\xe4\x93\x02J*E/v1/projects/{project}/search/indexes/{index}/documents/deleteByQuery:\x01*\xbaG#\n\x06Search\x12\x19\x44\x65lete documents by query\x12\xc8\x01\n\x06Search\x12(.tigrisdata.search.v1.SearchIndexRequest\x1a).tigrisdata.search.v1.SearchIndexResponse\"g\x82\xd3\xe4\x93\x02\x43\">/v1/projects/{project}/search/indexes/{index}/documents/search:\x01*\xbaG\x1b\n\x06Search\x12\x11Search Documents.0\x01\x42\x41\n\x1d\x63om.tigrisdata.db.api.v1.grpcZ github.com/tigrisdata/tigris/apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'server.v1.search_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.tigrisdata.db.api.v1.grpcZ github.com/tigrisdata/tigris/api'
  _SEARCHINDEXRESPONSE_FACETSENTRY._options = None
  _SEARCHINDEXRESPONSE_FACETSENTRY._serialized_options = b'8\001'
  _SEARCH.methods_by_name['CreateOrUpdateIndex']._options = None
  _SEARCH.methods_by_name['CreateOrUpdateIndex']._serialized_options = b'\202\323\344\223\0021\032,/v1/projects/{project}/search/indexes/{name}:\001*\272G)\n\006Search\022\037Creates or updates search index'
  _SEARCH.methods_by_name['GetIndex']._options = None
  _SEARCH.methods_by_name['GetIndex']._serialized_options = b'\202\323\344\223\002.\022,/v1/projects/{project}/search/indexes/{name}\272G.\n\006Search\022$Get information about a search index'
  _SEARCH.methods_by_name['DeleteIndex']._options = None
  _SEARCH.methods_by_name['DeleteIndex']._serialized_options = b'\202\323\344\223\0021*,/v1/projects/{project}/search/indexes/{name}:\001*\272G\036\n\006Search\022\024Deletes search index'
  _SEARCH.methods_by_name['ListIndexes']._options = None
  _SEARCH.methods_by_name['ListIndexes']._serialized_options = b'\202\323\344\223\002\'\022%/v1/projects/{project}/search/indexes\272G\035\n\006Search\022\023List search indexes'
  _SEARCH.methods_by_name['Get']._options = None
  _SEARCH.methods_by_name['Get']._serialized_options = b'\202\323\344\223\0029\0227/v1/projects/{project}/search/indexes/{index}/documents\272G,\n\006Search\022\"Get a single or multiple documents'
  _SEARCH.methods_by_name['CreateById']._options = None
  _SEARCH.methods_by_name['CreateById']._serialized_options = b'\202\323\344\223\002A\"</v1/projects/{project}/search/indexes/{index}/documents/{id}:\001*\272G\"\n\006Search\022\030Create a single document'
  _SEARCH.methods_by_name['Create']._options = None
  _SEARCH.methods_by_name['Create']._serialized_options = b'\202\323\344\223\002<\"7/v1/projects/{project}/search/indexes/{index}/documents:\001*\272G#\n\006Search\022\031Create multiple documents'
  _SEARCH.methods_by_name['CreateOrReplace']._options = None
  _SEARCH.methods_by_name['CreateOrReplace']._serialized_options = b'\202\323\344\223\002<\0327/v1/projects/{project}/search/indexes/{index}/documents:\001*\272G1\n\006Search\022\'Create or replace documents in an index'
  _SEARCH.methods_by_name['Update']._options = None
  _SEARCH.methods_by_name['Update']._serialized_options = b'\202\323\344\223\002<27/v1/projects/{project}/search/indexes/{index}/documents:\001*\272G&\n\006Search\022\034Update documents in an index'
  _SEARCH.methods_by_name['Delete']._options = None
  _SEARCH.methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002<*7/v1/projects/{project}/search/indexes/{index}/documents:\001*\272G!\n\006Search\022\027Delete documents by ids'
  _SEARCH.methods_by_name['DeleteByQuery']._options = None
  _SEARCH.methods_by_name['DeleteByQuery']._serialized_options = b'\202\323\344\223\002J*E/v1/projects/{project}/search/indexes/{index}/documents/deleteByQuery:\001*\272G#\n\006Search\022\031Delete documents by query'
  _SEARCH.methods_by_name['Search']._options = None
  _SEARCH.methods_by_name['Search']._serialized_options = b'\202\323\344\223\002C\">/v1/projects/{project}/search/indexes/{index}/documents/search:\001*\272G\033\n\006Search\022\021Search Documents.'
  _CREATEORUPDATEINDEXREQUEST._serialized_start=159
  _CREATEORUPDATEINDEXREQUEST._serialized_end=255
  _INDEXSOURCE._serialized_start=257
  _INDEXSOURCE._serialized_end=320
  _CREATEORUPDATEINDEXRESPONSE._serialized_start=322
  _CREATEORUPDATEINDEXRESPONSE._serialized_end=384
  _GETINDEXREQUEST._serialized_start=386
  _GETINDEXREQUEST._serialized_end=434
  _GETINDEXRESPONSE._serialized_start=436
  _GETINDEXRESPONSE._serialized_end=502
  _DELETEINDEXREQUEST._serialized_start=504
  _DELETEINDEXREQUEST._serialized_end=555
  _DELETEINDEXRESPONSE._serialized_start=557
  _DELETEINDEXRESPONSE._serialized_end=611
  _LISTINDEXESREQUEST._serialized_start=613
  _LISTINDEXESREQUEST._serialized_end=701
  _INDEXINFO._serialized_start=703
  _INDEXINFO._serialized_end=744
  _LISTINDEXESRESPONSE._serialized_start=746
  _LISTINDEXESRESPONSE._serialized_end=817
  _DOCSTATUS._serialized_start=819
  _DOCSTATUS._serialized_end=893
  _GETDOCUMENTREQUEST._serialized_start=895
  _GETDOCUMENTREQUEST._serialized_end=960
  _GETDOCUMENTRESPONSE._serialized_start=962
  _GETDOCUMENTRESPONSE._serialized_end=1028
  _CREATEBYIDREQUEST._serialized_start=1030
  _CREATEBYIDREQUEST._serialized_end=1111
  _CREATEBYIDRESPONSE._serialized_start=1113
  _CREATEBYIDRESPONSE._serialized_end=1145
  _CREATEDOCUMENTREQUEST._serialized_start=1147
  _CREATEDOCUMENTREQUEST._serialized_end=1221
  _CREATEDOCUMENTRESPONSE._serialized_start=1223
  _CREATEDOCUMENTRESPONSE._serialized_end=1296
  _CREATEORREPLACEDOCUMENTREQUEST._serialized_start=1298
  _CREATEORREPLACEDOCUMENTREQUEST._serialized_end=1381
  _CREATEORREPLACEDOCUMENTRESPONSE._serialized_start=1383
  _CREATEORREPLACEDOCUMENTRESPONSE._serialized_end=1465
  _UPDATEDOCUMENTREQUEST._serialized_start=1467
  _UPDATEDOCUMENTREQUEST._serialized_end=1541
  _UPDATEDOCUMENTRESPONSE._serialized_start=1543
  _UPDATEDOCUMENTRESPONSE._serialized_end=1616
  _DELETEDOCUMENTREQUEST._serialized_start=1618
  _DELETEDOCUMENTREQUEST._serialized_end=1686
  _DELETEDOCUMENTRESPONSE._serialized_start=1688
  _DELETEDOCUMENTRESPONSE._serialized_end=1761
  _DELETEBYQUERYREQUEST._serialized_start=1763
  _DELETEBYQUERYREQUEST._serialized_end=1833
  _DELETEBYQUERYRESPONSE._serialized_start=1835
  _DELETEBYQUERYRESPONSE._serialized_end=1873
  _SEARCHINDEXREQUEST._serialized_start=1876
  _SEARCHINDEXREQUEST._serialized_end=2167
  _SEARCHINDEXRESPONSE._serialized_start=2170
  _SEARCHINDEXRESPONSE._serialized_end=2471
  _SEARCHINDEXRESPONSE_FACETSENTRY._serialized_start=2398
  _SEARCHINDEXRESPONSE_FACETSENTRY._serialized_end=2471
  _SEARCH._serialized_start=2474
  _SEARCH._serialized_end=4991
# @@protoc_insertion_point(module_scope)