# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 01:10:06 2021

@author: Muhammad Zeinur Rosyid Arkham_2F
NIM    : 20083000129
"""

#cek golongan usia
ulangi = "y"
while ulangi=="y" or ulangi=="Y":
    print ("=================================")
    print (" CEK GOLONGAN USIA Soal no. 7(b) ")
    print ("=================================")
    u=1
    while int(u)>0 and int(u)<=100:
        u = input(">> Masukkan Usia = ")

        if int(u)>0 and int(u)<=100:
            if int(u)>=60: 
                sts="Lansia"
            elif int(u)>=35 and int(u)<59: sts="Dewasa"
            elif int(u)>=18 and int(u)<34: sts="Pemuda"
            elif int(u)>=15 and int(u)<17: sts="Remaja"
            else:
                sts="Anak-anak"
            print (sts)

            ulangi = input(">>> Ulang cek usia? y/t = ")
            if ulangi=="t" or ulangi=="T":
                break
        else:
            sts=">>> Usia terbatas hanya terbatas 0-100"
            print(sts)
            break
    