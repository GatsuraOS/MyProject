import sqlite3
from Schemas import LanguageSchema
from Schemas import LanguageInDBSchema


conn = sqlite3.connect("db.db")
cur = conn.cursor()


class LanguageCRUD:

    @staticmethod
    def add(language: LanguageSchema) -> None:
        cur.execute("""
        INSERT INTO languages(language_cod);
        """, (language.language_code, ))
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
    def update(language_id: int, language: LanguageSchema) -> None:
        cur.execute("""
        UPDATE languages SET (language_cod) WHERE id = ?;
        """, (language.language_code, language_id))
        conn.commit()

    @staticmethod
    def delete(language_id: int) -> None:
        cur.execute("""
        DELETE FROM languages WHERE id = ?;
        """, (language_id, ))
