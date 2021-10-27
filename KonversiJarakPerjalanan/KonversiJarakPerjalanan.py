# Program konversi jarak perjalanan
# I.F User memasukkan jarak dalam satuan cm
# F.S Menampilkan jarak dalam format km, m, cm

distanceInCM =  int(input('Masukkan jarak dalam cm : '))

kilometer = distanceInCM // 100000
restDistanceInCm = distanceInCM % 100000

meter = restDistanceInCm // 100
centimeter = restDistanceInCm % 100

print(kilometer, 'km', meter, 'm', centimeter, 'cm')