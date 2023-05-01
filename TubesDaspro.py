import os 
import argparse 
import sys

#Deklarasi Global Variabel
userName : str  = ""
userPass : str  = ""
userFile : str = [[""] for i in range(101)]
bahanBangunan : str = [[""] for i in range(101)]
daftarCandi : str = [[""] for i in range(101)]
sedangBerjalan : bool = True
seed : int = 0
totalBatu : int = 0
totalPasir : int = 0
totalAir : int = 0

# ===============================================================
# Kumpulan Fungsi Umum
# ===============================================================
def maximum(a:int,b:int)->int:
    if(a>b):return a
    else : return b 
def minimum(a:int,b:int)->int:
    if(a<b):return a
    else : return b 

def panjangFile(namaFile): 
    f = open(namaFile, "r")
    i = 0
    t = "test"
    while(t != ""): 
        t = f.readline()
        i+=1 
    return i-1
# ---------------------------------------------------------------- 
def tipeUser(userNameUser:str)-> str :
    for i in range(1,panjangFile("user.csv")): 
        if(userFile[i][0] == userNameUser):
            return userFile[i][2] 
# ----------------------------------------------------------------        
def length(nString, i:int =0, nMark:chr ='.'): #REKURSIF
    if i >= len(nString) or nString[i] == nMark:
        return i
    else:
        return length(nString, i + 1, nMark)
# ---------------------------------------------------------------- 
def cekPass(PassUser, arrayUser, n, i=1):  #REKURSIF
    if i >= n:
        return False
    elif arrayUser[i][1] == PassUser:
        return True
    else:
        return cekPass(PassUser, arrayUser, n, i + 1)
# ---------------------------------------------------------------- 
def cekUser(nameUser, arrayUser, n, i=1): #REKURSIF
    if i >= n:
        return False
    elif arrayUser[i][0] == nameUser:
        return True
    else:
        return cekUser(nameUser, arrayUser, n, i + 1)
 # ----------------------------------------------------------------    
def initializeArray (array : list, n :int, m:int, array2:list , n2:int) : 
    newArray = [["" for i in range(m)] for i in range(n+n2)]
    for i in range(n):
        for j in range(m): 
            newArray[i][j] = array[i][j]
    
    for i in range(n2): 
        for j in range(m): 
            newArray[i + n][j] = array2[j]
    return newArray
# ---------------------------------------------------------------- 
def initializeArray2 (array : list, n :int, m:int, array2:list , n2:int) : 
    newArray = [["" for i in range(m)] for i in range(n+n2)]
    for i in range(n): 
        for j in range(m): 
            newArray[i][j] = array[i][j]

    for i in range(n2): 
        for j in range(m): 
            newArray[i + n][j] = array2[i][j]
    return newArray           
# ----------------------------------------------------------------         
def splitArr(nString:str,n:int): #Split dilakukan dengan asumsi ";" sebagai pemisah
    tmpArray = ["" for i in range(n)]
    tmpStr = ""
    indexArray =0
    for i in range(length(nString)): 
        if(nString[i] == ";"):
            tmpArray[indexArray]=tmpStr
            tmpStr = ""
            indexArray +=1
        else : 
            tmpStr+=nString[i]
    tmpStr = removeEndspace(tmpStr)
    tmpArray[indexArray]=tmpStr
    return tmpArray
# ---------------------------------------------------------------- 
def removeEndspace(x, i=0, temp=""): #REKURSIF
    if i >= length(x) or x[i] == "\n":
        return temp
    else:
        return removeEndspace(x, i + 1, temp + x[i])
# ---------------------------------------------------------------- 
def hapusCandiCSV(indikatorHapus:str, jumlahHapus:int, indexIndikator:int): 
    arrayNew = [["" for i in range(5)] for i in range(panjangFile("candi.csv") -jumlahHapus)]
    x = 0
    cnt = 0
    for i in range(panjangFile("candi.csv")):
        if(daftarCandi[i][indexIndikator] != indikatorHapus):
            for j in range(5): 
                arrayNew[cnt][j] = daftarCandi[x][j]
            cnt+=1
        x += 1
    return arrayNew
