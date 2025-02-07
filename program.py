# banyak = int(input("berapa banyak data?"))

# nama = []
# umur = []

# for i in range(0, banyak):
#     # i itu untuk menyimnpan data dari range yang di buat berdasarkan banyak data yang di input
#     print(f"data ke {i}") 
#     # string format
#     # contoh format lama : print("data ke "+ str(i)) ,, karena i itu integer jadi harus di ubah ke string dulu dengan str(i) 
#     input_nama = input("masukan nama")
#     input_umur = int(input("masukan umur"))
    
#     nama.append(input_nama)
#     umur.append(input_umur)
#     # untuk menambahkan data ke list nama dan umur sesuai dengan inputan yang di masukan oleh user  

#     for i in range(len(nama)):
#         data_nama = nama[i]
#         data_umur = umur[i]
#     print(f"nama : {data_nama}, umur : {data_umur}")

# buat fitur berapa banyak data yang ingin di input'
banyak = int(input("berapa banyak data ?"))

nama= []
umur = []

for i in range(0,banyak):
    print(f"data ke {i}")
    input_nama = input("masukan nama")
    input_umur = int(input("masukan umur"))

    nama.append(input_nama)
    umur.append(input_umur)
    for i in range(len(nama)):
        data_nama = nama[i]
        data_umur = umur[i]
    print(f"nama : {data_nama}, umur : {data_umur}")
    print(f"ini semua data: {nama} dan {umur}")

    