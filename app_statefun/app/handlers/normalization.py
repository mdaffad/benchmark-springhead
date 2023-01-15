import unicodedata

import nltk
from app.adapters.stateful_functions import stateful_functions
from nltk.tokenize import word_tokenize
from statefun import Context, Message

stopwords = set(nltk.corpus.stopwords.words("english"))
lemmatizer = nltk.stem.WordNetLemmatizer()


def is_punct(token):
    return all(unicodedata.category(char).startswith("P") for char in token)


def is_stopword(token):
    return token.lower() in stopwords


def lemmatize(token):
    return lemmatizer.lemmatize(token)


@stateful_functions
def normalize(context: Context, message: Message, process: Process) -> None:  # noqa
    text: str = message.as_type(process.source_type_value)  # str expected
    normalized_text = [
        lemmatize(word).lower()
        for word in word_tokenize(text)
        if not is_punct(word) and not is_stopword(word)
    ]
    normalized_text = " ".join(normalized_text)
    # TODO: alternative target_id = context.address.target_id
    process.send(target_id=process.target_id, value=normalized_text, context=context)
