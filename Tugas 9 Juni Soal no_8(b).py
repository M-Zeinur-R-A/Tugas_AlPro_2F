# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 07:31:25 2021

@author: Muhammad Zeinur Rosyid Arkham_2F
NIM    : 20083000129 
"""
#Hitung nilai total transaksi pembelian Printer Epson T20
#Jika nilai pembelian di atas Rp 1,5 juta, diberikan diskon 15%
ulangi = "y"
while ulangi=="y" or ulangi=="Y":
    print("====================================================")
    print(" Hitung nilai total transaksi pembelian Soal no.8(b)")
    print("====================================================")
    
    hargaprinter = int(660000)
    jumlahprinter = int(input(">>Masukkan jumlah yang di beli = "))
    hargatotal = hargaprinter*jumlahprinter
    
    if int(hargatotal)>1500000:
        Diskon = hargatotal*15/100
        Total = hargatotal-Diskon
    
    print("Harga Printer        = Rp.", + hargaprinter)
    print("Total harga          = Rp.", + hargatotal)
    print("Diskon 15%           = Rp.", + Diskon)
    print("Total harga + Diskon = Rp.", int(Total))

    
    ulangi = input(">>> Hitung pembelian lainnya? y/t = ")
    if ulangi=="t" or ulangi=="T":
        break