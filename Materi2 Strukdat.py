# Membuat objek list Hewan
Hewan = ["Kucing", "Anjing", "Kuda", "Gajah", "Unta", "Jerapah"]
print("Semua Hewan:")
print(Hewan)

# Membuat objek list DeleteHewan
DeleteHewan = ["Kucing", "Gajah", "Kelinci"]
print("Hewan Yang Dihapus :")
print(DeleteHewan)

# Melakukan penghapusan data dari objek Hewan yang sama dengan data warna yang terdapat pada objek DeleteHewan
for hewan in DeleteHewan:
    while hewan in Hewan:
        Hewan.remove(hewan)

# Menampilkan hasilnya
print("Hewan setelah dihapus:")
print(Hewan)