# ---------------------------------------------------------------- 
def hapusJinCSV(namaJin:str): 
    arrayNew = [["" for i in range(3)] for i in range(panjangFile("user.csv") -1)]
    x = 0
    for i in range(panjangFile("user.csv")-1):
        if(userFile[i][0] == namaJin):
            x+=1
        for j in range(3): 
                arrayNew[i][j] = userFile[x][j]
        x+=1
    return arrayNew
# ---------------------------------------------------------------- 
def writeFile(namaFile,array,n , m): 
    f = open(namaFile, "w")
    for i in range(n): 
        for j in range(m): 
            if(j == m-1): 
                f.write(array[i][j])
            else :
                f.write(array[i][j]+";") 
        f.write("\n")
    f.close()
# ---------------------------------------------------------------- 
def cekId(id:int): 
    for i in range(panjangFile("candi.csv")): 
        if(id == daftarCandi[i][0]): 
            return True
    return False
# ---------------------------------------------------------------- 
def getTotal(index: int): 
    jumlahCandi = panjangFile("candi.csv")
    cnt = 0
    for i in range(1, jumlahCandi) : 
        cnt += int(daftarCandi[i][index]) 
    return cnt
# ---------------------------------------------------------------- 

#Fungsi Khusus untuk Soal - Soal
def memintaArgs() : #Prosedur untuk parent folder
    parser = argparse.ArgumentParser()
    parser.add_argument("Parent_Folder",help="nama parent folder penyimpanan data untuk aplikasi",type=str, nargs= "?")
    args  = parser.parse_args()
    if not args.Parent_Folder : 
        print("Tidak ada nama folder yang diberikan") 
        sys.exit()
    path = args.Parent_Folder
    if os.path.exists(path) : 
        print("Folder exist...")
        os.chdir(path)
        print("Parent Folder located....")
    else : 
        print('Folder "%s" tidak ditemukan'%path)
        sys.exit()

#Kumpulan prosedur & fungsi Load       
def load(namaFile:str,n:int)->list :  #Fungsi load utama -> Mengembalikkan array untuk diinisiasi ke variabel
    f = open(namaFile, 'r') 
    isiFile= f.readline()
    isiFile = str(isiFile)
    x = 0 
    tmpArray = [[""for i in range(n)]for i in range(panjangFile(namaFile))]
    while(isiFile != ""): 
        tmpStr = splitArr(isiFile,n)
        for i in range(n) : 
            tmpArray[x][i] = tmpStr[i]
        x+=1
        isiFile = f.readline()
    return tmpArray

def loadBahanBangunan(): #Prosedur untuk me-load bahan bangunan
    global totalBatu,totalAir,totalPasir, bahanBangunan
    bahanBangunan = load("bahan_bangunan.csv",3) #Digunakan fungsi load utama 
    if(panjangFile("bahan_bangunan.csv") > 1): 
        totalPasir = int(bahanBangunan[1][2])
        totalBatu = int(bahanBangunan[2][2])
        totalAir = int(bahanBangunan[3][2])
    print("Daftar bahan bangunan berhasil di-load")

def loadUserFile(): #Prosedur untuk me-load file user
    global userFile 
    userFile = load("user.csv",3)
    print("Daftar user berhasil di-load")

def loadDaftarCandi(): #Prosedur untuk me-load candi
    global daftarCandi 
    daftarCandi = load("candi.csv",5)
    print("Daftar candi berhasil di-load")
#End of Prosedur load

def save(): #Prosedur save
    panjangFileUser = panjangFile("user.csv")
    panjangFileBahan = panjangFile("bahan_bangunan.csv")
    panjangFIleCandi = panjangFile("candi.csv")
    namaFolder = input("Masukklan nama folder : ")
    print("Saving...")
    namaFolder= namaFolder
    os.chdir("..")
    if os.path.exists(namaFolder): 
        os.chdir(namaFolder)
    else : 
        print("Membuat folder " + namaFolder)
        os.mkdir(namaFolder)
        os.chdir(namaFolder)
    writeFile("user.csv", userFile , panjangFileUser,3 )
    writeFile("bahan_bangunan.csv",bahanBangunan, panjangFileBahan,3 )
    writeFile("candi.csv", daftarCandi, panjangFIleCandi,5 )
    print("Berhasil menyimpan data di folder " + namaFolder + " !")    

