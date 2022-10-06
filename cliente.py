#varias cosas
class Cliente:
    tiempo_espera=0
    def __init__(self,dpi,nombre,listado_transacciones,tiempo_atencion):
        self.dpi=dpi
        self.nombre=nombre
        self.listado_transacciones=listado_transacciones
        self.tiempo_atencion=tiempo_atencion

    def set_tiempo_espera(self,tiempo_espera):
        self.tiempo_espera=tiempo_espera


    def toString(self):
        return f"\n======Cliente======\nDPI: {self.dpi}\nNombre: {self.nombre}\nTiempo Atencion: {self.tiempo_atencion}\nTiempo Espera: {self.tiempo_espera}"    