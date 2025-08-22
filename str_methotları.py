msg = "ali ip atla Veli ip katla. koş zıp Hopla Oyna"  
sonuc1 = msg.upper() #bütün harfleri büyük yapar
print("sonuc1")
print(sonuc1)
sonuc2 = msg.lower() #bütün harfleri küçük yapar
print("sonuc2")
print(sonuc2)
sonuc3 = msg.title() #her kelimenin ilk harfini büyük yapar
print("sonuc3")
print(sonuc3)
sonuc4 = msg.capitalize() #sadece ilk harfi büyük yapar
print("sonuc4")
print(sonuc4)
sonuc5 = msg.split() #boşluklardan ayırır ve liste yapar
print("sonuc5")
print(sonuc5)
print(type(sonuc5)) #liste olduğunu gösterir
print(sonuc5[3]) #liste içinden 3. elemanı yazdırır
sonuc6 = "-".join(sonuc5) #liste elemanlarını - ile birleştirir
print("sonuc6")
print(sonuc6)
sonuç7 = msg.split(".") #a harfine göre ayırır
print("sonuc7")
print(sonuç7)
sonuc8 = "     deneme yapmak    ".strip() #başındaki ve sonundaki boşlukları siler
print("sonuc8")
print(sonuc8)
sonuc9 = msg.index("katla")  #katla kelimesinin başladığı indexi verir
print("sonuc9")
print(sonuc9)
sonuc10 = msg.find("ip") #ip kelimesinin başladığı indexi verir
print("sonuc10")
print(sonuc10)
sonuc11 = msg.rfind("ip") #ip kelimesinin başladığı indexi sondan başlayarak verir  
print("sonuc11")
print(sonuc11)
sonuc12 = msg.count("ip") #ip kelimesinin kaç kere geçtiğini verir
print("sonuc12")
print(sonuc12)
sonuc13 = msg.startswith("ali") #ali ile başlayıp başlamadığını kontrol eder
print("sonuc13")
print(sonuc13)
sonuc14 = msg.startswith("veli") #veli ile başlayıp başlamadığını kontrol eder
print("sonuc14")
print(sonuc14)
sonuc15 = msg.endswith("Oyna") #oyna ile bitip bitmediğini  kontrol eder
print("sonuc15")
print(sonuc15)
sonuc16 = msg.endswith("hopla") #hopla ile bitip bitmediğini  kontrol eder
print("sonuc16")
print(sonuc16)
sonuc17 = msg.replace("ip","top") #ip kelimesini top ile değiştirir
print("sonuc17")
print(sonuc17)
sonuc18 = msg.replace(" ","-") #boşlukları - ile değiştirir
print("sonuc18")
print(sonuc18)
sonuc19 = msg.center(100,"*") #mesajı 100 karaktere tamamlar ve ortalar, boşlukları * ile doldurur
print("sonuc19")
print(sonuc19)
#teşekkürler Sadık Turan