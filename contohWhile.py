# = 1
#hile i < 6:
  #rint(i)
  # += 1


#while menguakan break 

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1 


# While Menggunakan continue 
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  #rint(i)


data = [2, 4, 6, 8, 10]
sum = 0
i=0

while i < len(data):
	sum += data[i]
	i += 1

rata_rata= sum / len(data)
print ('Rata-rata data adalah:', rata_rata)