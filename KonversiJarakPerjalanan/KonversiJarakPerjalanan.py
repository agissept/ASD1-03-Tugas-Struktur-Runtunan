# Program konversi jarak perjalanan
# I.F User memasukkan jarak dalam satuan cm
# F.S Menampilkan jarak dalam format km, m, cm

jarakDalamCM =  int(input('Masukkan jarak dalam cm : '))

kilometer = jarakDalamCM // 100000
sisaJarakDalamCm = jarakDalamCM % 100000

meter = sisaJarakDalamCm // 100
centimeter = sisaJarakDalamCm % 100

print(kilometer, 'km', meter, 'm', centimeter, 'cm')