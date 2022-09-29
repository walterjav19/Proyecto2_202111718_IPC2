


class Empresa:
    def __init__(self,id,nombre,abreviatura,puntos_atencion,transacciones):
        self.id=id
        self.nombre=nombre
        self.abreviatura=abreviatura
        self.puntos_atencion=puntos_atencion
        self.transacciones=transacciones

    def empresa_toString(self):
        print("")
        print("==========Empresa==========")
        print("id: "+self.id)
        print("Nombre: "+self.nombre)
        print("Abreviatura: "+self.abreviatura)

    def get_id(self):
        return self.id  

    def get_puntos_atencion(self):
        return self.puntos_atencion   

    def get_escritorios(self):
        return self.escritorios
          
    def get_transacciones(self):
        return self.transacciones                 