from statefun import make_json_type, simple_type


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
