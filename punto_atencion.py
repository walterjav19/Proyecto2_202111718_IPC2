from escritorios import Escritorio
from lista_doble import doubleList


class Punto_Atencion:
    lista_objetos_escritorios=None
    def __init__(self,id_punto,nombre,direccion,list_escri):
        self.id_punto=id_punto
        self.nombre=nombre
        self.direccion=direccion
        self.list_escri=list_escri

    def set_lista_objetos_escritorios(self,lista):
        self.lista_objetos_escritorios=lista

    def iniciar_escritorios(self):
        lista_doble_escri=doubleList()
        for escritorio in self.list_escri:
            id_escri=escritorio.attrib['id']
            for subelem in escritorio:
                if subelem.tag=="identificacion":
                    iden=subelem.text
                elif subelem.tag=="encargado":
                    enc=subelem.text
            obj_escri=Escritorio(id_escri,iden,enc)            
            lista_doble_escri.append(obj_escri)
        self.lista_objetos_escritorios=lista_doble_escri

    def toString(self):
        return f"\n=====Punto de Atencion=====\nid: {self.id_punto}\nNombre: {self.nombre}\nDireccion: {self.direccion}\n"