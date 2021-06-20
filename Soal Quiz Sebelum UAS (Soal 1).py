# -*- coding: utf-8 -*-
"""
Edited on Sun Jun 20 16:58:56 2021
@Editor: Muhammad Zeinur Rosyid Arkham_2F
NIM    : 20083000129
Buat program untuk menghitung biaya total pengiriman barang di perusahaan Ekspedisi
Lorena di Malang
1. set variabel kota, jarak, ongkirperkm, totongkir
2. input pilihan kota
3. jika kota Sby, jarak = 169, ongkirperkm=2500, selain itu
jika kota Bdg, jarak = 452, ongkirperkm=4000
4. totongkir = jarak * ongkirperkm
5. tampilkan kota, totongkir
"""
ulangi = "y"
while ulangi=="y" or ulangi=="Y":
    print ("=============================================")
    print ("= TRANSKASI BIAYA EKSPEDISI                 =")
    print ("=============================================")
    print ("= Kode = A. Surabaya                        =")
    print ("= Kode = B. Bandung   @Edited by [Zein-2F]  =")
    print ("=============================================")

    #jika menggunakan list Kode dibawah ini, maka metode yang digunakan
    #adalah mendeteksi indeks value yang terpilih pada list kode.
    #caranya: melakukan pencarian pada list kode menggunakan 
    # nilai kode yang diinputkan
    #salah satu metode : gunakan while
    kode =['a','b']
    #algoritma:
        # baca berulang2 index dalam list kode, jika value sama dengan 
        # value pilihan, ambil index nya
        
    kota = ['surabaya','bandung']
    jarak = [169,452]
    ongkirperkm = [2500,4000]
    
    pilihan = input(">> Masukkan Kode Tujuan = ")
    #identifikasi pilihan
    if pilihan=="a":
        idx = 0
    elif pilihan=="b":
        idx = 1
    else:
        idx = 0

    #cetak tampilan layar
    print(">>> Pilihan Tujuan = " + kota[idx])
    print(">>> Jarak          = " + str(jarak[idx]) + " km")
    print(">>> Ongkir per km  = Rp. " + str(ongkirperkm[idx]))
    
    #hitung transksi
    fixjarak = jarak[idx]
    fixongkirkm = ongkirperkm[idx]
    totongkir = fixjarak * fixongkirkm
    
    #tampilkan total ongkir
    print(">>>-------------------------------------")
    print(">>> Total Biaya     = Rp." + str(totongkir))
    #break
    ulangi = input(">> Hitung Lagi ? y/t = ")
    if ulangi== "t" or ulangi =="T":
        break