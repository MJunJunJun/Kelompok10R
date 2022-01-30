from math import ceil
from browser import document, alert, console

# Deklarasi Variable
input1 = document['input1']
input2 = document['input2']
input3 = document['input3']
input4 = document['input4']
input5 = document['input5']
button1 = document['btn1']
button2 = document['btn2']
output1 = document['output1']
output2 = document['output2']


input = {'1': input1,
         '2': input2,
         '3': input3,
         '4': input4,
         '5': input5}

#typee = {'lamaInvestasi':  {'formula': lambda target,uangSetor : target/uangSetor, 'input1':  'Target Investasi', 'input2': 'Jumlah uang perbulan'},
#       'untungRugi':  {'formula': lambda hargaBeli,hargaJual, jumlahLot : hargaJual*jumlahLot-hargaBeli*jumlahLot, 'input3':  'Harga beli', 'input4': 'Harga jual','input5': 'Jumlah Lot'}}



# Fungsi untuk mengubah string dari input ke int atau float
def getNum(x):
    console.log("Masuk INT")
    temp = x
    # Convert string ke int
    try:
        temp = int(x)
    # Jika convert string ke int gagal (ValueError), maka convert ke float
    except ValueError:
        temp = float(x)
    finally:
        # Jika input (var temp) masih string (gagal convert ke int dan float), 
        # maka munculkan alert dan return dengan variable kosong ('')
        if temp != '' and type(temp) is str:
            alert('Harap masukkan Jumlah')
            temp = ''
            input1.value = temp
            return temp
        # Jika salah satu convert berhasil, maka return
        else:
            return temp

# Fungsi untuk memanggil rumus pada dictionary



# Fungsi Main
# Dijalankan ketika button di-click atau tombol 'enter' ditekan
def lama(ev):
    num1 = getNum(input1.value)
    num2 = getNum(input2.value)
    #result = Rumus(selectType.value, num1, num2, num3, num4, num5)
    result1 = num1/num2
    pembulat= ceil(result1)
    output1.textContent = str(pembulat)
    console.log("Masuk")

def untungRugi(ev):
    num3 = getNum(input3.value)
    num4 = getNum(input4.value)
    num5 = getNum(input5.value)
    #result = Rumus(selectType.value, num1, num2, num3, num4, num5)
    result2 = (num4*num5*100)-(num3*num5*100)
    pembulat= ceil(result2)
    output2.textContent = str(pembulat)
    console.log("Masuk")



# Fugnsi keyEnter
# Fungsi yang mengarahkan ke 'Fungsi Main' ketika tombol 'enter' ditekan
def keyEnter1(ev):
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        lama(0)
def keyEnter2(ev):
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        untungRugi(0)



button1.bind('click', lama) # Memanggil 'Fungsi Main' ketika button di-click
button2.bind('click', untungRugi) # Memanggil 'Fungsi Main' ketika button di-click

# Mengarahakan ke 'Fungsi keyEnter' ketiak 'enter' ditekan pada salah satu input field
input1.bind("keypress", keyEnter1)
input2.bind("keypress", keyEnter1)
input3.bind("keypress", keyEnter2)
input4.bind("keypress", keyEnter2)
input5.bind("keypress", keyEnter2)