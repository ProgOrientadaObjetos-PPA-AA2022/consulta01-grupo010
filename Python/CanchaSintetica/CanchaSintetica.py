


class CanchaSintetica:

    nombre = ""
    Horario = ""
    capacidad = 0.0
    ubicacion = ""
    Valor = 0

    def __init__(self, nom,ho,cap,ubi, val):
        self.nombre = nom
        self.Horario = ho
        self.capacidad = cap
        self.ubicacion = ubi
        self.valor = val


    def establecerNombre(self,n):
        self.nombre = n
    def obtenerNombre(self):
        return self.nombre
    def establecerHorario(self, n):
        self.Horario = n
    def obtenerHorario(self):
        return self.Horario
    def establecerCapacidad(self,n):
        self.capacidad = n
    def obtenerCapacidad(self):
        return self.capacidad
    def establecerUbicaion(self,n):
        self.ubicacion = n
    def obtenerUbicacion(self):
        return self.ubicacion
    def establecerValor(self,n):
        self.valor= n
    def obtenerValor(self):
        return self.valor


cancha = CanchaSintetica("Balon de Fuego","8am-12pm",300,"Punzara Chico",20)

nombre = cancha.obtenerNombre()
Horario = cancha.obtenerHorario()
capacidad  = cancha.obtenerCapacidad()
ubicacion = cancha.obtenerUbicacion()
valor = cancha.obtenerValor()
print("Cancha Sintetica: "+nombre+" \nHora de Atencion: "+Horario+" \nCapacidad: "+str(capacidad)+" \nUbicacion: "+ubicacion+"\nValor: "+str(valor)+"$")