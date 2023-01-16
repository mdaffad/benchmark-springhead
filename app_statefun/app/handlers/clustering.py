import logging

from app.adapters.stateful_functions import stateful_functions
from app.schemas import (
    FUNCTION_CLUSTREAM_VALUE_SPEC,
    FUNCTION_GENERAL_DICTIONARY_TYPE,
    FUNCTION_TEXT_EGRESS_RECORD_TYPE,
)
from river.cluster import CluStream
from statefun import Context, Message, kafka_egress_message

from .typename import CLUSTREAM

logger = logging.getLogger(__name__)


@stateful_functions.bind(CLUSTREAM, [FUNCTION_CLUSTREAM_VALUE_SPEC])
def clustream(context: Context, message: Message) -> None:  # noqa
    clustream = context.storage.clustream or None
    if not clustream:
        clustream = clustream = CluStream(
            n_macro_clusters=3, max_micro_clusters=5, time_gap=3, seed=0, halflife=0.4
        )

    message = message.as_type(FUNCTION_GENERAL_DICTIONARY_TYPE)
    message = message["vectorized_value"]
    try:
        clustream = clustream.learn_one(message)
    except Exception:
        # logger.error(str(e))
        return

    # Update storage
    context.storage.clustream = clustream

    predict = None
    try:
        predict = clustream.predict_one(message)
    except Exception:
        return

    request = {
        "predict": predict,
        "centers": clustream.centers,
    }

    context.send_egress(
        kafka_egress_message(
            typename="function/kafka-egress",
            topic="cluster",
            value=request,
            value_type=FUNCTION_TEXT_EGRESS_RECORD_TYPE,
        )
    )
