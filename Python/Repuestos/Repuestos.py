class Repuestos:

    nombre = ""
    ingresos = 0.0
    egresos = 0.0
    marca = ""
    ganancias = 0


    def __init__(self, nom,ingr,en,mar):
        self.nombre = nom
        self.ingresos = ingr
        self.egresos =  en
        self.marca = mar




    def establecerNombre(self,n):
        self.nombre = n
    def obtenerNombre(self):
        return self.nombre
    def establecerIngresos(self, n):
        self.Ingresos = n
    def obtenerIngresos(self):
        return self.ingresos
    def establecerEgresos(self,n):
        self.Egresos = n
    def obtenerEgresos(self):
        return self.egresos
    def establecerMarca(self,n):
        self.marca = n
    def obtenerMarca(self):
        return self.marca


rep = Repuestos("Jaramillo",1000,750,"Chevrolet")

nombre = rep.obtenerNombre()
ingresos = rep.obtenerIngresos()
egresos = rep.obtenerEgresos()
marca = rep.obtenerMarca()
ganancias = ingresos - egresos

print("Repuestos: "+nombre+" \nIngresos: "+str(ingresos)+"$"+" \nEgresos: "+str(egresos)+"$"+" \nMarca:"+marca+ "\nGanacias: "+str(ganancias)+"$")