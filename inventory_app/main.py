from inventory import Inventory
import sys

def display_menu():
    print("\nSistem Manajemen Inventory")
    print("1. Tambah Item")
    print("2. Lihat Semua Item")
    print("3. Update Item")
    print("4. Hapus Item")
    print("5. Cari Item")
    print("6. Lihat Stok Rendah")
    print("7. Total Nilai Inventory")
    print("8. Export ke Excel")
    print("9. Keluar")

def add_item_ui():
    print("\nTambah Item Baru")
    name = input("Nama: ")
    quantity = int(input("Quantity: "))
    price = float(input("Harga: "))
    category = input("Kategori (opsional): ") or None
    
    try:
        Inventory.add_item(name, quantity, price, category)
        print("Item berhasil ditambahkan!")
    except ValueError as e:
        print(f"Error: {e}")

def view_items_ui():
    print("\nDaftar Item")
    items = Inventory.get_items()
    
    if not items:
        print("Tidak ada item dalam inventory.")
        return
    
    print(f"{'ID':<5} {'Nama':<20} {'Quantity':<10} {'Harga':<10} {'Kategori':<15} {'Terakhir Diupdate'}")
    print("-" * 80)
    for item in items:
        print(f"{item['id']:<5} {item['name']:<20} {item['quantity']:<10} {item['price']:<10.2f} {item['category'] or '-':<15} {item['last_updated']}")

def update_item_ui():
    item_id = int(input("Masukkan ID item yang akan diupdate: "))
    
    print("Masukkan nilai baru (kosongkan jika tidak ingin mengubah)")
    name = input("Nama: ") or None
    quantity = input("Quantity: ")
    quantity = int(quantity) if quantity else None
    price = input("Harga: ")
    price = float(price) if price else None
    category = input("Kategori: ") or None
    
    try:
        Inventory.update_item(
            item_id,
            name=name,
            quantity=quantity,
            price=price,
            category=category
        )
        print("Item berhasil diupdate!")
    except ValueError as e:
        print(f"Error: {e}")

def delete_item_ui():
    item_id = int(input("Masukkan ID item yang akan dihapus: "))
    Inventory.remove_item(item_id)
    print("Item berhasil dihapus!")

def search_items_ui():
    keyword = input("Masukkan kata kunci pencarian: ")
    items = Inventory.search(keyword)
    
    if not items:
        print("Tidak ditemukan item yang sesuai.")
        return
    
    print(f"\nHasil pencarian untuk '{keyword}':")
    print(f"{'ID':<5} {'Nama':<20} {'Quantity':<10} {'Harga':<10} {'Kategori':<15}")
    print("-" * 60)
    for item in items:
        print(f"{item['id']:<5} {item['name']:<20} {item['quantity']:<10} {item['price']:<10.2f} {item['category'] or '-'}")

def low_stock_ui():
    threshold = input("Masukkan threshold stok rendah (default 5): ") or "5"
    items = Inventory.get_low_stock(int(threshold))
    
    if not items:
        print(f"Tidak ada item dengan stok di bawah {threshold}.")
        return
    
    print(f"\nItem dengan stok di bawah {threshold}:")
    print(f"{'ID':<5} {'Nama':<20} {'Quantity':<10} {'Harga':<10}")
    print("-" * 45)
    for item in items:
        print(f"{item['id']:<5} {item['name']:<20} {item['quantity']:<10} {item['price']:<10.2f}")

def total_value_ui():
    total = Inventory.get_total_value()
    print(f"\nTotal nilai inventory: Rp {total:,.2f}")

def export_to_excel_ui():
    filename = input("Masukkan nama file output (kosongkan untuk nama default): ") or None
    try:
        output_file = Inventory.export_to_excel_pretty(filename)
        print(f"Data berhasil diexport ke file: {output_file}")
    except Exception as e:
        print(f"Error saat mengekspor data: {e}")

def main():
    # Inisialisasi database
    from database import initialize_database
    initialize_database()
    
    while True:
        display_menu()
        choice = input("Pilih menu (1-8): ")
        
        if choice == '1':
            add_item_ui()
        elif choice == '2':
            view_items_ui()
        elif choice == '3':
            update_item_ui()
        elif choice == '4':
            delete_item_ui()
        elif choice == '5':
            search_items_ui()
        elif choice == '6':
            low_stock_ui()
        elif choice == '7':
            total_value_ui()
        elif choice == '8':
            export_to_excel_ui()    
        elif choice == '9':
            print("Keluar dari aplikasi...")
            sys.exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()