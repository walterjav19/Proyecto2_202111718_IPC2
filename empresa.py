from escritorios import Escritorio
from lista_doble import doubleList


class Empresa:
    lista_escritorios=None
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

    def iniciar_escritorios(self):
        list_escritorio=doubleList()
        for punto in self.puntos_atencion:
            for subelem in punto:
                if subelem.tag=="listaEscritorios":
                    escritorios=subelem

            for escritorio in escritorios:
                id_escri=escritorio.attrib['id']
                for subelem in escritorio:
                    if subelem.tag=="identificacion":
                        iden=subelem.text
                    elif subelem.tag=="encargado":
                        encar=subelem.text
                obj_esc=Escritorio(id_escri,iden,encar)
                list_escritorio.append(obj_esc)  

        self.lista_escritorios=list_escritorio

    def get_id(self):
        return self.id  

    def limpiar_lista_escritorio(self):
        self.lista_escritorios=None
  
        
    def get_puntos_atencion(self):
        return self.puntos_atencion   

    def get_escritorios(self):
        return self.escritorios
          
    def get_transacciones(self):
        return self.transacciones                 

    def get_lista_escritorio(self):
        return self.lista_escritorios    