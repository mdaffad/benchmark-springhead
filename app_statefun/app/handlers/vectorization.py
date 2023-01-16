from collections import Counter

from app.adapters.stateful_functions import stateful_functions
from app.schemas import (
    FUNCTION_DFS_VALUE_SPEC,
    FUNCTION_GENERAL_DICTIONARY_TYPE,
    FUNCTION_N_DOCUMENT_VALUE_SPEC,
)
from river.feature_extraction import TFIDF as RiverTFIDF
from statefun import Context, Message, StringType, message_builder

from .typename import CLUSTREAM, TFIDF


@stateful_functions.bind(
    TFIDF, [FUNCTION_N_DOCUMENT_VALUE_SPEC, FUNCTION_DFS_VALUE_SPEC]
)
def tfidf(context: Context, message: Message) -> None:  # noqa
    document_counter = context.storage.dfs or {}
    document_number = context.storage.n or 0

    tfidf = RiverTFIDF()
    if document_counter:
        tfidf.dfs = Counter(document_counter)
        tfidf.n = document_number
    text = message.as_type(StringType)

    tfidf = tfidf.learn_one(text)

    # Update docs storage
    dfs = tfidf.dfs
    n = tfidf.n
    context.storage.dfs = dict(dfs)
    context.storage.n = n

    tfidf = tfidf.transform_one(text)
    request = {
        "vectorized_value": tfidf,
    }
    context.send(
        message_builder(
            target_typename=CLUSTREAM,
            target_id=context.address.id,
            value=request,
            value_type=FUNCTION_GENERAL_DICTIONARY_TYPE,
        )
    )
