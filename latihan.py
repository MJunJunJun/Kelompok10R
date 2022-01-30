def jumlah(a,b):
    c=a+b
    return c

hasil=jumlah(3,2)
#print(hasil)


kali=lambda x,y: x*y
print(kali(3,4))


lamaInvestasi = lambda target,uangSetor : target/uangSetor
lama=lamaInvestasi(100000,12)
print(lama)


rugiUntung = lambda jumlahLot,hargaBeli,hargaJual : hargaJual*jumlahLot-hargaBeli*jumlahLot

jual=rugiUntung(10,2000,3000)
print(jual)

for i in range(1,10):
    print(i)