while True:
    def anagram(kata1,kata2):
        kata1 = kata1.replace(" ","").lower()
        kata2 = kata2.replace(" ","").lower()
        return sorted(kata1) == sorted(kata2)

    kata1 = input("Masukan Kata ke Satu : ")
    kata2 = input("Masukan Kata ke Dua : ")

    if anagram(kata1,kata2):
        print("Dua kata tersebut Merupakan Anagram")
    else:
        print("Dua kata tersebut Bukan Anagram")

    lanjut = input("Apakah ingin lanjut? (y/n): ")
    if lanjut == "n":
        break