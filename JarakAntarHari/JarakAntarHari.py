# Program menghitung jarak antar hari
# I.F User memasukkan 2 buah tanggal (dd:mm:yy)
# F.S Menampilkan jarak 2 buah tanggal tersebut dalam format tahun, bulan, hari

firstDate = int(input('Masukkan tanggal pertama: '))
firstMonth = int(input('Masukkan bulan pertama: '))
firstYear = int(input('Masukkan tahun pertama: '))

secondDate = int(input('Masukkan tanggal kedua: '))
secondMonth = int(input('Masukkan bulan kedua: '))
secondYear = int(input('Masukkan tahun kedua: '))

totalDayFromFirstDate = (firstYear*365) + (firstMonth*30) + firstDate
totalDayFromSecondDate = (secondYear*365) + (secondMonth*30) + secondDate

differenceDay = totalDayFromSecondDate - totalDayFromFirstDate

year = differenceDay // 365
restDayOfTheYear = differenceDay % 365

month = restDayOfTheYear // 30
day = restDayOfTheYear % 30


print(year, 'tahun', month, 'bulan', day, 'hari')