def ganjil(bawah, atas):
  
    deret = []
    if bawah < atas:
        mulai = bawah + 1 if bawah % 2 == 0 else bawah + 2
        for i in range(mulai, atas, 2):
            deret.append(i)
    else:
        mulai = bawah if bawah % 2 != 0 else bawah - 1
        for i in range(mulai, atas - 1, -2):
            deret.append(i)
    print(", ".join(map(str, deret)))

ganjil(10, 30)
ganjil(97, 82)