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

    def __init__(self, text):
        self.text = text
        self.text_lang_code = "en_UK"
        self.translated_lang_code = "es_ES"
        self.status = RequestStatus.REQUESTED

    def __repr__(self):
        return '<id {}>'.format(self.id)