from fastapi import APIRouter, HTTPException, Depends

from Schemas import LanguageSchema, LanguageInDBSchema
from CRUD import CRUDLanguage


language_router = APIRouter(
    prefix="/language"
)


async def check_language_id(language_id: int) -> int | None:
    language = await CRUDLanguage.get(language_id=language_id)
    if language:
        return language_id
    else:
        raise HTTPException(status_code=404, detail="invalid language_id arrived")


@language_router.get("/get", response_model=LanguageInDBSchema, tags=["Language"])
async def get_language(language_id: int = Depends(check_language_id)):
    language = await CRUDLanguage.get(language_id=language_id)
    if language:
        return language
    else:
        raise HTTPException(status_code=404, detail=f"language with id{language_id} is not found")


@language_router.get("/all", response_model=list[LanguageInDBSchema], tags=["Language"])
async def get_all_languages():
    languages = await CRUDLanguage.get_all()
    if languages:
        return languages
    else:
        raise HTTPException(status_code=404, detail="languages not found")


@language_router.post("/add", response_model=LanguageInDBSchema, tags=["Language"])
async def add_language(language: LanguageSchema):
    language = await CRUDLanguage.add(language=language)
    if language:
        return language
    else:
        raise HTTPException(status_code=404, detail="this language is exist")


@language_router.delete("/del", tags=["Language"])
async def delete_language(language_id: int = Depends(check_language_id)):
    await CRUDLanguage.delete(language_id=language_id)
    raise HTTPException(status_code=200, detail=f"language with id {language_id} was deleted")


@language_router.put("/update", tags=["Language"])
async def update_language(language: LanguageInDBSchema):
    await CRUDLanguage.update(language=language)
    raise HTTPException(status_code=200, detail="language was updated")
