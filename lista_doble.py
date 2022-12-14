class Nodo:
    def __init__(self, elemento):
        self.elemento = elemento
        self.siguiente = None
        self.anterior = None

class doubleList:
    def __init__(self):
        self.root = None
        
    def append(self, dato):

        if self.root is None:
            nuevoNodo = Nodo(dato)
            self.root = nuevoNodo
            return
        
        apuntador = self.root

        while apuntador.siguiente is not None:
            apuntador = apuntador.siguiente

        nuevoNodo = Nodo(dato)
        apuntador.siguiente = nuevoNodo
        nuevoNodo.anterior = apuntador


    def recorrer_id_escritorio(self, iden):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                if apuntador.elemento.id==iden:
                    return apuntador.elemento   
                apuntador = apuntador.siguiente


    def contar_escritorios_activos(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            i=0
            apuntador = self.root
            while apuntador is not None:
                if apuntador.elemento.activo==True:
                    i+=1
                    return i   
                apuntador = apuntador.siguiente



    def contar_escritorios_inactivos(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            i=0
            apuntador = self.root
            while apuntador is not None:
                if apuntador.elemento.activo==False:
                    i+=1
                    return i   
                apuntador = apuntador.siguiente

    def obtener_empresa(self, iden):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                if apuntador.elemento.id==iden:
                    return apuntador.elemento
                apuntador = apuntador.siguiente

    def obtener_transaccion(self, iden):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                if apuntador.elemento.id==iden:
                    return apuntador.elemento
                apuntador = apuntador.siguiente



    def obtener_punto(self, iden):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                if apuntador.elemento.id_punto==iden:
                    return apuntador.elemento
                apuntador = apuntador.siguiente


    def obtener_escritorio(self, iden):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                if apuntador.elemento.id==iden:
                    return apuntador.elemento
                apuntador = apuntador.siguiente

    def imprimir_lista(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                print(apuntador.elemento, "???")
                apuntador = apuntador.siguiente

    def sumar_tiempos_atencion(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            i=0
            apuntador = self.root
            while apuntador is not None:
                i+=apuntador.elemento.tiempo_atencion
                apuntador = apuntador.siguiente
            return i
#tiempos de espera
    def tiempo_medio_espera(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            i=0
            apuntador = self.root
            while apuntador is not None:
                i+=apuntador.elemento.tiempo_espera
                apuntador = apuntador.siguiente
            return i/self.contar_elementos()        

    def tiempo_minimo_espera(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            minimo=apuntador.elemento.tiempo_espera
            while apuntador is not None:
                if apuntador.elemento.tiempo_espera<minimo:
                    minimo=apuntador.elemento.tiempo_espera
                apuntador = apuntador.siguiente
            return minimo    



    def tiempo_maximo_espera(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            maximo=apuntador.elemento.tiempo_espera
            while apuntador is not None:
                if apuntador.elemento.tiempo_espera>maximo:
                    maximo=apuntador.elemento.tiempo_espera
                apuntador = apuntador.siguiente
            return maximo    
#fin tiempos de espera

    def tiempo_medio_atencion(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            i=0
            apuntador = self.root
            while apuntador is not None:
                i+=apuntador.elemento.tiempo_atencion
                apuntador = apuntador.siguiente
            return i/self.contar_elementos()        

    def tiempo_minimo_atencion(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            minimo=apuntador.elemento.tiempo_atencion
            while apuntador is not None:
                if apuntador.elemento.tiempo_atencion<minimo:
                    minimo=apuntador.elemento.tiempo_atencion
                apuntador = apuntador.siguiente
            return minimo    



    def tiempo_maximo_atencion(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            maximo=apuntador.elemento.tiempo_atencion
            while apuntador is not None:
                if apuntador.elemento.tiempo_atencion>maximo:
                    maximo=apuntador.elemento.tiempo_atencion
                apuntador = apuntador.siguiente
            return maximo    






    def imprimir_lista_empresas(self):
        if self.root is None:
            print("No hay empresas cargadas")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                print(apuntador.elemento.empresa_toString())
                apuntador = apuntador.siguiente


    def imprimir_lista_clientes(self):
        if self.root is None:
            print("No hay clientes cargados")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                print(apuntador.elemento.toString())
                apuntador = apuntador.siguiente            

    def imprimir_lista_puntos(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                print(apuntador.elemento.toString())
                apuntador = apuntador.siguiente

    def imprimir_lista_transacciones(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                print(apuntador.elemento.to_String())
                apuntador = apuntador.siguiente

    def imprimir_lista_escritorios(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                print(apuntador.elemento.escritorios_to_String())
                apuntador = apuntador.siguiente





    def eliminar_inicio(self):
        if self.root is None:
            print("La lista no contiene Nodos para eliminar")
            return
        
        if self.root.siguiente is None:
            self.root = None
        else:
            self.root = self.root.siguiente
            self.root.anterior = None


    def eliminar_final(self):
        if self.root is None:
            print("La lista no contiene Nodos para eliminar")
            return
        
        if self.root.siguiente is None:
            self.root = None
            return

        apuntador = self.root
        while apuntador.siguiente is not None:
            apuntador = apuntador.siguiente
        apuntador.anterior.siguiente = None

    def lista_vacia(self):
        if self.root is None:
            return True
        else:
            return False
    
    def contar_elementos(self):
        apuntador = self.root
        cuenta = 0

        while apuntador is not None:
            cuenta = cuenta + 1
            apuntador = apuntador.siguiente
        return cuenta


    def contar_escritorios_activos(self):
        apuntador = self.root
        cuenta = 0

        while apuntador is not None:
            if apuntador.elemento.activo==True:
                cuenta = cuenta + 1
            apuntador = apuntador.siguiente
        return cuenta

    def contar_escritorios_desactivados(self):
        apuntador = self.root
        cuenta = 0

        while apuntador is not None:
            if apuntador.elemento.activo==False:
                cuenta = cuenta + 1
            apuntador = apuntador.siguiente
        return cuenta

    def obtener_nodo(self,id):
        i=0
        apunt=self.root
        while apunt is not None:
            i+=1
            if i==id:
                return apunt.elemento
            apunt=apunt.siguiente    
            #varias cosas