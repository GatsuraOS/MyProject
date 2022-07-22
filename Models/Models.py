from datetime import datetime

from sqlalchemy import Column, SmallInteger, VARCHAR, TIMESTAMP, ForeignKey, Boolean, DECIMAL
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Category(Base):
    __tablename__: str = "categories"

    id = Column(SmallInteger, primary_key=True)
    parent_id = Column(SmallInteger, ForeignKey("categories.id", ondelete="CASCADE"))
    is_published = Column(Boolean, default=False)
    name = Column(VARCHAR(20), nullable=False)


class Product(Base):
    __tablename__: str = "products"

    id = Column(SmallInteger, primary_key=True)
    category_id = Column(SmallInteger, ForeignKey("categories.id"), ondelete="CASCADE", nullable=False)
    price = Column(DECIMAL(8, 2), default=0)
    total = Column(DECIMAL(10, 2), default=0)
    is_published = Column(Boolean, default=False)
    name = Column(VARCHAR(24), nullable=False)


class Language(Base):
    __tablename__: str = "languages"

    id = Column(SmallInteger, primary_key=True)
    language_cod = Column(VARCHAR(10), nullable=False, unique=True)


class Status(Base):
    __tablename__: str = "statuses"

    id = Column(SmallInteger, primary_key=True)
    name = Column(VARCHAR(15), default="new", unique=True)


class BotUser(Base):
    __tablename__: str = "bot_users"

    id = Column(VARCHAR(20), primary_key=True, nullable=False)
    is_blocked = Column(Boolean, default=False)
    balance = Column(DECIMAL(8, 2), default=0)
    language_id = Column(SmallInteger, ForeignKey("languages.id"), ondelete="NO ACTION", nullable=False)


class Invoice(Base):
    __tablename__: str = "invoices"

    id = Column(VARCHAR(15), primary_key=True, nullable=False)
    bot_user_id = Column(VARCHAR(20), nullable=False)
    date_create = Column(TIMESTAMP, default=datetime.now())
    total = Column(SmallInteger, default=0)
    status_id = Column(SmallInteger, ForeignKey("statuses.id"),
                       onupdate="CASCADE", ondelete="NO ACTION",
                       nullable=False)


class Order(Base):
    __tablename__: str = "orders"

    id = Column(SmallInteger, primary_key=True)
    bot_user_id = Column(VARCHAR(20), ForeignKey("bot_users.id"), ondelete="CASCADE", nullable=False)
    date_create = Column(TIMESTAMP, default=datetime.now())
    status_id = Column(SmallInteger, ForeignKey("statuses.id"),
                       onupdate="CASCADE", ondelete="NO ACTION",
                       nullable=False)
    invoice_id = Column(VARCHAR(15), ForeignKey("invoices.id"),
                        ondelete="CASCADE", onupdate="CASCADE",
                        nullable=False)


class OrderItem(Base):
    __tablename__: str = "order_items"

    id = Column(SmallInteger, primary_key=True)
    order_id = Column(SmallInteger, ForeignKey("orders.id"),
                      ondelete="CASCADE", onupdate="CASCADE",
                      nullable=False)
    product_id = Column(SmallInteger, ForeignKey("products.id"),
                        ondelete="CASCADE", onupdate="CASCADE",
                        nullable=False)
    total = Column(SmallInteger, default=0)
