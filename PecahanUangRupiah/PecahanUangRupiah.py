# Program pecahan uang rupiah
# I.F User memasukkan uang yang ingin dipecah
# F.S Menampilkan pecahan dalam kelipatan 1000, 500, 100, 50, 25

uang = int(input('Masukkan uang yang ingin dipecah: '))

pecahan1000 = uang // 1000
sisaUang = uang % 1000

pecahan500 = sisaUang // 500
sisaUang = sisaUang % 500

pecahan100 = sisaUang // 100
sisaUang = sisaUang % 100

pecahan50 = sisaUang // 50
sisaUang = sisaUang % 50

pecahan25 = sisaUang // 25

print(pecahan1000, 'pecahan 1000,', pecahan500, 'pecahan 500,', pecahan100, 'pecahan 100,', pecahan50, 'pecahan 50,', pecahan25, 'pecahan 25')