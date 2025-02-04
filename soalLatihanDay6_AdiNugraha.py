# Adi Nugraha - JCDS 2602
# Tugas Day 6


filmAnda = input("Masukan 5 film kesukaan anda dipisahkan dengan tanda koma : ")
filmTeman = input("Masukan 5 film kesukaan teman anda dipisahkan dengan tanda koma : ")

filmAnda = filmAnda.split(",")
filmTeman = filmTeman.split(",")

filmAnda = set(filmAnda)
filmTeman = set(filmTeman)

kesukaanFilm = filmAnda.intersection(filmTeman)
persenKesukaan = len(kesukaanFilm) / len(filmAnda) * 100

print(f"Kesukaan film kalian yang sama sebesar {persenKesukaan} %")

# Case 2
# SOAL 4

print('''
      Selamat Datang di Pasar Buah
      List Menu :
      1. Menampilkan Daftar Buah 
      2. Menambah Buah
      3. Menghapus Buah
      4. Membeli Buah
      5. Exit Program
      ''')

listBuah = [
    {
        "Nama":"Apel",
        "Stock": 20,
        "Harga" : 10000
    },
    {
        "Nama":"Jeruk",
        "Stock": 15,
        "Harga" : 15000
    },
    {
        "Nama":"Anggur",
        "Stock": 25,
        "Harga" : 20000
    }
]

keranjangBelanja = []

while True:
    opsi = int(input("Masukan Opsi : "))
    if opsi == 1:
        print('Index : Nama : Stock : Harga')
        for i in range(len(listBuah)):
            print(f"{i} : {listBuah[i]['Nama']} : {listBuah[i]['Stock']} : {listBuah[i]['Harga']}")
    elif opsi == 2:
        namaBuah = input("Masukan Nama Buah : ")
        stockBuah = int(input("Masukan Stock Buah : "))
        hargaBuah = int(input("Masukan Harga Buah : "))
        listBuah.append({
            "Nama": namaBuah,
            "Stock": stockBuah,
            "Harga" : hargaBuah
        })
        print('Index : Nama : Stock : Harga')
        for i in range(len(listBuah)):
            print(f"{i} : {listBuah[i]['Nama']} : {listBuah[i]['Stock']} : {listBuah[i]['Harga']}")
    elif opsi == 3:
        print('Index : Nama : Stock : Harga')
        for i in range(len(listBuah)):
            print(f"{i} : {listBuah[i]['Nama']} : {listBuah[i]['Stock']} : {listBuah[i]['Harga']}")
        indexBuah = int(input("Masukan Index Buah Yang Ingin Dihapus : "))
        # listBuah.pop(indexBuah)
        del listBuah[indexBuah]
        print('Index : Nama : Stock : Harga')
        for i in range(len(listBuah)):
            print(f"{i} : {listBuah[i]['Nama']} : {listBuah[i]['Stock']} : {listBuah[i]['Harga']}")
    elif opsi == 4:
        print('Index : Nama : Stock : Harga')
        for i in range(len(listBuah)):
            print(f"{i} : {listBuah[i]['Nama']} : {listBuah[i]['Stock']} : {listBuah[i]['Harga']}")
        
        while True:
            indexBuah = int(input("Masukan Index Buah Yang Ingin Dibeli : "))
            jumlah = int(input("Masukan Jumlah Buah Yang Ingin Dibeli: "))     

            if listBuah[indexBuah]['Stock'] < jumlah:
                print(f"Stock tidak cukup, stock {listBuah[indexBuah]['Nama']} tinggal {listBuah[indexBuah]['Stock']} buah")
                ulang = input("Mau beli yang lain ? (ya/tidak) : ").lower()
                if ulang == 'tidak':
                    break
                elif ulang == 'ya':
                    continue
               
            keranjangBelanja.append({
                "Buah": listBuah[indexBuah]['Nama'],
                "Harga" : listBuah[indexBuah]['Harga'] ,
                "Qty" : jumlah
            })

            listBuah[indexBuah]['Stock'] -= jumlah

            print('Index : Nama : Stock : Harga')
            for i in range(len(keranjangBelanja)):
                print(f"{i} : {keranjangBelanja[i]['Buah']} : {keranjangBelanja[i]['Qty']} : {keranjangBelanja[i]['Harga']}")

            
            ulang = input("Mau beli yang lain ? (ya/tidak) : ").lower()
            if ulang == 'tidak':
                
                print('Index : Nama : Stock : Harga : Total Harga')
                for i in range(len(keranjangBelanja)):
                    print(f"{i} : {keranjangBelanja[i]['Buah']} : {keranjangBelanja[i]['Qty']} : {keranjangBelanja[i]['Harga']} : {keranjangBelanja[i]['Harga'] * keranjangBelanja[i]['Qty']}")

                totalBelanja = sum(item['Harga'] * item['Qty'] for item in keranjangBelanja)
                print(f"Total yang harus anda bayar : {totalBelanja}")

                bayar = int(input("Masukan Uang Pembayaran : "))
                kembalian = bayar - totalBelanja
                print("Terima Kasih")
                print(f"Kembalian anda : {kembalian}")

                keranjangBelanja.clear()

                break
            elif ulang == 'ya':
                continue    
    elif opsi == 5:
        break
    else:
        print("Opsi tidak ada")
    








