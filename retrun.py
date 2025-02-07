# def jumlahkan(*list_angka):
#     total = 0
#     for angka in list_angka:
#         total = total + angka
#     print(f"total {list_angka} = {total}")
#     return total
# total = jumlahkan(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# print(total)
def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    print(f"total {list_angka} = {total}")
    return (list_angka, total)
list_angka, total = jumlahkan(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(f"list angka = {list_angka}, total = {total}")
