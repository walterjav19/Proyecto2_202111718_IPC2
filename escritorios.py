#varias cosas
class Escritorio:
    activo=False
    def __init__(self,id,identificacion,encargado):
        self.id=id
        self.identificacion=identificacion
        self.encargado=encargado
    
    def get_activo(self):
        return self.activo

    def set_activo(self):
        self.activo=True
     
    def set_desactivar(self):
        self.activo=False 

    def escritorios_to_String(self):
        a=""
        if self.activo==True:
            a="SI"
        else:
            a="NO"    
        return f"\n======Escritorio======\nId: {self.id}\nIdentificacion: {self.identificacion}\nEncargado: {self.encargado}\nActivo: {a}"    

