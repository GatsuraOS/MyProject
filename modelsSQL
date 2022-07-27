import sqlite3

conn = sqlite3.connect("db.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id INTEGER,
    is_published BOOLEAN DEFAULT (false),
    name TEXT NOT NULL,
    FOREIGN KEY (parent_id) REFERENCES categories(id)
);
""")
conn.commit()
cur.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER,
    price REAL DEFAULT (0),
    total INTEGER DEFAULT (0),
    name TEXT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
""")
conn.commit()
cur.execute("""
CREATE TABLE IF NOT EXISTS languages(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    language_cod TEXT NOT NULL UNIQUE 
);
""")
conn.commit()
cur.execute("""
CREATE TABLE IF NOT EXISTS statuses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);
""")
conn.commit()
cur.execute("""
CREATE TABLE IF NOT EXISTS bot_users(
    id TEXT PRIMARY KEY NOT NULL UNIQUE,
    is_blocked BOOLEAN DEFAULT (false),
    balance REAL DEFAULT (0),
    language_id INTEGER NOT NULL,
    FOREIGN KEY (language_id) REFERENCES languages(id) 
);
""")
conn.commit()
cur.execute("""
CREATE TABLE IF NOT EXISTS invoices(
    id TEXT PRIMARY KEY NOT NULL UNIQUE,
    bot_user_id TEXT NOT NULL,
    date_create INTEGER,
    total INTEGER DEFAULT (0),
    status_id INTEGER NOT NULL,
    FOREIGN KEY (bot_user_id) REFERENCES bot_users(id),
    FOREIGN KEY (status_id) REFERENCES statuses(id)
);
""")
conn.commit()
cur.execute("""
CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    bot_user_id TEXT NOT NULL,
    date_create INTEGER,
    status_id INTEGER NOT NULL,
    invoice_id TEXT NOT NULL UNIQUE,
    FOREIGN KEY (bot_user_id) REFERENCES bot_users(id),
    FOREIGN KEY (status_id) REFERENCES statuses(id),
    FOREIGN KEY (invoice_id) REFERENCES invoices(id)    
);
""")
conn.commit()
cur.execute("""
CREATE TABLE IF NOT EXISTS order_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    total INTEGER DEFAULT (0),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (order_id) REFERENCES orders(id)
);
""")
conn.commit()
