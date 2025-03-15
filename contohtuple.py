nama=('Ali', 'Budi', 'Citra')

for n in nama:
	print(n)
	

nama = ('Ali', 'Budi', 'Citra')
nama_yang_dicari = 'Budi'
ada = False

for n in nama:
	if n == nama_yang_dicari:
		ada = True
		break

if ada:
	print (nama_yang_dicari, 'ada dalam tuple.')
else:
	print (nama_yang_dicari, 'tidak ada dalam tuple.')