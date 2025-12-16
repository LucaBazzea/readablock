import os
import re

from ebooklib import epub, ITEM_DOCUMENT


def get_epub_as_list():
    """Load the EPUB file and split its text into sentences."""
    epub_path = os.path.join(os.path.dirname(__file__), "../Gatto e topo in società.epub")
    book = epub.read_epub(epub_path)

    text = []
    for item in book.get_items():
        if item.get_type() == ITEM_DOCUMENT:
            text.append(item.get_content().decode("utf-8"))

    full_text = "\n".join(text)

    sentences = re.split(r'(?<=[.!?])\s+', full_text.strip())

    # Filter out empty sentences
    sentences = [s for s in sentences if s]

    return sentences
