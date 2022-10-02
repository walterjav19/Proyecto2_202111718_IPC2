class Transaccion:
    def __init__(self,id,nombre,tiempo):
        self.id=id
        self.nombre=nombre
        self.tiempo=tiempo
       
    def to_String(self):
        return f"=======Transaccion=======\nId: {self.id}\nNombre: {self.nombre}\nTiempo atencion: {self.tiempo}\n"       