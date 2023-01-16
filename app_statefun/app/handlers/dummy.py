from app.adapters.stateful_functions import stateful_functions
from app.schemas import FUNCTION_STRING_TYPE
from statefun import Context, Message, StringType, message_builder

from .typename import DUMMY, NORMALIZATION


@stateful_functions.bind(DUMMY)
def custom_process_logger(context: Context, message: Message) -> None:
    incoming_message = message.as_type(FUNCTION_STRING_TYPE)
    print(incoming_message)
    request = incoming_message
    context.send(
        message_builder(
            target_typename=NORMALIZATION,
            target_id=context.address.id,
            value=request,
            value_type=StringType,
        )
    )
