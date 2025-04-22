def hitung_faktorial(n):
    #fungsi menghitung faktorial
    if n == 0 or n == 1:
        return 1
    else:
        hasil = 1
        for i in range(2, n+1):
            hasil *= i
        return hasil

def main():
    #Input angka dari user
    try:
        angka = int(input("Masukkan angka : "))
        if angka < 0:
            print("Angka harus positif atau nol")
        else:
            #Menampilkan hasil dari faktorial
            print(f"Faktorial dari {angka} adalah {hitung_faktorial(angka)}")
    except ValueError:
        print("Input tidak valid, masukkan angka bulat")

# Menjalankan fungsi utama
if __name__ == "__main__":
    main()