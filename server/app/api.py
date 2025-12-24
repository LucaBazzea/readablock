from django.core.cache import cache

from ninja import NinjaAPI
from ninja.responses import Response

from app import schema, services


api = NinjaAPI()

@api.post("/read/")
def read(request, data: schema.BookSchema):
    sentence_last_read = cache.get("sentence_last_read") or 0

    epub = services.convert_epub_to_str()
    epub_cleaned = services.remove_html(epub)

    if sentence_last_read == 0:
        sentence_first = 0
    else:
        sentence_first = sentence_last_read + 1

    # TODO calculate this based on character limit
    sentence_last = sentence_first + 4
 
    sentences = services.convert_text_to_sentences(epub_cleaned, sentence_first, sentence_last)

    cache.set("sentence_last_read", sentence_last, 300)

    return Response(
        {"sentences": sentences, "sentence_last_read": sentence_last_read},
        status=200
    )
