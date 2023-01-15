import logging

from app.adapters.stateful_functions import stateful_functions
from river.cluster import CluStream
from statefun import Context, Message

logger = logging.getLogger(__name__)


@stateful_functions
def clustream(context: Context, message: Message, process: Process) -> None:  # noqa
    clustream = context.storage.clustream or None
    if not clustream:
        clustream = clustream = CluStream(
            n_macro_clusters=3, max_micro_clusters=5, time_gap=3, seed=0, halflife=0.4
        )

    message = message.as_type(process.source_type_value)
    message = message["vectorized_value"]
    try:
        clustream = clustream.learn_one(message)
    except Exception as e:
        logger.error(str(e))
        return

    # Update storage
    context.storage.clustream = clustream

    predict = None
    try:
        predict = clustream.predict_one(message)
    except Exception as e:
        logger.error(str(e))

    request = {
        "predict": predict,
        "centers": clustream.centers,
    }

    process.send(target_id=process.target_id, value=request, context=context)
