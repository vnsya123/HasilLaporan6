def hitung_ips():
    jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))
    total_nilai = 0
    total_sks = 0

    for i in range(jumlah_matkul):
        nilai = input(f"Masukkan nilai mata kuliah ke-{i+1} (A/B/C/D): ").upper()
        sks = 3  

        if nilai == 'A':
            bobot = 4
        elif nilai == 'B':
            bobot = 3
        elif nilai == 'C':
            bobot = 2
        elif nilai == 'D':
            bobot = 1
        else:
            print("Nilai tidak valid. Masukkan A, B, C, atau D.")
            continue 

        total_nilai += bobot * sks
        total_sks += sks

    if total_sks > 0:
        ips = total_nilai / total_sks
        print(f"IPS Anda adalah: {ips:.2f}")
    else:
        print("Tidak ada mata kuliah yang diinput.")

hitung_ips()