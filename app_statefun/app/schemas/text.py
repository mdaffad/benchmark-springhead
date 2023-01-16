from pickle import dumps, loads

from statefun import IntType, ValueSpec, make_json_type, simple_type


def serialize_to_utf_8(value: str):
    return value.encode("utf-8")


def deserialize_to_utf_8(value):
    return value.decode("utf-8")


FUNCTION_STRING_TYPE = simple_type(
    typename="function/string",
    serialize_fn=serialize_to_utf_8,
    deserialize_fn=deserialize_to_utf_8,
)

FUNCTION_TEXT_EGRESS_RECORD_TYPE = make_json_type(typename="function/egress")
FUNCTION_DFS_TYPE = make_json_type(typename="function/tfidf")
FUNCTION_CLUSTREAM_TYPE = simple_type(
    typename="function/clustream",
    serialize_fn=dumps,
    deserialize_fn=loads,
)


FUNCTION_DFS_VALUE_SPEC = ValueSpec(name="dfs", type=FUNCTION_DFS_TYPE)
FUNCTION_CLUSTREAM_VALUE_SPEC = ValueSpec(
    name="clustream", type=FUNCTION_CLUSTREAM_TYPE
)

FUNCTION_N_DOCUMENT_VALUE_SPEC = ValueSpec(name="n", type=IntType)

FUNCTION_GENERAL_DICTIONARY_TYPE = make_json_type(typename="function/dictionary")