# ===============================================================
# Bagian Login dan Logout
# ===============================================================
def logIn(): #Prosedur login
    print("Silahkan masukkan username Anda")
    global userName , userPass
    lengthArray = panjangFile("user.csv")
    while True: 
        userName = input(">>>> ")
        if(cekUser(userName,userFile, lengthArray)) : 
            print("Masukkan Password")
            userPass = input(">>>> ")
            if(cekPass(userPass,userFile,lengthArray)):     
                print("Login Berhasil")
                break
            else: 
                print("Password Salah")
        else : 
            print("User Tidak Ditemukan")
        print("Masukkan Username Ulang")
# ----------------------------------------------------------------  
def logOut(): #Prosesur untuk logout
    global userPass,userName 
    if(userPass == "" and userName ==""): 
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu ")
    else : 
        userPass = ""
        userName = ""
        print("Logout berhasil")
# ----------------------------------------------------------------  


# ===============================================================
# Bagian untuk Batch Kumpul
# ===============================================================

# Prosedur menggunakan prosedur untuk bagian Kumpul (Line: ....)
def batchkumpul(): 
    totalJinPengumpul : int = jumlahJin("Pengumpul") 
    if(totalJinPengumpul == 0 ): 
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    else : 
        print("Mengerahkan %d jin untuk mengumpulkan bahan"%totalJinPengumpul)
        Kumpul(totalJinPengumpul)
# ----------------------------------------------------------------


# ===============================================================
# Bagian untuk Batch Bangun
# ===============================================================

# Prosedur batch bangun utama
def batchbangun(): 
    totalJinPembangun  : int =  jumlahJin("Pembangun")
    jumlahCandi = panjangFile("candi.csv")-1
    print("Sudah terdapat %d candi"%jumlahCandi)

    if(totalJinPembangun + jumlahCandi > 100) : 
        print("Mengerahkan %d jin untuk membangun candi"%(100 - jumlahCandi))
        bangunBanyak(jumlahJin-jumlahCandi)
    else : 
        print("Mengerahkan %d jin untuk membangun candi"%totalJinPembangun)
        bangunBanyak(totalJinPembangun)
# ----------------------------------------------------------------

#Prosedur membangun candi setiap jin dan dimasukkan ke csv
def bangunBanyak(jumlahJin :int ): 
    global totalPasir, totalBatu, totalAir, daftarCandi, bahanBangunan
    jumlahPasir = 0 
    jumlahBatu = 0
    jumlahAir = 0
    nPasir = [0 for i in range (jumlahJin)]
    nBatu =[0 for i in range (jumlahJin)]
    nAir = [0 for i in range (jumlahJin)]
    arrayJin = getJinPembangun()
    for i in range(jumlahJin): 
        nPasir[i] =lcg(151873,3112,50603)
        nBatu[i] =lcg(151879,3112,50603)
        nAir[i] = lcg(151837,3112,50603)
        jumlahPasir += nPasir[i]
        jumlahAir += nAir[i]
        jumlahBatu += nBatu[i]
    print("Bahan yang diperlukan : " + str(jumlahPasir) + " pasir, " + str(jumlahBatu) + " batu, " + str(jumlahAir) +" air")
    if(jumlahPasir > totalPasir or jumlahAir > totalAir or jumlahBatu > totalBatu): 
        print("Bangun gagal. Kurang %d pasir, %d batu, dan %d air."%(jumlahPasir-totalPasir),(jumlahBatu-totalBatu),(jumlahAir-totalAir))
        return 0
    else : 
        totalPasir -= jumlahPasir
        totalAir -= jumlahAir
        totalBatu -= jumlahBatu
        print("Jin berhasil membangun %d candi"%jumlahJin)
        for j in range(jumlahJin): 
            idCandi = 0
            for i in range(1,panjangFile("candi.csv")): 
                if(i == panjangFile("candi.csv") -1  or i != int(daftarCandi[i][0]) ): 
                    idCandi = i
            arrayTemp = [str(idCandi), arrayJin[j][0], str(nPasir[j]), str(nBatu[j]),str(nAir[j])]
            if(panjangFile("candi.csv") -1 < 100): 
                arrayNew = initializeArray(daftarCandi, panjangFile("candi.csv"),5, arrayTemp,1)
                writeFile("candi.csv", arrayNew, panjangFile("candi.csv") + 1, 5)
                bahanBangunan[1][2] = str(totalPasir)
                bahanBangunan[2][2] = str(totalBatu)
                bahanBangunan[3][2] = str(totalAir)
                writeFile("bahan_bangunan.csv", bahanBangunan, panjangFile("bahan_bangunan.csv"), 3)
                loadBahanBangunan()
                loadDaftarCandi()
