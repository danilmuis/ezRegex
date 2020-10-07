import xlrd
from os.path import join, dirname, abspath
import pandas as pd
fname = join(dirname(dirname(abspath(__file__))),'DATA DAERAH\\' 'notes_kode_kantor.xlsx')
print(fname)
hasil = open('e:/Works/Magang Pegadaian/DATA DAERAH/hasil.txt','a')
data = open('e:/Works/Magang Pegadaian/DATA DAERAH/data.txt','a')

#file = pd.read_csv('e:/Works/Magang Pegadaian/DATA DAERAH/notes_kode_kantor.csv',sep=';')

file = pd.read_excel('e:/Works/Magang Pegadaian/DATA DAERAH/kode KPP_NPWP.xlsx')
#kode = file['KODE_KANTOR']
array = []
# for i in range (len(file['NAMA_KANTOR'])):
    #data.write(str(i)+'\n')
    #if("CBM" in file['NAMA_KANTOR'][i] or "UBM" in file['NAMA_KANTOR'][i]):
    #    array.append(str(file['KODE_KANTOR'][i]))
    
    # if(len(file['KODE_KANTOR'][i]) == 5 ):
    #     try:
    #         x = int(file['KODE_KANTOR'][i])
    #         array.append(str(file['KODE_KANTOR'][i]))
    #     except:
    #         print("NOT INT : "+file['KODE_KANTOR'][i])
    
    
    # if(len(file['KODE_KANTOR'][i]) == 3 ):
    #     array.append(str(file['KODE_KANTOR'][i]))
    # try:
    #     x = int(file['KODE_KANTOR'][i])
        
    # except:
    #     array.append(str(file['KODE_KANTOR'][i]))

for i in range(len(file['Kode KPP'])):
    if(file['Column1'][i] == 'KPP'):
        array.append(str(int(file['Kode KPP'][i])).zfill(3))
print((array))









#data.write(array)
#print(kode.str.contains("10000").any())      
#print(file['NAMA_KANTOR'][0])
def cek(x,y):
    data = []
    for i in range(x,y+1):
        if(not kode.str.contains(str(i)).any()):
            hasil.write(str(i)+'\n')

#cek(10001,14420)
#cek(60001,61052)