n = int(input("Masukkan jumlah baris (n): "))

lebar = len(str(n)) + 1  

for i in range(1, n + 1):

    for j in range(1, i + 1):
        print(f"{j:{lebar}}", end="")

    for k in range((n - i) * lebar * 2):
        print(" ", end="")

    for j in range(i, 0, -1):
        print(f"{j:{lebar}}", end="")

    print()
