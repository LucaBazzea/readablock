from ninja import Schema


class BookSchema(Schema):
    #book_id: int
    #characters_per_page: int
    sentence_current: int = 0
    sentences_amount: int = 4
