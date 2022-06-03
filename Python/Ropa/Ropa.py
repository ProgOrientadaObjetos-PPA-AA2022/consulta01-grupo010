class Ropa:

    nombre = ""
    camisetas = 0.0
    pantalones = 0.0
    chompas = 0.0
    valor = 0


    def __init__(self, nom,cam,pan,chomp):
        self.nombre = nom
        self.camisetas = cam
        self.pantalones =  pan
        self.chompas = chomp



    def establecerNombre(self,n):
        self.nombre = n
    def obtenerNombre(self):
        return self.nombre
    def establecerCamisetas(self, n):
        self.camisetas = n
    def obtenerCamisetas(self):
        return self.camisetas
    def establecerPantalones(self,n):
        self.pantalones = n
    def obtenerPantalones(self):
        return self.pantalones
    def establecerChompas(self,n):
        self.chompas = n
    def obtenerChompas(self):
        return self.chompas


ropa = Ropa("RM,",35,40,63)

nombre = ropa.obtenerNombre()
camisetas = ropa.obtenerCamisetas()
pantalones = ropa.obtenerPantalones()
chompas = ropa.obtenerChompas()
valor = camisetas + pantalones + chompas
valort = valor * 0.12
valort = valor + valort

print("Tienda de Ropa: "+nombre+" \nValor de Camisetas: "+str(camisetas)+"$"+" \nValor de Pantalones: "+str(pantalones)+"$"+" \nValor de Chompas:"+str(chompas)+"$"+"\nValor a Pagar sin Iva: "+str(valor)+"$"+"\nValor Total a Pagar: "+str(valort)+"$")