# ----------------------------------------------------------------  

# Fungsi mengembalikan array yang berisi hanya jin pembangun
def getJinPembangun() -> list: 
    jumlahJinPembangun = jumlahJin("Pembangun")
    sebuahArray = [["" for i in range(3)] for i in range(jumlahJinPembangun)] 
    x = 0
    for i in range(panjangFile("user.csv")): 
        if(userFile[i][2] == "Pembangun"): 
            for j in range(3): 
                print(i,j)
                sebuahArray[x][j] = userFile[i][j]
            x+=1
    return sebuahArray
# ---------------------------------------------------------------- 

# ===============================================================
# Fungsi Switch Utama untuk Menerima Command
# ===============================================================
def switch(userCommand): #Fungsi switch untuk input command game

# Fungsi yang bisa diakses semua user
    if( userCommand == "logout"):
        logOut()
    elif(userCommand =="login"): 
        logIn()    
    elif(userCommand == "load"): 
        global userFile, daftarCandi, bahanBangunan 
        userFile = load("user.csv",3)
        daftarCandi = load("candi.csv",5)
        bahanBangunan = load("bahan_bangunan.csv",3)
        if(panjangFile("bahan_bangunan.csv")>1):
            loadBahanBangunan()
    elif(userCommand == "save"): 
        save()
    elif(userCommand == "exit"): 
        Exit()
    elif(userCommand == "help"): 
        Help()
# ----------------------------------------------------------------

# Fungsi yang bisa diakses Bondowoso
    if(userName == "Bondowoso"): 
        if(userCommand == "summonjin"): 
            summonJin()
        elif(userCommand == "hapusjin"):
            hapusJin()
        elif(userCommand == "ubahjin"): 
            ubahTipeJin()
        elif(userCommand == "laporanjin"):
            laporanJin()
        elif(userCommand == "laporancandi"):
            laporanCandi()
        elif(userCommand == "batchbangun"): 
            batchbangun()
        elif(userCommand == "batchkumpul"):
            batchkumpul()
# ----------------------------------------------------------------

#Fungsi yang bisa diakses jin Pembangun atau Pengumpul
    elif(tipeUser(userName) == "Pengumpul"):
        if(userCommand == "kumpul"): 
            Kumpul(1)
    elif(tipeUser(userName) == "Pembangun"):
        if(userCommand == "bangun"): 
            Bangun()
# ---------------------------------------------------------------- 

# Fungsi yang bisa diakses Roro Jonggrang
    elif(userCommand == "ayamberkokok"): 
        ayamBerkokok()
    elif(userCommand == "hancurkancandi"):
        hancurkanCandi()
# ---------------------------------------------------------------- 

def summonJin(): #Prosedur summon jin
    if(panjangFile("user.csv") -3 == 100): 
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu.")
        return 0
    print("Jenis jin yang dapat dipanggil : ")
    print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n(2) Pembangun - Bertugas membangun candi")
    while True: 
        inputNomer = input("Masukkan nomer jenis jin yang ingin dipanggil : ")
        if(inputNomer == "1" ): 
            print('Memilih jin "Pengumpul"')
            tipeJin = "Pengumpul"
            break
        elif(inputNomer == "2" ): 
            print('Memilih jin "Pembangun"')
            tipeJin = "Pembangun"
            break
        else : 
            print('Tidak ada jenis jin bernomor "%d"' %inputNomer)
    while True: 
        namaJin = input("Masukkan username jin : ")
        if(cekUser(namaJin, userFile,panjangFile("user.csv"))) : 
            print('Username "' + namaJin + '" sudah diambil!')
        else: 
            print("Pendaftaran Username berhasil")
            break
    while True : 
        passJin = input("Masukkan password jin : ")
        if(len(passJin) < 5 or length(passJin) > 25): 
            print("Password panjangnya harus 5 - 25 karakter!")
        else : 
            print("Mengumpulkan sesajen...")
            print("Menyerahkan sesajen...")
            print("Membacakan mantra...")
            break
    print("Jin " + namaJin + " berhasil dipanggil")
    arrayTemp = [namaJin, passJin, tipeJin]
    arrayNew = initializeArray(userFile, panjangFile("user.csv"),3,arrayTemp,1)
    writeFile("user.csv",arrayNew,panjangFile("user.csv")+1,3)
    loadUserFile()

