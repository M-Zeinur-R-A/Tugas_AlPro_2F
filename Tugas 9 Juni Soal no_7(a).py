# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 00:58:03 2021

@author: Muhammad Zeinur Rosyid Arkham_2F
NIM    : 20083000129 
"""

#cek kelulusan, jika nilai > 60 maka status Lulus
ulangi = "y"
while ulangi=="y" or ulangi=="Y":
    print ("===========================")
    print (" CEK KELULUSAN Soal no.7(a)")
    print ("===========================")

    n = input(">> Masukkan Nilai = ")

    if int(n)>60:
        sts = "LULUS"
    else:
        sts = "TIDAK LULUS"
    if int(n)>100:
        sts = "Melebihi nilai Maksimal yang di tentukan!!"
    print(sts)

    #break
    ulangi = input(">> Cek Ulang/lagi ? y/t = ")
    if ulangi== "t" or ulangi =="T":
        break