import requests
from bs4 import BeautifulSoup
def getKode_Nama(url):
    data = requests.get(url)

    soup = BeautifulSoup(data.text,'html.parser')

    nama_kpp = soup.find_all('td',valign='top')
    nama = []
    for i in nama_kpp:
        if(i.h4 != None):
            nama.append(str(i.h4)[4:-5])
            
            
    kode = []
    span = soup.find_all('span',id='tanggal')
    for i in span:
        kpp = str(i).split(';')[1]
        kode.append(kpp[12:-7])
    return kode,nama
#file = open('e:/xampp/htdocs/ezRegex/kode_KPP.csv','w')
#file.write('KODE_KPP,NAMA_KPP\n')
for i in range(1,60):
    
    url = 'https://ortax.org/ortax/?mod=kpp&f=sp&nama=&camat=&search_kat=kpp&form=kpp_search&lurah=&page=list&hlm={}'.format(str(i))
    x,y = getKode_Nama(url)
    for i in range(len(x)):
        print(x[i]+","+y[i]+"\n")
        #file.write(x[i]+","+y[i]+"\n")
print("DONE")

