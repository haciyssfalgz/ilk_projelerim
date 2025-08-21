urun_adi = "elma "
fiyat= 15 
miktar = 5.0

sonuç1 = str(miktar) + " kilo "+ urun_adi +" için " + str(miktar*fiyat) + " tl öde"

print(sonuç1)

sonuç2 = "{2} kilo {0} için {1} tl öde".format(urun_adi,(fiyat*miktar),miktar)

print(sonuç2)

sonuç3 = "{m} kilo {u} için {tf} tl öde".format( m = miktar, u = urun_adi, tf = (fiyat*miktar))

print(sonuç3)

sonuç4 = "{} kilo {} için {} tl öde".format(miktar,urun_adi,(fiyat*miktar))

print(sonuç4)

sonuç5 = f"{miktar} kilo {urun_adi} için {miktar*fiyat} tl öde"

print(sonuç5)
print(sonuç1,sonuç2,sonuç3,sonuç4,sonuç5)#en son hepsi yanyana yazacak
