from fastapi import APIRouter
from pydantic import BaseModel, Field

from susu_translator.engine import translate_text

router = APIRouter()


class TranslationRequest(BaseModel):
    text: str = Field(min_length=1, description="Input text")
    source_language: str = Field(description="Language code, e.g., susu")
    target_language: str = Field(description="Language code, e.g., en")


class TranslationResponse(BaseModel):
    translation: str
    engine: str


@router.post("/translate", response_model=TranslationResponse)
def translate(payload: TranslationRequest) -> TranslationResponse:
    result = translate_text(
        text=payload.text,
        source_language=payload.source_language,
        target_language=payload.target_language,
    )
    return TranslationResponse(translation=result, engine="rule_based_stub")
