while True:
    print("Masukkan Hanya Angka dan pisahkan dengan spasi (contoh: 3 1 4)")
    while True:
        try:
            a = input("Masukkan elemen tuple pertama: ")
            a = a.split()
            a = tuple(int(i) for i in a)
            break
        except ValueError:
            print("masukan input hanya angka, pisahkan dengan spasi")


    while True:
        try:
            b = input("Masukkan elemen tuple kedua: ")
            b = b.split()
            b = tuple(int(i) for i in b)
            break
        except ValueError:
            print("masukan input hanya angka, pisahkan dengan spasi")



    gabung = a + b
    print("Hasil gabungan : ", gabung)

    cekduplikat = []
    for angka in gabung:
        if angka not in cekduplikat:
            cekduplikat.append(angka)
    print("Cek duplikat : ", cekduplikat)

    n = len(cekduplikat)
    for i in range(n):
        for j in range(0, n - i - 1):
            if cekduplikat[j] < cekduplikat[j + 1]:
                cekduplikat[j], cekduplikat[j + 1] = cekduplikat[j + 1], cekduplikat[j]
    print("Setelah diurutkan descending:", cekduplikat)

    hasilakhir = tuple(cekduplikat)
    print("Hasil akhir : ", hasilakhir)
    
    lanjut = input("apakah ingin lanjut? (y/n): ")
    if lanjut == "n":
        break
