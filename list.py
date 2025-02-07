nama = []
# nambah data ke list
nama.append("wafy")
nama.append("putra")
nama.append("pangestu")

# ngambil data satuan dari list dimulai dari 0
print(nama[0])
print(nama[2])
print(nama[1])
print (len(nama))

# menghapus data dari list
nama.remove("wafy")
print(nama)
print(nama[0])
print(nama[1])
print (len(nama))

# mengganti data dari list
print(nama)
nama[0] = "wafy"
nama[1] = "putra"
print(nama)
print(nama[1])
print(nama[0])