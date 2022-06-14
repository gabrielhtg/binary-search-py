import os

os.system('cls')

list_angka = [2, 5, 13, 24, 38, 41, 57, 63, 77, 89, 91]

ujung = 10
awal = 0

def binary_search(yang_dicari, kiri, kanan) :
    tengah = (kanan - kiri) // 2
    
    if (list_angka[tengah] == yang_dicari) :
        return tengah
    
    elif (list_angka[tengah] < yang_dicari) :
        return binary_search(yang_dicari, tengah, kanan + (kanan - tengah))
    
    elif (list_angka[tengah] > yang_dicari) :
        return binary_search(yang_dicari, kiri, tengah)

print("----------------------------------------") 
n = int(input("Masukkan angka yang dicari : "))

print("----------------------------------------")
try :
    print("Nilainya berada di index ke", binary_search(n, awal, ujung))

except :
    print("Bilangan itu tidak dapat ditemukan.")
print("----------------------------------------")

    