import random

print("==============")
print("Permainan Suit")
print("==============")

print("")
def pilihan():
    print("Pilihan : ")
    print("1. Gunting")
    print("2. Batu")
    print("3. Kertas")
    print("4. Keluar")

def permainan():
    kamu = int(input("Masukkan Pilihanmu : "))
    kom = random.choice(["Gunting", "Batu", "Kertas" ])
    if kamu == 1:
        print("Kamu     : Gunting")
        print("Komputer : ", kom)
        if kom == "Gunting":
            print("\tSeri")
        if kom == "Batu":
            print("\tKamu kalah")
        if kom == "Kertas":
            print("\tKamu menang")

    if kamu == 2:
        print("Kamu     : Batu")
        print("Komputer : ", kom)
        if kom == "Gunting":
            print("\tKamu menang")
        if kom == "Batu":
            print("\tSeri")
        if kom == "Kertas":
            print("\tKamu Menang")

    if kamu == 3:
        print("Kamu     : Kertas")
        print("Komputer : ", kom)
        if kom == "Gunting":
            print("\tKamu kalah")
        if kom == "Batu":
            print("\tKamu menang")
        if kom == "Kertas":
            print("\tSeri")

        if kamu == 4:
            exit


    if kamu >= 5:
        print("Pilihan tidak tersedia")
        pilihan()
        permainan()
    if kamu == 0:
        print("Mode cheat diaktifkan(belum bisa digunakan)")
        pilihan()
        permainan()
while True :
    pilihan()
    permainan()

