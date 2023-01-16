import unicodedata

import nltk
from app.adapters.stateful_functions import stateful_functions
from nltk.tokenize import word_tokenize
from statefun import Context, Message, StringType, message_builder

from .typename import NORMALIZATION, TFIDF

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
    text: str = message.as_type(StringType)
    normalized_text = [
        lemmatize(word).lower()
        for word in word_tokenize(text)
        if not is_punct(word) and not is_stopword(word)
    ]
    normalized_text = " ".join(normalized_text)
    context.send(
        message_builder(
            target_typename=TFIDF,
            target_id=context.address.id,
            value=normalized_text,
            value_type=StringType,
        )
    )