#Fungsi dan Prosedur Ubah Tipe Jin 
def getJin(userName): #Fungsi berguna untuk mengambil array yang hanya berisi jin dengan username spesifik
    arrayJin = ["" for i in range(3)]
    for i in range(panjangFile("user.csv")): 
        for j in range(3): 
            if(userFile[i][0] == userName ): 
                arrayJin = [i]
    return arrayJin
 
def ubahTipeJin(): #Fungsi utama ubah tipe jin
    while True  : 
        userNameJin = input("Masukkan username jin : ")
        if( cekUser(userNameJin)) : 
            break 
        else : 
            print("Tidak ada jin dengan username tersebut.")
    arrayJin = getJin(userNameJin)
    while True :
        if(arrayJin[2] == "Pengumpul"): 
            konfirmasiUser = input('Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ')
        elif(arrayJin[2] == "Pembangung"): 
            konfirmasiUser = input('Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ')
        else : 
            print("Error")
            return 0
        if(konfirmasiUser == "Y" or konfirmasiUser =="y"): 
            break
        else : 
            return 0 
        
    for i in range(panjangFile("user.csv")):
        if(userFile[i][0] == userNameJin):
            if(arrayJin[2] == "Pembangun"): 
                userFile[i][2] = "Pengumpul"
            else : 
                userFile[i][2] ="Pembangun"
    writeFile("user.csv", userFile,panjangFile("user.csv"), 3)
    print("Tipe jin berhasil diubah")
    loadUserFile()
    return 0 
#End of Fungsi dan Prosedur Ubah Tipe Jin 

#Prosedur dan Fungsi Hitung Candi 
def hitungCandi(namaJin:str)->int: #Fungsi untuk menghitung beraepa banyak jumlah candi yang ada dengan nama jin spesifik
    cnt = 0 
    for i in range(panjangFile("candi.csv")): 
        if(daftarCandi[i][1] == namaJin):
            cnt+=1
    return cnt
    
def hapusJin(): #Fungsi utama hapus candi
    while True : 
        namaJin = input("Masukkan username jin : ")
        if( cekUser(namaJin,userFile,panjangFile("user.csv"))) : 
            break 
        elif(namaJin == "Bondowoso"): 
            print("Tidak bisa menghapus Bandung Bondowoso")
        elif(namaJin == "Roro") : 
            print("Tidak bisa menghapus Roro Jonggrang")
        else : 
            print("Tidak ada jin dengan username tersebut.")
    while True :
        konfirmasiUser = input("Apakah anda yakin ingin menghapus jin dengan username " +namaJin + "(Y/N)? ")
        if(konfirmasiUser == "Y" or konfirmasiUser =="y") :
            break
        else : 
            return 0
    jumlahCandi = hitungCandi(namaJin)
    if jumlahCandi > 0 : 
       arrayCandiNew = hapusCandiCSV(namaJin,jumlahCandi,1)
       print(jumlahCandi)
       writeFile("candi.csv", arrayCandiNew, panjangFile("candi.csv")-jumlahCandi ,5)
    arrayNew = hapusJinCSV(namaJin)
    writeFile("user.csv", arrayNew, panjangFile("user.csv")-1 ,3)
    print("Jin "+ namaJin + " berhasil dihapus.")
    loadUserFile()
#End of Hitung Candi
    
def ayamBerkokok(): #Prosedur untuk Ayam Berkokok
    print("Kukuruyuk.. Kukuruyuk..\n")
    print("Jumlah candi : " + str(panjangFile("candi.csv") -1) +"\n")
    if(panjangFile("candi.csv") -1 == 100): 
        print("Yah, Bandung Bondowoso memenangkan permainan!")
    else : 
        
        print("Selamat, Roro Jonggrang memenangkan permainan!")
        print("\n")
        print("*Bandung Bondowoso angry noise* \nRoro Jonggrang dikutuk menjadi candi.")

