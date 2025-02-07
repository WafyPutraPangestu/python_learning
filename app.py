import function 


daftar_kontak = []
daftar_kontak.append({
    "nama": "wafy",
    "email": "wafy@gmail.com",
    "telepon": "08123456789"
    
})

while True: 
    print("Selamat datang!")
    print("--- Menu ---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar")
    menu = input("Pilih menu:")
    
    if menu == "0":
     break
    elif menu == "1":
        function.display_kontak(daftar_kontak)
    elif menu == "2":
        kontak = function.nambah_kontak()
        daftar_kontak.append(kontak)
    elif menu == "3":
        function.hapus_kontak(daftar_kontak)
    elif menu == "4":
        function.cari_kontak(daftar_kontak)
    else:
        print("Menu tidak tersedia")
        
        
print("Program selesai, sampai jumpa!")
    