import sqlite3
from typing import List, Dict, Optional

def create_connection():
    """Membuat koneksi ke database SQLite"""
    conn = sqlite3.connect('inventory.db')
    return conn

def initialize_database():
    """Membuat tabel jika belum ada"""
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        category TEXT,
        last_updated TEXT DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()

def add_item(name: str, quantity: int, price: float, category: str = None):
    """Menambahkan item baru ke inventory"""
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO items (name, quantity, price, category)
    VALUES (?, ?, ?, ?)
    ''', (name, quantity, price, category))
    
    conn.commit()
    conn.close()

def get_all_items() -> List[Dict]:
    """Mendapatkan semua item dari inventory"""
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM items')
    rows = cursor.fetchall()
    
    items = []
    for row in rows:
        items.append({
            'id': row[0],
            'name': row[1],
            'quantity': row[2],
            'price': row[3],
            'category': row[4],
            'last_updated': row[5]
        })
    
    conn.close()
    return items

def update_item(item_id: int, name: str = None, quantity: int = None, 
                price: float = None, category: str = None):
    """Memperbarui item yang ada"""
    conn = create_connection()
    cursor = conn.cursor()
    
    # Membuat query dinamis berdasarkan parameter yang diberikan
    updates = []
    params = []
    
    if name is not None:
        updates.append("name = ?")
        params.append(name)
    if quantity is not None:
        updates.append("quantity = ?")
        params.append(quantity)
    if price is not None:
        updates.append("price = ?")
        params.append(price)
    if category is not None:
        updates.append("category = ?")
        params.append(category)
    
    if not updates:
        return  # Tidak ada yang diupdate
    
    query = "UPDATE items SET " + ", ".join(updates) + " WHERE id = ?"
    params.append(item_id)
    
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def delete_item(item_id: int):
    """Menghapus item dari inventory"""
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
    
    conn.commit()
    conn.close()

def search_items(keyword: str) -> List[Dict]:
    """Mencari item berdasarkan nama atau kategori"""
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT * FROM items 
    WHERE name LIKE ? OR category LIKE ?
    ''', (f'%{keyword}%', f'%{keyword}%'))
    
    rows = cursor.fetchall()
    
    items = []
    for row in rows:
        items.append({
            'id': row[0],
            'name': row[1],
            'quantity': row[2],
            'price': row[3],
            'category': row[4],
            'last_updated': row[5]
        })
    
    conn.close()
    return items