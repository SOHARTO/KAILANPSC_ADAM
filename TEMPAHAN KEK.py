jenis_kek = ["keju", "mentega","pelangi","kopi"]
print("HARGA KEK KEJU=RM40,MENTEGA==RM35,PELANGI=RM25,KOPI=15")
a=int(input("Masukkan tempahan untuk kek keju"))
b=int(input("Masukkan tempahan untuk kek mentega"))
c=int(input("Masukkan tempahan untuk kek pelangi"))
d=int(input("Masukkan tempahan untuk kek kopi"))

tempahan = [a,b,c,d]

def jumlah_harga():
    for i in range (4):
        jumlah[i] = harga_kek[i]*tempahan[i]
    return (jumlah)    

def cetak ():
    print("\n\ntempahan anda ialah")
    print(a,"kek", jenis_kek[0])
    print(a,"kek", jenis_kek[1])
    print(a,"kek", jenis_kek[2])
    print(a,"kek", jenis_kek[3])