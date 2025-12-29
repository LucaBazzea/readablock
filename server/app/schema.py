from ninja import Schema


class BookSchema(Schema):
    #book_id: int
    #character_limit: int
    #sentence_last_read: int = 0
    page_turn: str | None = None # "next" | "previous"
