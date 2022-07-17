import sqlite3
from Schemas import CategorySchema
from Schemas import CategoryInDBSchema


conn = sqlite3.connect("db.db")
cur = conn.cursor()


class CategoryCRUD:

    @staticmethod
    def add(category: CategorySchema) -> None:
        cur.execute("""
        INSERT INTO categories(parent_id, is_published, name);
        """, (category.parent_id, category.is_published, category.name))
        conn.commit()

    @staticmethod
    def get(category_id: int) -> list[CategoryInDBSchema]:
        cur.execute("""
        SELECT * FROM categories WHERE id = ?;
        """, (category_id, ))
        categories = []
        for category in cur.fetchall():
            categories.append(
                CategoryInDBSchema(
                    id=category[0],
                    parent_id=category[1],
                    is_published=category[2],
                    name=category[3]
                )
            )
        return categories

    @staticmethod
    def get_all() -> list[CategoryInDBSchema]:
        cur.execute("""
        SELECT * FROM categories;
        """)
        categories = []
        for category in cur.fetchall():
            categories.append(
                CategoryInDBSchema(
                    id=category[0],
                    parent_id=category[1],
                    is_published=category[2],
                    name=category[3]
                )
            )
        return categories

    @staticmethod
    def update(category_id: int, category: CategorySchema) -> None:
        cur.execute("""
        UPDATE categories SET (parent_id, is_published, name) WHERE id = ?;
        """, (category.parent_id, category.is_published, category.name, category_id))
        conn.commit()

    @staticmethod
    def delete(category_id: int) -> None:
        cur.execute("""
        DELETE FROM categories WHERE id = ?;
        """, (category_id, ))
        conn.commit()
