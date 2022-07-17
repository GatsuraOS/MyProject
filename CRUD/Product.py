import sqlite3
from Schemas import ProductSchema
from Schemas import ProductInDBSchema


conn = sqlite3.connect("db.db")
cur = conn.cursor()


class ProductCRUD:

    @staticmethod
    def add(product: ProductSchema) -> None:
        cur.execute("""
        INSERT INTO products(category_id, price, total, name);
        """, (product.category_id, product.price, product.total, product.name))
        conn.commit()


    @staticmethod
    def get(product_id: int) -> list[ProductInDBSchema]:
        cur.execute("""
        SELECT * FROM products WHERE id = ?;
        """, (product_id, ))
        products = []
        for product in cur.fetchall():
            products.append(
                ProductInDBSchema(
                    id=product[0],
                    category_id=product[1],
                    price=product[2],
                    total=product[3],
                    name=product[4]
                )
            )
        return products


    @staticmethod
    def get_all() -> list[ProductInDBSchema]:
        cur.execute("""
        SELECT * FROM products;
        """)
        products = []
        for product in cur.fetchall():
            products.append(
                ProductInDBSchema(
                    id=product[0],
                    category_id=product[1],
                    price=product[2],
                    total=product[3],
                    name=product[4]
                )
            )
        return products


    @staticmethod
    def update(product_id: int, product: ProductSchema) -> None:
        cur.execute("""
        UPDATE products SET (category_id, price, total, name) WHERE id = ?;
        """, (product.category_id, product.price, product.total, product.name, product_id))
        conn.commit()


    @staticmethod
    def delete(category_id: int) -> None:
        cur.execute("""
        DELETE FROM categories WHERE id = ?;
        """, (category_id, ))
        conn.commit()