"""
ini adalah demo project pertama dengan python

semua sintaksis dasar bahasa pemrograman terdiri dari :
1.sekuensial : langkah berurutan
2.percabangan : langkah melompat jika kondisi terpenuhi
3.perulangan : mengulang langkah yang sama berkali kali selama/sampai konidisi terpenuhi
"""

# sekuensial
print('ibu berkata "pergi ke toko"')
print('budi menjawab "apa yang harus saya lakukan di toko"')
print('ibu menjawab "beli satu botol susu,dan jika ada telor beli 6"')
print('dan budi berangkat ke toko')
print('dan mulai berbelanja')


# percabangan
print('=======')
#var adalah tempat menyimpan data
jumlah_botol_susu = 173

# ada proses indentasi yaitu tab,yang menandakan bahwa itu milik if
# karena perintah yg sebelumnya itu benar
if jumlah_botol_susu > 0:
    print("yuda beli botol susu")
else:
    print('budi tidak jadi membeli 1 botol susu')