#Fungsi dan Prosedur untuk Kumpul
def lcg(a : int , c: int, m: int ) -> int : #Fungsi untuk Random Number Generator (digunakan lcg)
    # X = (a*x + c) mod m 
    global seed 
    hasilLCG = (a*seed + c) % m
    seed = hasilLCG
    return hasilLCG %6

def Kumpul(jumlahJin:int): #Fungsi utama untuk kumpul
    global totalBatu, totalPasir, totalAir, bahanBangunan
    nPasir =0
    nBatu =0
    nAir = 0 
    
    for i in range(jumlahJin): 
        nPasir+=lcg(151811,3112,50603)
        nBatu +=lcg(151813,3112,50603)
        nAir  +=lcg(1518019,3112,50605)   
    
    totalBatu += nBatu
    totalAir += nAir
    totalPasir += nPasir
    print("Jin menemukan total " + str(nPasir) + " pasir "  + str(nBatu) + " batu " + str(nAir) + " air")
    arrayTemp = [["Pasir","sebuah pasir",str(nPasir)], ["Batu","sebuah batu", str(nBatu)], ["Air", "sebuah air", str(nAir)]]
    if(panjangFile("bahan_bangunan.csv") == 1): 
        print(bahanBangunan)
        arrayNew = initializeArray2(bahanBangunan,1, 3, arrayTemp, 3)
        writeFile("bahan_bangunan.csv", arrayNew, 4 , 3)
    else : 
        bahanBangunan[1][2] = str(totalPasir)
        bahanBangunan[2][2] = str(totalBatu)
        bahanBangunan[3][2] = str(totalAir)
        writeFile("bahan_bangunan.csv", bahanBangunan, panjangFile("bahan_bangunan.csv"),3)
    loadBahanBangunan()
#End of Kumpul



def hancurkanCandi(): #Prosedur untuk Hancurkan Candi
    while True : 
        idCandi = input("Masukkan id candi: ")
        if(cekId(idCandi)) : 
            break
        else : 
            print("Tidak ada candi dengan id  " +  idCandi)
    while True : 
        konfirmasiUser = input("Apakah anda yakin ingin menghancurkan candi ID: "+ idCandi+ "  (Y/N)? ") 
        if(konfirmasiUser == "y" or konfirmasiUser =="Y"): 
            break; 
        else: 
            return 0
    arrayNew = hapusCandiCSV(idCandi,1,0)
    writeFile("candi.csv", arrayNew, panjangFile("candi.csv")-1 ,5)
    print("Candi dengan id " + idCandi + " berhasil dihapus")
    loadDaftarCandi()
    
def Bangun(): 
    global totalPasir, totalBatu, totalAir, daftarCandi, bahanBangunan
    nPasir = lcg(151873,3112,50603)
    nBatu =lcg(151879,3112,50603)
    nAir = lcg(151837,3112,50603)
    print("Bahan yang diperlukan : " + str(nPasir) + " pasir, " + str(nBatu) + " batu, " + str(nAir) +" air")
    if(nPasir <= totalPasir and nAir <= totalAir and nBatu <= totalBatu): 
        print("Candi berhasil dibangun.")
        sisaCandi =100 - panjangFile("candi.csv") +1
        print("Sisa candi yang perlu dibangun: " + str(sisaCandi))
        totalPasir -= nPasir
        totalAir -= nAir
        totalBatu -= nBatu
        idCandi = 0
        for i in range(1,panjangFile("candi.csv")): 
            if(i == panjangFile("candi.csv") -1  or i != int(daftarCandi[i][0]) ): 
                idCandi = i
        arrayTemp = [str(idCandi), userName, str(nPasir), str(nBatu),str(nAir)]
        if(panjangFile("candi.csv") -1 < 100): 
            arrayNew = initializeArray(daftarCandi, panjangFile("candi.csv"),5, arrayTemp,1)
            writeFile("candi.csv", arrayNew, panjangFile("candi.csv") + 1, 5)
            bahanBangunan[1][2] = str(totalPasir)
            bahanBangunan[2][2] = str(totalBatu)
            bahanBangunan[3][2] = str(totalAir)
            writeFile("bahan_bangunan.csv", bahanBangunan, panjangFile("bahan_bangunan.csv"), 3)
            loadBahanBangunan()
            loadDaftarCandi()
        
    else  : 
        print("Bahan bangunan tidak mencukupi")
        print("Candi tidak bisa dibangun!")

