# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 01:36:21 2021

@author:  Muhammad Zeinur Rosyid Arkham_2F
NIM    : 20083000129
"""
#Penilaian mahasiswa akan mendapat nilai huruf X 
ulangi = "y"
while ulangi=="y" or ulangi=="Y":
    print ("===================================")
    print (" Penilaian mahasiswa Soal no. 7(d) ")
    print ("===================================")
    u=1
    while int(u)>0 and int(u)<=100:
        u = input(">> Masukkan Nilai = ")

        if int(u)>0 and int(u)<=100:
            if int(u)>=91 and int(u)<100: 
                sts=">> A <<"
            elif int(u)>=81 and int(u)<91: sts=">> B <<"
            elif int(u)>=71 and int(u)<81: sts=">> C <<"
            elif int(u)<=71: sts=">> D <<"
            print (sts)

            ulangi = input(">>> Ulang cek Nilai? y/t = ")
            if ulangi=="t" or ulangi=="T":
                break
        else:
            sts=">>> Nilai hanya terbatas 0-100 <<<"
            print(sts)
            break
