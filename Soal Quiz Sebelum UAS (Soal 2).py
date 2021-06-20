# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 18:36:53 2021

@author: Muhammad Zeinur Rosyid Arkham_2F
NIM    : 20083000129 
"""

#Soal 2 Transaksi Oli
ulangi = "y"
while ulangi=="y" or ulangi=="Y":
    print ("===========================================")
    print ("                Daftar Harga Oli           ")
    print ("-------------------------------------------")
    print (" a. Duration SW20 1L        @ Rp53.000     ")
    print (" b. Castrol Magnatec 1L     @ Rp50.000     ")
    print (" c. Federal Supreme XX 1L   @ Rp54.000     ")
    print (" d. Yamalube 1L             @ Rp45.000     ")
    print (" e. Shell 1L                @ Rp46.000     ")
    print ("                                           ")
    print (" @Created by: Muhammad Zeinur Rosyid Arkham")
    print ("              20083000129 - 2F             ")
    print ("===========================================")

    kode =['a','b','c','d','e']
    Merk = ['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L']
    Harga = [53000,50000,54000,45000,46000]
    
    pilihan = input("=> Masukkan Kode Pilihan = ")
    
    if pilihan=="a" or pilihan=="A":
        idx = 0
    elif pilihan=="b" or pilihan=="B":
        idx = 1
    elif pilihan=="c" or pilihan=="C":
        idx = 2
    elif pilihan=="d" or pilihan=="D":
        idx = 3
    elif pilihan=="e" or pilihan=="E":
        idx = 4
    else:
        print("=> Kode tidak diketahui, Maka pilihan kode 'a' sebagai (default)")
        idx = 0
    
    jumlah  = int(input("=> Masukkan jumlah yang ingin di beli = "))
    
    print ("===========================================")
    print ("==> Merk Oli       = " + Merk[idx])
    print ("==> Harga          = Rp. " + str(Harga[idx]))
    
    fixJumlah = jumlah
    fixHarga = Harga[idx]
    totHarga = fixJumlah * fixHarga
    hdiskon = totHarga * (5/100)
            
    if int(totHarga)>=200000:
        totBiaya = totHarga - hdiskon
        PPN = totBiaya * (1/100)
        totalAkhir = totBiaya - PPN
    else:
        hdiskon = 0
        PPN = totHarga * (1/100)
        totalAkhir = totHarga - PPN
            
    print("==> Diskon          = Rp. " + str(hdiskon))
    print("==> PPN             = Rp. " + str(PPN))
    print("==>|---------------------------------------")
    print("==> Total Biaya     = Rp. " + str(totalAkhir))

    ulangi = input(">> Hitung Transaksi lagi ? y/t = ")
    if ulangi== "t" or ulangi =="T":
        break