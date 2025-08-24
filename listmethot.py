urunler = ["mersedes", "bmw", "audi", "ferrari"]
print("urunler")
print(urunler)
urunler.append ("tofas")
print("append")
print(urunler)
urunler.insert(len(urunler),"renault")
print("insert")
print(urunler)
urunler.remove("tofas")
print("remove")
print(urunler)
del urunler[2]
print("del")
print(urunler)
urunler.pop()
print("pop")
print(urunler)
urunler2 = urunler.copy()
print("copy")
urunler2[2] = "opel"
print(urunler2)
print(urunler)

urunler.extend(urunler2)
print("extend")
print(urunler)
print("clear")
print(urunler.clear())
urunler = ["mersedes", "bmw", "audi", "ferrari"]
del urunler[::]
print("del")
print(urunler)