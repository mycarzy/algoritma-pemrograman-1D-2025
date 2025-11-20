kontak = {}

def tampilkan():
    if not kontak:
        print("Belum ada data")
        return
    for key,data in kontak.items():
        print(f"Nama : {key} | No Telepon : {data[0]} | Email : {data[1]}")

def tambah():
    while True:
        nama = input("Nama kontak baru: ").strip().capitalize()
        nama = nama.replace(" ","")
        if not nama.isalpha():
            print("terdapat angka")
        else:
            break
    if nama in kontak:
        print("Kontak dengan nama ini sudah ada")
        return
    
    while True:
        telepon = input("Nomor telepon: ")
        if not telepon.isdigit():
            print("nomor harus berisi angka")
            continue
        break

    email = input("Email: ").strip()

    kontak[nama] = [telepon, email]
    print("Kontak ditambahkan")    

def cari():
    if not kontak:
        print("Belum ada data")
    else:
        tampilkan()
        nama = input("Masukan nama yang ingin dicari : ").capitalize()
        if nama in kontak:
            telepon, email = kontak[nama]
            print()
            print(f"Data ditemukan")
            print(f"Nama : {nama}")
            print(f"Telepon : {telepon}")
            print(f"Email   : {email}\n")
        else:
            print("Kontak tidak ditemukan")

def update_email():
    if not kontak:
        print("Belum ada data")
    else:
        tampilkan()
        nama = input("Masukan nama yang ingin diupdate emailnya : ").capitalize()
        if nama not in kontak:
            print("Nama tidak ditemukan")
            return
        newemail = input(f"Masukan email baru untuk {nama} : ")
        kontak[nama][1] = newemail
        print("Email berhasil diperbarui!\n")

def hapus():
    if not kontak:
        print("Belum ada data")
    else:
        tampilkan()
        nama = input("Masukkan nama kontak yang ingin dihapus: ").capitalize()
        if nama not in kontak:
            print("Kontak tidak ditemukan")
            return
        del kontak[nama]
        print("Kontak berhasil dihapus")


while True:
    print("""
=== Program KONTAK ===
1. Tampilkan semua kontak
2. Cari kontak
3. Tambah kontak
4. Update email 
5. Hapus 
0. Keluar
""")

    pilihan = input("Pilih menu: ").strip()

    if pilihan == "1":
        tampilkan()
    elif pilihan == "2":
        cari()
    elif pilihan == "3":
        tambah()
    elif pilihan == "4":
        update_email()
    elif pilihan == "5":
        hapus()
    elif pilihan == "0":
        print("Program selesai")
        break
    else:
        print("Pilihan tidak valid")
