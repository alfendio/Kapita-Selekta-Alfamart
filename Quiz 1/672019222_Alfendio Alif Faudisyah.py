"""
  Alfendio Alif Faudisyah
  672019222
"""

kalimatPertama =  "Saya sedang belajar Bahasa Pemrograman Python"
kalimatKedua = "di Minggu Ke-"
mingguKe = 2
dataPertama = {'nama':'Budi', 'nik':1234567, 'periode': 2022}

print ("1.", kalimatPertama[20:].lower())

print ("2. %s %s%s" % (kalimatPertama, kalimatKedua, mingguKe))

print ("3. %s %s%s %s %s %s %s" % (kalimatPertama[0:4], kalimatKedua, mingguKe, kalimatPertama[12:19].capitalize(), kalimatPertama[20:26].capitalize(), kalimatPertama[27:38].capitalize(), kalimatPertama[39:].upper()))

print ("4.", kalimatPertama.split())

listKalimatPertama = kalimatPertama.split()

var1 = listKalimatPertama [0]

var2 = listKalimatPertama [1]

var3 = listKalimatPertama [2]

var4 = listKalimatPertama [3]

var5 = listKalimatPertama [4]

var6 = listKalimatPertama [5]

print ("5.", var1, var2, var3, var4, var5, var6)

listKalimatPertamaCopy = listKalimatPertama.copy()   

del listKalimatPertama[3:5]                

listKalimatPertamaBaru = [x for x in listKalimatPertamaCopy if x not in listKalimatPertama] 

print ("6.", listKalimatPertamaBaru)

listKalimatPertama.append(kalimatKedua)

listKalimatPertama.append(mingguKe)

print ("7.", listKalimatPertama, "Panjang = ", len(listKalimatPertama))

print ("8.", listKalimatPertama[0], listKalimatPertama[1], listKalimatPertama[2], listKalimatPertama[4], listKalimatPertama[5])

tupleKalimat = ('Saya', 'sedang', 'belajar', 'Bahasa', 'Pemrograman', 'Python', 'di Minggu Ke-', 2)

print ("9.", tupleKalimat)

dataPertama['umur'] = 20

print("10.", dataPertama)

dataPertama.update({'nik': 2021345})

print("11.", dataPertama)
