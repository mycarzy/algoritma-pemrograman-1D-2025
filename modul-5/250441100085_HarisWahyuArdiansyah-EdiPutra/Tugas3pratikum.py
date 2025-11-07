while True:

    def hitunggaji(nama, jabatan, gajipokok):
        jabatan = jabatan.lower()

        if jabatan == "manager":
            persentunjangan = 0.10
        elif jabatan == "staff":
            persentunjangan = 0.05
        else:
            persentunjangan = 0.0

        tunjangan = int(gajipokok * persentunjangan)
        pph = int(gajipokok * 0.05  )
        gajiakhir = int(gajipokok - pph + tunjangan)
        
        print("\n========================================")
        print(f"Nama        : {nama}")
        print(f"Jabatan     : {jabatan}")
        print(f"Gaji Pokok  : Rp{gajipokok}")
        print(f"Tunjangan   : Rp{tunjangan}")
        print(f"PPH (5%)    : Rp{pph}")
        print(f"Gaji Bersih : Rp{gajiakhir}")
        print("========================================")
        
    while True:
        nama = str(input("Nama : "))
        if any(char.isdigit()for char in nama):
            print("Input nama terdapat angka")
        else:
            break
            
    while True:
        jabatan = str(input("Jabatan : "))
        if any(char.isdigit()for char in jabatan):
            print("Input jabatan terdapat angka")
        else:
            break
    while True:
        try: 
            gajipokok = int(input("Gaji Pokok : "))
            
            if gajipokok < 0:
                print("Gaji tidak boleh minus")
            else:
                break
        except ValueError:
            print("Gaji harus berupa angka")
        
    hitunggaji(nama, jabatan, gajipokok)


    lanjut = input("Apakah ingin lanjut? (y/n)")
    if lanjut == "n":
        break