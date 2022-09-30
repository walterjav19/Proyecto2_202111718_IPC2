class Escritorio:
    activo=False
    def __init__(self,id,identificacion,encargado):
        self.id=id
        self.identificacion=identificacion
        self.encargado=encargado
    
    def get_activo(self):
        return self.activo

    def set_activo(self,activo):
        self.activo=activo 

