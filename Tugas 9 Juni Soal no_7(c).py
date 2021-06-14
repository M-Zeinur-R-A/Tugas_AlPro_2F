# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 01:20:23 2021

@author: Muhammad Zeinur Rosyid Arkham_2F
NIM    : 20083000129
"""

#Menampilkan nilai huruf dengan Menginputkan sebuah bilangan bulat dari 0-100.
ulangi = "y"
while ulangi=="y" or ulangi=="Y":
    print ("=================================")
    print (" MENAMPILKAN NILAI Soal no. 7(c) ")
    print ("=================================")
    u=1
    while int(u)>0 and int(u)<=100:
        u = input(">> Masukkan Nilai = ")

        if int(u)>0 and int(u)<=100:
            if int(u)>=80: 
                sts=">> Baik Sekali <<"
            elif int(u)>=65: sts=">> Baik <<"
            elif int(u)>=55: sts=">> Cukup <<"
            elif int(u)>=40: sts=">> Kurang <<"
            else:
                sts="Kurang Sekali"
            print (sts)

            ulangi = input(">>> Ulang cek Nilai? y/t = ")
            if ulangi=="t" or ulangi=="T":
                break
        else:
            sts=">>> Nilai hanya terbatas 0-100 <<<"
            print(sts)
            break