inventaris = {}
id_barang = 1


def tampilkan():
    if not inventaris:
        print("Belum ada barang dalam inventaris.")
        return
    print("\n=== DAFTAR INVENTARIS ===")
    for id_barang, data in inventaris.items():
        print(f"ID: {id_barang} || Nama: {data[0]} | Harga: {data[1]} | Stok: {data[2]}")

def cari():
    if not inventaris:
        print()
        print("Belum ada data/barang dalam inventaris.")
        return
    id_barang = input("Masukkan ID barang yang dicari: ")
    id_barang = int(id_barang)
    if id_barang not in inventaris:
        print("Barang tidak ditemukan.")
    else:
        nama, harga, stok = inventaris[id_barang]
        print(f"Barang ditemukan: Nama : {nama} | Hargan : {harga} |  Stok : {stok}")


def tambah_barang(id_barang):
    nama = input("Masukkan nama barang: ")
    
    while True:
        harga = input("Masukkan harga barang: ")
        if not harga.isdigit():
            print("Harga harus berupa angka!")
            continue
        harga = int(harga)
        break

    while True:
        stok = input("Masukkan jumlah stok: ")
        if not stok.isdigit():
            print("Stok harus berupa angka!")
            continue
        stok = int(stok)
        break
    
    inventaris[id_barang] = [nama, harga, stok]
    print("Barang berhasil ditambahkan.")
    id_barang += 1
    return id_barang

def update_stok():
    if not inventaris:
        print("Belum ada barang dalam inventaris.")
        return
    id_barang = int(input("Masukkan ID barang yang ingin diperbarui stoknya: "))
    if id_barang not in inventaris:
        print("Barang tidak ditemukan.")
        return
    nama = inventaris[id_barang][0]
    stok = inventaris[id_barang][2]
    print(f"Nama barang : {nama} || Jumlah stok : {stok}")

    while True:
        perubahan = input("Masukkan perubahan stok (Tambahkan '-' jika ingin mengurangi stok): ")
        try:
            perubahan = int(perubahan)
        except ValueError:
            print("Input harus berupa angka ")
            continue
        stokbaru = stok + perubahan

        if stokbaru < 0:
            print("Perubahan ini akan membuat stok negatif! Coba lagi.")
            continue
        break

    inventaris[id_barang][2] = stokbaru
    print(f"Stok {nama} berhasil diperbarui menjadi {stokbaru}.")


def hapus_barang():
    if not inventaris:
        print("Belum ada barang dalam inventaris.")
        return
    id_barang = int(input("Masukkan ID barang yang ingin dihapus: "))

    if id_barang not in inventaris:
        print("Barang tidak ditemukan.")
    else:
        del inventaris[id_barang]
        print("Barang berhasil dihapus.")


while True:
    print("\n=== INVENTARIS GUDANG ===")
    print("1. Tampilkan Semua Barang")
    print("2. Cari Barang")
    print("3. Tambah Barang Baru")
    print("4. Update Stok Barang")
    print("5. Hapus Barang")
    print()
    print("0. Keluar")

    pilihan = input("Pilih : ")
    if pilihan == "1":
        tampilkan()
    elif pilihan == "2":
        cari()
    elif pilihan == "3":
        id_barang = tambah_barang(id_barang)
    elif pilihan == "4":
        update_stok()
    elif pilihan == "5":
        hapus_barang()
    elif pilihan == "0":
        print("Keluar dari program")
        break
    else:
        print("Pilihan tidak valid!")
        continue

