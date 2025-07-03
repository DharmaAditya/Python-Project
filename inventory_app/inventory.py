from typing import List, Dict
import pandas as pd
from datetime import datetime
from database import *

class Inventory:
    @staticmethod
    def add_item(name: str, quantity: int, price: float, category: str = None):
        """Menambahkan item baru"""
        if quantity < 0 or price < 0:
            raise ValueError("Quantity dan price tidak boleh negatif")
        add_item(name, quantity, price, category)
    
    @staticmethod
    def get_items() -> List[Dict]:
        """Mendapatkan semua item"""
        return get_all_items()
    
    @staticmethod
    def update_item(item_id: int, **kwargs):
        """Memperbarui item"""
        valid_fields = {'name', 'quantity', 'price', 'category'}
        for field in kwargs:
            if field not in valid_fields:
                raise ValueError(f"Field {field} tidak valid")
        
        if 'quantity' in kwargs and kwargs['quantity'] < 0:
            raise ValueError("Quantity tidak boleh negatif")
        
        if 'price' in kwargs and kwargs['price'] < 0:
            raise ValueError("Price tidak boleh negatif")
        
        update_item(item_id, **kwargs)
    
    @staticmethod
    def remove_item(item_id: int):
        """Menghapus item"""
        delete_item(item_id)
    
    @staticmethod
    def search(keyword: str) -> List[Dict]:
        """Mencari item"""
        return search_items(keyword)
    
    @staticmethod
    def get_low_stock(threshold: int = 5) -> List[Dict]:
        """Mendapatkan item dengan stok rendah"""
        items = get_all_items()
        return [item for item in items if item['quantity'] < threshold]
    
    @staticmethod
    def get_total_value() -> float:
        """Menghitung total nilai inventory"""
        items = get_all_items()
        return sum(item['quantity'] * item['price'] for item in items)

    @staticmethod
    def export_to_excel(filename: str = None):
        """Mengekspor data inventory ke file Excel"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"inventory_report_{timestamp}.xlsx"
        
        items = get_all_items()
        
        # Convert to DataFrame
        df = pd.DataFrame(items)
        
        # Reorder columns
        df = df[['id', 'name', 'quantity', 'price', 'category', 'last_updated']]
        
        # Export to Excel
        df.to_excel(filename, index=False, sheet_name="Inventory")
        
        return filename