#Program Test
#Mengkonversi suhu

#KAMUS
tK=float
tC=float
tF=float
tR=float
#ALGORITMA
suhu  = float(input("Masukkan suhu = "))
satuan = input("masukkan satuan suhu (dalam tC,tF,tR,tK) = ")

if (satuan == "tC") :
   tK = suhu + 273.15
   print("Suhu dalam satuan kelvin= ",tK,"K")
   tF = 9/5*suhu + 32
   print("Suhu dalam satuan derajat fahrenheit= ",tF,"F")
   tR = 4/5*suhu
   print("Suhu dalam satuan derajat reamur",tR,"R")

elif (satuan == "tF") :
    tK = 5/9*(suhu - 32) + 273.15
    print("Suhu dalam satuan kelvin= ",tK,"K")
    tR = 4/9*(suhu - 32)
    print("Suhu dalam satuan derajat reamur= ",tR,"R")
    tC = 5/9*(suhu - 32)
    print("Suhu dalam satuan derajat celcius= ",tC,"C")

elif (satuan == "tR") :
    tK = 5/4*(suhu) + 273.15
    print("Suhu dalam satuan kelvin= ",tK,"K")
    tF = 9/4*suhu + 32
    print("Suhu dalam satuan derajat fahrenheit= ",tF,"F")
    tC = 5/4*suhu
    print("Suhu dalam satuan derajat celcius= ",tC,"C")

elif (satuan == "tK") :
    tF = 9/5*(suhu - 273.15) + 32
    print("Suhu dalam satuan fahrenheit= ",tF,"F")
    tR = 4/5*(suhu - 273.15)
    print("Suhu dalam satuan derajat reamur= ",tR,"R")
    tC = suhu - 273.15
    print("Suhu dalam satuan derajat celcius= ",tC,"C")