# ===============================================================
# Bagian Laporan Candi
# ===============================================================
def hitungHarga(id:str): 
    for i in range(panjangFile("candi.csv")):
        if(daftarCandi[i][0] == id ): 
            return 10000 * int(daftarCandi[i][2]) + 15000 * int(daftarCandi[i][3]) + int(daftarCandi[i][4]) * 7500
def candiTermahal():
    idCandi = daftarCandi[1][0]
    for i in range(2, panjangFile("candi.csv")):
        if(hitungHarga(daftarCandi[i][0]) > hitungHarga(idCandi)): 
            idCandi = daftarCandi[i][0]
    return idCandi

def candiTermurah():
    idCandi = daftarCandi[1][0]
    for i in range(2, panjangFile("candi.csv")):
        if(hitungHarga(daftarCandi[i][0]) < hitungHarga(idCandi)): 
            idCandi = daftarCandi[i][0]
    return idCandi

def laporanCandi(): 
    if(userName != "Bondowoso"): 
        print("Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.")
        return 0
    
    totalBatuUse = getTotal(3)
    totalAirUse = getTotal(4)
    totalPasirUse = getTotal(2)
    idCandiTermahal = candiTermahal()
    idCandiTermurah = candiTermurah()
    print("> Total Candi : " + str(panjangFile("candi.csv") -1  ))
    print("> Total Pasir yang diperlukan : " + str(totalPasirUse))
    print("> Total Batu yang digunakan : " + str(totalBatuUse))
    print("> Total Air yang digunakna : " + str(totalAirUse))
    if( panjangFile("candi.csv")  > 2): 
        print("> Id Candi termahal : " + idCandiTermahal + " (Rp %d)"%(hitungHarga(idCandiTermahal)))
        print("> Id Candi termurah : " + idCandiTermurah + " (Rp %d)"%(hitungHarga(idCandiTermurah)))
    else: 
        print("> Id Candi termahal :  -")
        print("> id Candi termurah :  -")
# ---------------------------------------------------------------- 

# ===============================================================
# Bagian Laporan Jin
# ===============================================================
def jinTermalas()-> str: # Mencari jin termalas
    minCandi = 999
    jinMalas= ""  
    for i in range(3,panjangFile("user.csv")): 
        if(userFile[i][2] == "Pembangun"): 
            tmp = menghitungJumlahCandi(userFile[i][0])
            if(minCandi > tmp):
                minCandi = tmp
                jinMalas = userFile[i][0]
            elif(minCandi == tmp): 
                jinMalas = bandingkanNamaMalas(jinMalas, userFile[i][0])
    return jinMalas

def bandingkanNamaRajin(userNameJin1 : str, userNameJin2:str)->str: # Membandingkan nama untuk cari jin termalas
    jinRajin = userNameJin1
    for i in range(minimum(len(userNameJin1), len(userNameJin2))): 
        if(userNameJin1[i] < userNameJin2[i]): 
            break
        elif(userNameJin1[i] > userNameJin2[i]):
            jinRajin = userNameJin2
            break
    return jinRajin

def bandingkanNamaMalas(userNameJin1 : str, userNameJin2:str)->str: # Membandingkan nama untuk cari jin terajin
    jinMalas = userNameJin1
    for i in range(minimum(len(userNameJin1), len(userNameJin2))): 
        if(userNameJin1[i] > userNameJin2[i]): 
            break
        elif(userNameJin1[i] < userNameJin2[i]):
            jinMalas = userNameJin2
            break
    return jinMalas

def jinTerajin()->str: #Mencari jin terajin
    maxCandi = -999  
    jinRajin = ""  
    for i in range(3,panjangFile("user.csv")): 
        if(userFile[i][2] == "Pembangun"): 
            tmp = menghitungJumlahCandi(userFile[i][0])
            if(maxCandi < tmp):
                maxCandi = tmp
                jinRajin = userFile[i][0]
            if(maxCandi == tmp): 
                jinRajin = bandingkanNamaRajin(jinRajin, userFile[i][0])
    return jinRajin

