class kendaraan: 
  def __init__(self, jenisKendaraan): 
    self.jenisKendaraan = jenisKendaraan 

class rodaDua(kendaraan): 
  def __init__(self, jenisKendaraan):
    super().__init__(jenisKendaraan) 

class rodaEmpat(kendaraan): 
  def __init__(self, jenisKendaraan):
    super().__init__(jenisKendaraan) 

kendaraanRodaDua = rodaDua('Honda-Alfendio') 
print(kendaraanRodaDua.jenisKendaraan) 

kendaraanRodaEmpat = rodaEmpat('Toyota-Alif')
print(kendaraanRodaEmpat.jenisKendaraan)