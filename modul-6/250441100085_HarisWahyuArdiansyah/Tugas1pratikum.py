

datakunjungan = [] 
id = 1      

def tambah_kunjungan(id):
    print()
    print("===Pendataan Pengunjung Santri===")
    nama_pengunjung = input("Masukkan nama pengunjung : ")
    nama_santri = input("Nama antri Yang Dijenguk : ")
    daerah = input("Asal Daerah (Sumatr/Kalimantan/Jawa) : ").lower()

    if daerah not in ["sumatra", "kalimantan", "jawa"]:
        print("Hanya dapat memasukan daerah yang berasal dari SUMATRA,KALIMANTAN,JAWA")
        return id
    datakunjungan.append([id, nama_pengunjung, nama_santri, daerah])
    print("Data Berhasil ditambahkan")
    id += 1
    return id


def tampilkan_kunjungan():
    print()
    print("=== Daftar Kunjungan Santri ===")
    if not datakunjungan:
        print("Belum ada data kunjungan")
        return
    urutan_daerah = ["sumatra", "kalimantan", "jawa"]
    for daerah in urutan_daerah:
        print(f"--->Daerah: {daerah}<---")
        ada_data = False
        for data in datakunjungan:
            if data[3] == daerah:
                print(f"ID: {data[0]} | Pengunjung: {data[1]} | Santri: {data[2]}")
                ada_data = True
        if not ada_data:
            print("Tidak ada pengunjung")


def hapus():
    print("\n=== Hapus Data Kunjungan ===")
    if not datakunjungan:
        print("Belum ada data kunjungan")
        return
    try:
        idhapus = int(input("Masukkan id yang ingin dihapus: "))
        for data in datakunjungan:
            if data[0] == idhapus:
                datakunjungan.remove(data)
                print(f"Data id-{idhapus} berhasil dihapus.")
                return
        print("id tidak ditemukan.")
    except ValueError:
        print("Input harus berupa angka.")

while True:
    print("\n=== Sistem Kunjungan Santri ===")
    print("1. Tambah Data")
    print("2. Tampilkan Kunjungan")
    print("3. Hapus Data Kunjungan")
    print("0. Keluar")

    pilihan = input("Pilih menu (1-4): ")
    
    if pilihan == "1":
        id = tambah_kunjungan(id)
    elif pilihan == "2":
        tampilkan_kunjungan()
    elif pilihan == "3":
        hapus()
    elif pilihan == "0":
        break
    else:
        print("Pilihan tidak tersedia")