def jumlahJin(tipeJin : str)->int: # Mencari jumlah jin berdasarkan tipenya (Pembangun/Pengumpul)
    cnt = 0  
    for i in range(panjangFile("user.csv")): 
        if(userFile[i][2] == tipeJin): 
            cnt+=1
    return cnt

def menghitungJumlahCandi(userNameJin : str)->int : #Menghitung jumlah candi yang dibangun oleh "userNameJin"
    cnt = 0
    for i in range(1,panjangFile("candi.csv")): 
        if(daftarCandi[i][1] == userNameJin):
            cnt +=1 
    return cnt 

def laporanJin(): #Laporan Jin Utama
    if(userName !=  "Bondowoso"):
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
        return 0
    jinterajin :str = "-"
    jintermalas:str ="-"
    totalJinPengumpul : int = jumlahJin("Pengumpul") 
    totalJinPembangun  : int =  jumlahJin("Pembangun")
    totalJin =  totalJinPembangun + totalJinPengumpul
    if(panjangFile("user.csv") >= 6 ): 
        jinterajin = jinTerajin()
        jintermalas = jinTermalas()
    print("> Total jin : " + str(totalJin))
    print("> Total jin Pengumpul : " + str(totalJinPengumpul))
    print("> Total jin Pembangun : " + str(totalJinPembangun))
    print("> Jin Terajin: "  + jinterajin)
    print("> Jin Termalas: " + jintermalas)
    print("> Jumlah Pasir: " + str(totalPasir) +  " unit")
    print("> Jumlah Air: " + str(totalAir) +  " unit" ) 
    print("> Jumlah Batu: " + str(totalBatu) +  " unit")    
# ---------------------------------------------------------------- 


# ===============================================================
# Bagian untuk Exit
# ===============================================================
def Exit(): #Prosedur untuk Exit
    panjangFileUser = panjangFile("user.csv")
    panjangFileBahan = panjangFile("bahan_bangunan.csv")
    panjangFIleCandi = panjangFile("candi.csv")
    while True :
        konfirmasiUser = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        if(konfirmasiUser == "Y" or konfirmasiUser =="y"): 
            writeFile("user.csv", userFile , panjangFileUser,3 )
            writeFile("bahan_bangunan.csv",bahanBangunan, panjangFileBahan,3 )
            writeFile("candi.csv", daftarCandi, panjangFIleCandi,5 )
            break
        elif(konfirmasiUser == "n" or konfirmasiUser =="N") : 
            break
    sys.exit()
# ---------------------------------------------------------------- 

def getTipeJin(userName: str) -> str : 
    for i in range(panjangFile("user.csv")): 
        if userFile[i][0] == userName : 
            return userFile[i][2]
    
def Help(): #Prosedur untuk Help
    print("=========== HELP ===========")
    if(userName == "" and userPass == ""): 
        print("1. Login")
        print("   Untuk masuk menggunakan akun")
        print("2. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    elif(userName == "Bondowoso"): 
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
        print("3. hapusjin")
        print("   Untuk menghapus\menghilangkan jin")
        print("4. laporanjin")
        print("   Untuk melihat laporan mengenai jin yang ada")
        print("5. laporancandi")
        print("   Untuk melihat laporan mengenai candi yang sudah dibangun")
        print("6. batchkumpul")
        print("   Mengerahkan semua jin Pengumpul untuk mengumpulkan bahan")
        print("7. batchbangun")
        print("   Mengerahkan semua jin Pembangun untuk membangun banyak candi")
        print("8. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    elif(userName == "Roro") : 
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang tersedia")
        print("3. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    elif(getTipeJin(userName) == "Pembangun"): 
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. bangun")
        print("   Untuk membangun candi")
        print("3. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    elif(getTipeJin(userName) == "Pengumpul"): 
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan bahan candi")
        print("3. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
#Program Utama
memintaArgs()
print("Loading...")
print('Selamat datang di program "Manajerial Candi" ')

loadUserFile()
loadBahanBangunan()
loadDaftarCandi()

while sedangBerjalan : 
    x = input(">>>> ")
    switch(x) 
