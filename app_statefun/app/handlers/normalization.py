import unicodedata

import nltk
from app.adapters.stateful_functions import stateful_functions
from app.schemas import FUNCTION_STRING_TYPE
from nltk.tokenize import word_tokenize
from statefun import Context, Message, StringType, kafka_egress_message

from .typename import NORMALIZATION

stopwords = set(nltk.corpus.stopwords.words("english"))
lemmatizer = nltk.stem.WordNetLemmatizer()


def is_punct(token):
    return all(unicodedata.category(char).startswith("P") for char in token)


def is_stopword(token):
    return token.lower() in stopwords


def lemmatize(token):
    return lemmatizer.lemmatize(token)


@stateful_functions.bind(NORMALIZATION)
def normalize(context: Context, message: Message) -> None:
    text: str = message.as_type(FUNCTION_STRING_TYPE)
    normalized_text = [
        lemmatize(word).lower()
        for word in word_tokenize(text)
        if not is_punct(word) and not is_stopword(word)
    ]
    normalized_text = " ".join(normalized_text)
    context.send_egress(
        kafka_egress_message(
            typename="function/kafka-egress",
            topic="cluster",
            value=normalized_text,
            value_type=StringType,
        )
    )
