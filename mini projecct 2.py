print("==== Sistem Pengingat Jadwal ====")
print()

jadwal = {
    "Senin": {},
    "Selasa": {},
    "Rabu": {},
    "Kamis": {},
    "Jum'at": {},
    "Sabtu": {},
    "Minggu": {}
}

def peran():
    while True:
        peran_input = input("Masukkan peran (admin/pengguna): ").strip()
        if peran_input == "admin":
            menu_admin()
            break
        elif peran_input == "pengguna":
            menu_pengguna()
            break
        else:
            print("Peran tidak valid! Silakan coba lagi.")

def tambah_mata_pelajaran():
    hari = input("Hari: ").strip()
    jam = input("Waktu: ").strip()
    mata_pelajaran = input("Mata pelajaran: ").strip()
    
    if hari in jadwal:
        jadwal[hari][jam] = mata_pelajaran
        print("Mata pelajaran berhasil ditambahkan!")
    else:
        print("Hari tidak valid!")

def update_mata_pelajaran():
    hari = input("Hari: ").strip()
    jam = input("Jam: ").strip()
    mata_pelajaran = input("Mata pelajaran baru: ").strip()
    
    if hari in jadwal and jam in jadwal[hari]:
        jadwal[hari][jam] = mata_pelajaran
        print("Mata pelajaran berhasil diperbarui!")
    else:
        print("Jadwal tidak ditemukan!")

def hapus_jadwal():
    hari = input("Hari: ").strip()
    jam = input("Jam: ").strip()
    
    if hari in jadwal and jam in jadwal[hari]:
        del jadwal[hari][jam]
        print("Mata pelajaran berhasil dihapus!")
    else:
        print("Jadwal tidak ditemukan!")

def lihat_jadwal():
    print("Jadwal:")
    for hari, jam in jadwal.items():
        print(f"{hari}:")
        if jam:
            for jam_waktu, mata_pelajaran in jam.items():
                print(f"  {jam_waktu}: {mata_pelajaran}")
        else:
            print("  (Tidak ada mata pelajaran)")

def hapus_hari():
    hari = input("Masukkan hari yang ingin dihapus: ").strip()
    if hari in jadwal:
        del jadwal[hari]
        print(f"{hari} berhasil dihapus beserta semua mata pelajarannya!")
    else:
        print("Hari tidak valid!")

def reset_jadwal():
    global jadwal
    jadwal = {
        "Senin": {},
        "Selasa": {},
        "Rabu": {},
        "Kamis": {},
        "Jum'at": {},
        "Sabtu": {},
        "Minggu": {}
    }
    print("Jadwal berhasil direset!")

def menu_pengguna():
    while True:
        print("\nMenu Pengguna:")
        print("1. Tambah mata pelajaran")
        print("2. Perbarui mata pelajaran")
        print("3. Hapus mata pelajaran")
        print("4. Lihat jadwal")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi: ")
        if pilihan == "1":
            tambah_mata_pelajaran()
        elif pilihan == "2":
            update_mata_pelajaran()
        elif pilihan == "3":
            hapus_jadwal()
        elif pilihan == "4":
            lihat_jadwal()
        elif pilihan == "5":
            break
        else:
            print("Opsi tidak valid!")

def menu_admin():
    while True:
        print("\nMenu Admin:")
        print("1. Tambah mata pelajaran")
        print("2. Perbarui mata pelajaran")
        print("3. Hapus mata pelajaran")
        print("4. Lihat jadwal")
        print("5. Lihat semua hari")
        print("6. Cari jadwal")
        print("7. Reset jadwal")
        print("8. Hapus hari")
        print("9. Keluar")
        
        pilihan = input("Pilih opsi: ")
        
        if pilihan == "1":
            tambah_mata_pelajaran()
        elif pilihan == "2":
            update_mata_pelajaran()
        elif pilihan == "3":
            hapus_jadwal()
        elif pilihan == "4":
            lihat_jadwal()
        elif pilihan == "5":
            lihat_semua_hari()
        elif pilihan == "6":
            cari_jadwal()
        elif pilihan == "7":
            reset_jadwal()
        elif pilihan == "8":
            hapus_hari()
        elif pilihan == "9":
            break
        else:
            print("Opsi tidak valid!")

def lihat_semua_hari():
    print("Daftar Hari dan Jumlah Mata Pelajaran:")
    for hari, jam in jadwal.items():
        jumlah = len(jam)
        print(f"{hari}: {jumlah} mata pelajaran")

def cari_jadwal():
    hari = input("Masukkan hari untuk dicari: ").strip()
    if hari in jadwal:
        print(f"Jadwal untuk {hari}:")
        if jadwal[hari]:
            for jam, mata_pelajaran in jadwal[hari].items():
                print(f"  {jam}: {mata_pelajaran}")
        else:
            print("  (Tidak ada mata pelajaran)")
    else:
        print("Hari tidak valid!")
peran()
