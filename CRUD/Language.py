import sqlite3
from Schemas import LanguageSchema
from Schemas import LanguageInDBSchema


conn = sqlite3.connect("db.db")
cur = conn.cursor()


class LanguageCRUD:


    @staticmethod
    def add(language:LanguageSchema) -> None:
        cur.execute("""
        INSERT INTO languages(language_cod);
        """, (language.language_code))
        conn.commit()

    @staticmethod
    def get(language_id: int) -> list[LanguageInDBSchema]:
        cur.execute("""
        SELECT * FROM languages WHERE ID =?;
        """, (language_id, ))
        languages = []
        for language in cur.fetchall():
            languages.append(
                LanguageInDBSchema(
                    id=language[0],
                    language_cod=language[1]
                )
            )
        return languages

    @staticmethod
    def get_all() -> list[LanguageInDBSchema]:
        cur.execute("""
        SELECT * FROM languages;
        """)
        languages = []
        for language in cur.fetchall():
            languages.append(
                LanguageInDBSchema(
                    id=language[0],
                    language_cod=language[1]
                )
            )
        return languages

    @staticmethod
    def update(language_id: int, language: LanguageInDBSchema) -> None: