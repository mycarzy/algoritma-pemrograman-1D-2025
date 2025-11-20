
kupon = {}

def tampilkan():
    if not kupon:
        print("Anda tidak memiliki kupon")
        print()
        return
    print("Kupon yang anda miliki")
    print("----------------------")
    for kodekupon,persen in kupon.items():
        print(f" - {kodekupon} : {persen}%")


def tambah():
    inputkode = input("Masukan kode kupon : ").upper().strip()
    if inputkode in kupon:
        print("Kupon sudah ada")
        return
    
    inputpersen = input("Masukan besar diskon : ").strip()
    if not inputpersen.isdigit():
        print("Persen harus berupa angka")
        return
    inputpersen = int(inputpersen)
    if inputpersen <= 0 or inputpersen > 100 :
        print("Diskan hanya 1 - 100")
        return
    
    kupon[inputkode] = inputpersen
    print(f"Kupon {inputkode} berhasil ditambahkan")


def penggunaan():
    while True:
        try:
            harga = int(input("Masukan Total belanjaan : "))
            if harga < 0:
                print("Harga tidak boleh minus")
                continue
            break
        except ValueError:
            print("Pastikan memasukan angka")
            continue
        
    while True:
        print("""
metode pembayaran:
1. Gunakan Kupon
2. Tanpa Kupon
""")
        pilihan = input("Pilih : ")
        if pilihan not in ["1","2"]:
            print("Silakahn pilih diantara (1 dan 2)")
            continue
        
        if pilihan == "1":
            if not kupon:
                print("Anda tidak memiliki kupon")
                print()
                continue

            kode = input("Masukkan kode kupon : ").strip().upper()
            if not kode:
                print("Anda menginput Kosong")
                return
            if kode not in kupon:
                print(f"Kupon '{kode}' tidak valid atau sudah dipakai")
                return
            persen = kupon[kode]
            del kupon[kode]
            print(f"Kupon '{kode}' berhasil dipakai")
            break
        else:
            persen = 0
            break
    diskon = int(harga * (persen / 100.0))
    hargaakhir = int(harga - diskon)
    
    print()
    print("Rincian transaksi:")
    print("-------------------")
    print(f"Total sebelum diskon : {harga}")
    print(f"Potongan Kupon       : {persen}%")
    print(f"Jumlah diskon        : {diskon}")
    print(f"Total yang harus dibayar: {hargaakhir}")
    print()         


print()
print("== Sistem Kasir ==")

while True:
    print("Menu:")
    print("1. Tampilkan kupon tersedia")
    print("2. Pembayaran")
    print("3. Tambah kupon")
    print("0. Keluar")

    pilihan = input("Pilih menu : ")
    print()

    if pilihan == '1':
        tampilkan()
    elif pilihan == '2':
        penggunaan()
    elif pilihan == '3':
        tambah()
    elif pilihan == '0':
        print("Keluar dari program")
        break
    else:
        print("Pilihan tidak valid.")
