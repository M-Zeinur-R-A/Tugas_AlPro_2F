# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 06:38:45 2021

@author: Muhammad Zeinur Rosyid Arkham_2F
NIM    : 20083000129 
"""
#Hitung nilai total transaksi pembelian Printer Epson T20
ulangi = "y"
while ulangi=="y" or ulangi=="Y":
    print("====================================================")
    print(" Hitung nilai total transaksi pembelian Soal no.8(b)")
    print("====================================================")
    
    hargaprinter = int(660000)
    jumlahprinter = int(input(">>Masukkan jumlah yang di beli = "))
    hargatotal = hargaprinter*jumlahprinter
    
    print("Harga Printer", + hargaprinter)
    print("Total harga = Rp." , int(hargatotal))
    
    ulangi = input(">>> Hitung pembelian lainnya? y/t = ")
    if ulangi=="t" or ulangi=="T":
        break