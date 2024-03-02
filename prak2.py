class Retangle:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def luas (self):
        return self.panjang * self.lebar
    
    def keliling (self):
        return (self.panjang * self.lebar) * 2
    
persegi = Retangle (10, 5)

print(persegi.luas())
print(persegi.keliling())