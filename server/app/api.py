from ninja import NinjaAPI
from ninja.responses import Response

from app import schema, services


api = NinjaAPI()


@api.post("/read/")
def read(request, data: schema.BookSchema):
    """Return the next `n` sentences starting from `sentence_current`."""
    start = data.sentence_current
    end = start + data.sentences_amount

    sentences = services.get_epub_as_list()

    if start >= len(sentences):
        return Response({"error": "Current sentence out of range"}, status=400)
    if end > len(sentences):
        end = len(sentences)

    return Response({"sentences": sentences[start:end]}, status=200)
