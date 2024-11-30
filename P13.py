# Ketikan Code Disini lalu Jalankan (Run)
import os


class DataMahasiswa:
    def membuatfiledatamahasiswa():
       
        if os.path.exists("data_mahasiswa.txt"):
            pass
        
        else:
            with open("data_mahasiswa.txt", "w") as file:
                file.write("--- Data Mahasiswa ---\n")

    def menambahkan_data_mahasiswa():
        
        with open("data_mahasiswa.txt", "a") as file:
            
            nama = input("Masukkan Nama Lengkap")
            nim = input("Masukkan NIM")
            
            file.writelines(f"Nama Lengkap: {nama}, NIM: {nim}\n")
            print(f"Data Berhasil Disimpan  dengan nama {nama} - {nim}")
    

class BacaData:
    def membacafiledatamahasiswa():
        with open("data_mahasiswa.txt", "r") as file:
            for namamahasiswa in file:
                print(namamahasiswa)
    
    def membacafiledatakehadiran():
        with open("kehadiran.txt", "r") as file:
            for namakehadiran in file:
                print(namakehadiran)
    


class Kehadiran:
    def membuatfiledatakehadiran():
        
        if os.path.exists("kehadiran.txt"):
            pass
        else:
            with open("kehadiran.txt","w") as file:
                file.write("--- Data Kehadiran ---\n")

    def menambahkan_data_kehadiran():
            
            nama1 = input("Masukkan Nama Lengkap")
            
            if Kehadiran.cek_nama(nama1):
                print("Nama Sudah Ada")
                return
            else:
                pass

            inputkehadiran = input("Hadir /Tidak Hadir")    
            
            if inputkehadiran.lower() == 'hadir' or inputkehadiran.lower() == 'tidak hadir':
                with open("kehadiran.txt", "a") as file:
                    file.writelines(f"{nama1} - {inputkehadiran}\n")
                    print("Data Telah Ditambahkan")
        
            elif inputkehadiran == "Keluar":
                return 
            
            else:
                print("Input tidak valid, Isi (Hadir/Tidak Hadir)")
                return 

    def cek_nama(nama):
        
        if os.path.exists("kehadiran.txt"):
            with open("kehadiran.txt", "r") as file:
                for baris in file:
                    bagian = baris.split('-')
                    if len(bagian) >= 2:
                        if bagian[0].strip().lower() == nama.lower():
                            return True  
        return False  
                
            

class FileManager:
    def menghapus_file():
        while True:
            inputanfiledata = input("Masukkan nama file, Misal (kehadiran.txt), (Ketik k untuk keluar)")
            
            if inputanfiledata == "k":
                break

            if os.path.exists(inputanfiledata):
                inputankonfirmasi = input(f"Apakah anda yakin ingin menghapus file {inputanfiledata} (y/n)")

                if inputankonfirmasi == "y":
                    os.remove(inputanfiledata)
                    print(f"File {inputanfiledata} berhasil dihapus ")
                    return Menu.main_menu
                
                elif inputankonfirmasi == "n":
                    print(f"File tidak jadi dihapus")
                    return Menu.main_menu

                
                else:
                    print("Input tidak valid, tolong masukkan 'y' atau 'n'")
                



class Menu():
    def main_menu():
        print("-----------")
        print("1. Menambahkan Data Mahasiswa")
        print("2. Menampilkan Data Mahasiswa")
        print("3. Menambahkan Data Kehadiran")
        print("4. Menampilkan Data Kehadiran")
        print("5. Menghapus File")
        print("6. Keluar")
        
        while True:
            
            pilihan = input("Masukkan Pilihan")

            if pilihan == "1":
                DataMahasiswa.membuatfiledatamahasiswa()
                DataMahasiswa.menambahkan_data_mahasiswa()
            
            elif pilihan == "2":
                BacaData.membacafiledatamahasiswa()
            
            elif pilihan == "3":
                Kehadiran.membuatfiledatakehadiran()
                Kehadiran.menambahkan_data_kehadiran()

            elif pilihan == "4":
                BacaData.membacafiledatakehadiran()
                
            elif pilihan == "5":
                FileManager.menghapus_file()

            elif pilihan == "6":
                break

            else:
                print("Pilihan Tidak Valid")

Menu.main_menu()

        
            

    
