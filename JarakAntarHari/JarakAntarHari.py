# Program menghitung jarak antar hari
# I.F User memasukkan 2 buah tanggal (dd:mm:yy)
# F.S Menampilkan jarak 2 buah tanggal tersebut dalam format tahun, bulan, hari

tanggalPertama = int(input('Masukkan tanggal pertama: '))
bulanPertama = int(input('Masukkan bulan pertama: '))
tahunPertama = int(input('Masukkan tahun pertama: '))

tanggalKedua = int(input('Masukkan tanggal kedua: '))
bulanKedua = int(input('Masukkan bulan kedua: '))
tahunKedua = int(input('Masukkan tahun kedua: '))

totalHariDariTanggalPertama = (tahunPertama*365) + (bulanPertama*30) + tanggalPertama
totalHariDariTanggalKedua = (tahunKedua*365) + (bulanKedua*30) + tanggalKedua

perbedaanHari = totalHariDariTanggalKedua - totalHariDariTanggalPertama

tahun = perbedaanHari // 365
sisaHariDariTahun = perbedaanHari % 365

bulan = sisaHariDariTahun // 30
hari = sisaHariDariTahun % 30


print(tahun, 'tahun', bulan, 'bulan', hari, 'hari')