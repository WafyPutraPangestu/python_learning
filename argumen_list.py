
def jumlahkan(satu, dua, tiga):
    total = satu + dua + tiga
    print(f"total {satu} + {dua} +{tiga} = {total}")
jumlahkan(10, 20, 30)

# argument list
def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"total {list_angka} = {total}")
jumlahkan(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

def jumlahkan(x, *list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"total {list_angka} = {total}")
jumlahkan(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
