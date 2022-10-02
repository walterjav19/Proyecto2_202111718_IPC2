from lista_doble import doubleList
from punto_atencion import Punto_Atencion
from transaccion import Transaccion
#varias cosas

class Empresa:
    lista_atencion=None
    lista_transacciones=None
    def __init__(self,id,nombre,abreviatura,puntos_atencion,transacciones):
        self.id=id
        self.nombre=nombre
        self.abreviatura=abreviatura
        self.puntos_atencion=puntos_atencion
        self.transacciones=transacciones


    def set_lista_atencion(self,lista):
        self.lista_atencion=lista

    def set_lista_transacciones(self,lista):
        self.lista_transacciones=lista


    def empresa_toString(self):
        return f"\n==========Empresa==========\nid: {self.id}\nNombre: {self.nombre}\nAbreviatura: {self.abreviatura}"

    def iniciar_puntos_atencion(self):
        list_Atencion=doubleList()
        for punto in self.puntos_atencion:
            id_punto=punto.attrib['id']
            for subelem in punto:
                if subelem.tag=="nombre":
                    nombre_punto=subelem.text
                elif subelem.tag=="direccion":
                    direccion=subelem.text
                elif subelem.tag=="listaEscritorios":
                    lista_escritorios=subelem         
            pto_aten=Punto_Atencion(id_punto,nombre_punto,direccion,lista_escritorios)
            pto_aten.iniciar_escritorios()
            list_Atencion.append(pto_aten)
            self.lista_atencion=list_Atencion
                    
        self.lista_atencion=list_Atencion

    def iniciar_transacciones(self):
        list_transa=doubleList()
        for transaccion in self.transacciones:
            id_tran=transaccion.attrib['id']
            for subelem in transaccion:
                if subelem.tag=="nombre":
                    nom=subelem.text
                elif subelem.tag=="tiempoAtencion":
                    t_aten=subelem.text
            obj_transaccion=Transaccion(id_tran,nom,t_aten)            
            list_transa.append(obj_transaccion)
        self.lista_transacciones=list_transa    





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