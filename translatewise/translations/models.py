from translatewise import db
from enum import Enum


class RequestStatus(Enum):
    PENDING = "PENDING"
    REQUESTED = "REQUESTED"
    TRANSLATED = "TRANSLATED"


class Translation(db.Model):
    __tablename__ = 'translations'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(), nullable=False, unique=True)
    text_lang_code = db.Column(db.String(8), nullable=False)
    translated = db.Column(db.String())
    translated_lang_code = db.Column(db.String(8), nullable=False)
    status = db.Column(db.String(16), nullable=False)
    word_count = db.Column(db.Integer)

    def __init__(self, text, text_lang_code="en", translated_lang_code="es"):
        self.text = text
        self.text_lang_code = text_lang_code
        self.translated_lang_code = translated_lang_code
        self.status = RequestStatus.REQUESTED.value

    def __repr__(self):
        return (
            f"Translation({self.text}, "
            f"{self.translated}, "
            f"{self.word_count}, "
        )
