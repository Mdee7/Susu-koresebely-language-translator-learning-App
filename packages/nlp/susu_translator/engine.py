"""Minimal translation engine stub for MVP scaffolding."""

SAMPLE_LEXICON: dict[tuple[str, str, str], str] = {
    ("i ni", "susu", "en"): "hello",
    ("hello", "en", "susu"): "i ni",
}


def translate_text(text: str, source_language: str, target_language: str) -> str:
    """Translate using a tiny in-memory lexicon, fallback passthrough."""
    normalized = text.strip().lower()
    return SAMPLE_LEXICON.get((normalized, source_language.lower(), target_language.lower()), text)
