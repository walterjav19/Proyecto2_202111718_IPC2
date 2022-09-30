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


    
    def recorrer_id_empresa(self, iden):
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
                print(apuntador.elemento, "→")
                apuntador = apuntador.siguiente

    def imprimir_lista_empresas(self):
        if self.root is None:
            print("La lista esta vacia")
            return
        else:
            apuntador = self.root
            while apuntador is not None:
                apuntador.elemento.empresa_toString()
                apuntador = apuntador.siguiente

    def eliminar_inicio(self):
        if self.root is None:
            print("La lista no contiene Nodos para eliminar")
            return
        
        if self.root.siguiente is None:
            self.root = None

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


    def obtener_nodo(self,id):
        i=0
        apunt=self.root
        while apunt is not None:
            i+=1
            if i==id:
                return apunt.elemento
            apunt=apunt.siguiente    