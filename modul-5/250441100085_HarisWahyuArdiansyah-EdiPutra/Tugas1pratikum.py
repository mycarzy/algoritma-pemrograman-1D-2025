while True:
    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial (n - 1)
        
    while True:
        try:
            n = int(input("Masukan bilangan : "))
            if n < 0:
                print("Angka harus bilangan positif")
            else:
                print(f"Hasil faktorial dari {n} adalah : {factorial(n)}")
                break
        except ValueError:
            print("Input harus berupa angka!!")

    lanjut = input("Apakah Ingin Lanjut ?(y/n)")
    if lanjut == "n":
        break
            