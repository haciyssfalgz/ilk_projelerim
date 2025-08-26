while True:
    ilksayı = input ("ilksayıyı gir ")
    islem = input ( "işlem türünü gir ")
    ikincisy = input ("ikinci sayıyı gir ")
    if islem == "+":    
        sonuç= int(ilksayı) + int(ikincisy)
        print("=", sonuç)
    elif islem == "-":
        sonuç= int(ilksayı) - int(ikincisy)
        print("=", sonuç)
    elif islem == "*":
        sonuç= int(ilksayı) * int(ikincisy)
        print("=", sonuç)
    elif islem == "/":
        sonuç= int(ilksayı) / int(ikincisy)
        print("=", sonuç)
    else :
        print("yok böyle bişey!!!")