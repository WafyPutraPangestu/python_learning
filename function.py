def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("========================")
        print(f"nama: {kontak['nama']}")
        print(f"Email: {kontak['email']}")
        print(f"Telepon: {kontak['telepon']}")
        
    
def nambah_kontak():
    nama = input("nama:")
    email = input("email:")
    telepon = input("telepon:")
    kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon,
    }
    return kontak

def hapus_kontak(daftar_kontak):
    telepon = input("masukan nomor telepon yang akan dihapus:")
    index = -1
    for i in range(0, len(daftar_kontak)):
        kontak = daftar_kontak[i]
        if telepon == kontak["telepon"]:
            index = i
            break
    if index == -1:
        print("gagal menghapus daftar kontak karena tidak ditemukan")
    else:
        print("berhasil menghapus daftar kontak")
    del daftar_kontak[index]
    
def cari_kontak(daftar_kontak):
    nama_yg_dicari = input("masukan nama yang akan dicari:")
    for kontak in daftar_kontak:
        nama = kontak["nama_yg_dicari"]
        if nama.lower().find(nama_yg_dicari.lower()) != -1:
            print("========================")
            print(f"nama: {kontak['nama']}")
            print(f"Email: {kontak['email']}")
            print(f"Telepon: {kontak['telepon']}")
        