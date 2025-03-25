import random
import datetime


def main():
    daftar_tugas = {}
    print("Selamat datang di Manajemen Daftar Tugas!")
    while True: 
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Lihat Daftar Tugas")
        print("3. Tandai Tugas Selesai")
        print("4. Hapus Tugas")
        print("5. Rekomendasi Tugas Acak")
        print("6. Keluar")
        
        pilihan = input("Masukkan pilihan (1-6): ")
        
        if pilihan == "1":
            nama_tugas = input("Masukkan nama tugas: ")
            deadline = input("Masukkan deadline (DD-MM-YYYY): ")
            try:
                tanggal_deadline = datetime.datetime.strptime(deadline, "%d-%m-%Y").date()
                id_tugas = random.randint(1000, 9999)
                daftar_tugas[id_tugas] = {
                    'nama': nama_tugas,
                    'deadline': tanggal_deadline,
                    'selesai': False
                }
                print(f"Tugas '{nama_tugas}' berhasil ditambahkan dengan ID {id_tugas}!")
            except ValueError:
                print("Format tanggal tidak valid! Gunakan DD-MM-YYYY")
                
        elif pilihan == "2":
            if not daftar_tugas:
                print("Daftar tugas kosong!")
            else:
                print("\nDaftar Tugas:")
                for id_tugas, detail in daftar_tugas.items():
                    status = "Selesai" if detail['selesai'] else "Belum Selesai"
                    print(f"ID: {id_tugas} | Tugas: {detail['nama']} | Deadline: {detail['deadline']} | Status: {status}")
                    
        elif pilihan == "3":
            id_tugas = int(input("Masukkan ID tugas yang selesai: "))
            if id_tugas in daftar_tugas:
                daftar_tugas[id_tugas]['selesai'] = True
                print(f"Tugas '{daftar_tugas[id_tugas]['nama']}' ditandai selesai!")
            else:
                print("ID tugas tidak ditemukan!")
                
        elif pilihan == "4":
            id_tugas = int(input("Masukkan ID tugas yang akan dihapus: "))
            if id_tugas in daftar_tugas:
                del daftar_tugas[id_tugas]
                print("Tugas berhasil dihapus!")
            else:
                print("ID tugas tidak ditemukan!")
                
        elif pilihan == "5":
            if daftar_tugas:
                tugas_belum_selesai = [t for t in daftar_tugas.values() if not t['selesai']]
                if tugas_belum_selesai:
                    rekomendasi = random.choice(tugas_belum_selesai)
                    print(f"Rekomendasi tugas untuk dikerjakan: '{rekomendasi['nama']}' (Deadline: {rekomendasi['deadline']})")
                else:
                    print("Semua tugas sudah selesai!")
            else:
                print("Daftar tugas kosong!")
                
        elif pilihan == "6":
            print("Terima kasih telah menggunakan program ini!")
            break
            
        else:
            print("Pilihan tidak valid! Silakan masukkan angka 1-6.")

if __name__ == "__main__":
    main()