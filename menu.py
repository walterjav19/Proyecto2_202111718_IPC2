from cliente import Cliente
from empresa import Empresa
from escritorios import Escritorio
from leer import leer, lista_empresas,lista_clientes
from lista_doble import doubleList
from punto_atencion import Punto_Atencion
from transaccion import Transaccion
opcion=0
lista_doble_escritorios=doubleList()
pto_obj=None
emp=None
def menu():
    global opcion
    print("===MENU DE INICIO===")
    print("1. Configuracion de empresas")
    print("2. Seleccion de empresas y puntos de atencion")
    print("3. Manejo de Puntos de atencion")
    print("4. Salir")
    opcion=input("")
    if int(opcion)==1:
        menu_empresa()
    elif int(opcion)==2:
        opcion_2()
    elif int(opcion)==3:
        manejo_puntos_atencion()
    elif int(opcion)==4:
        print("SALIENDO!!")               
    else:
        print("Por favor elija una opcion entre 1-4")      

def menu_empresa():
    print("")
    print("===MENU DE EMPRESA===")
    print("1. Limpiar Sistema")
    print("2. Cargar Archivo de configuracion del sistema")
    print("3. Crear Nueva empresa")
    print("4. Cargar archivo de configuracion de la prueba")
    print("")
    op=int(input("Elija Opcion: "))

    if op==1:
        for i in range(lista_empresas.contar_elementos()):
            lista_empresas.eliminar_final()
        for i in range(lista_clientes.contar_elementos()):
            lista_clientes.eliminar_final()    
        print("Estructuras limpias correctamente")
        print("")
    elif op==2:
        path=input("Coloque la Ruta del XML: ")
        leer.leer_xml_empresas(path)
    elif op==3:
        crear_empresa()
    elif op==4:
        path=input("Cargue la ruta del XML: ")
        leer.leer_xml_config(path)
    else:
        print("Ingrese un numero entre [1-4]")    

def crear_empresa():
    lista_objetos_puntos=doubleList()
    lista_objetos_transaccion=doubleList()
    id=input("Ingrese el Id de la Empresa: ")
    nom=input("Ingrese el Nombre de la Empresa: ")
    ab=input("Ingrese Abreviatura de la empresa: ")
    nueva_empresa=Empresa(id,nom,ab,None,None)
    num_p=int(input("Cuantos Puntos de atencion Necesita: "))

    for i in range(num_p):
        print("")
        lista_objetos_escritorios=doubleList()
        id_punto=input("Ingrese el Id del Punto: ")
        nombre_punto=input("Ingrese el Nombre del Punto: ")
        direccion_punto=input("Ingrese la Direccion del Punto: ")
        nuevo_punto=Punto_Atencion(id_punto,nombre_punto,direccion_punto,None)
        lista_objetos_puntos.append(nuevo_punto)
        num_e=int(input("Cuantos escritorios de atencion Necesita: "))
        print("")
        for j in range(num_e):
            id_escri=input("Ingrese el Id del Escritorio: ")
            identi_escri=input("Ingrese la Identificacion del Escritorio: ")
            encar=input("Ingrese el encargado del Escritorio: ")
            escritorio_nuevo=Escritorio(id_escri,identi_escri,encar)
            lista_objetos_escritorios.append(escritorio_nuevo)
            nuevo_punto.set_lista_objetos_escritorios(lista_objetos_escritorios)
            print("")
    nueva_empresa.set_lista_atencion(lista_objetos_puntos)

    num_t=int(input("Cuantas Transacciones Necesita: "))
    for k in range(num_t):
        id_transac=input("Ingrese el Id de la transaccion: ")
        nombre_tran=input("Ingrese el Nombre de la transaccion: ")
        tiempo=input("Ingrese el tiempo de atencion de la transaccion: ")
        nueva_transa=Transaccion(id_transac,nombre_tran,tiempo)
        lista_objetos_transaccion.append(nueva_transa)
    nueva_empresa.set_lista_transacciones(lista_objetos_transaccion)    
    lista_empresas.append(nueva_empresa)
    print("\n*********Atencion*********\nEmpresa Creada Correctamente\n")



def opcion_2():
    global pto_obj,emp
    if lista_empresas.lista_vacia()==True:
        print("no hay empresas en el sistema aun")
    else:    
        lista_empresas.imprimir_lista_empresas()
        print("")
        empresa=int(input("Elegir empresa: "))
        emp=lista_empresas.obtener_nodo(empresa)
        emp.lista_atencion.imprimir_lista_puntos()
        list_puntos=emp.lista_atencion
        pto=int(input("Elegir Punto: "))
        pto_obj=list_puntos.obtener_nodo(pto)
        print("\nPunto a estudiar elegido correctamente\n")



def manejo_puntos_atencion():
    global pto_obj
    n=0
    while n !=7:
        print("")
        print("===MENU DE PUNTOS DE ATENCION===")
        print("1. Ver Estado del punto")
        print("2. Activar Escritorio")
        print("3. Desactivar escritorio")
        print("4. Atender Cliente")
        print("5. Solicitud de Atencion")
        print("6. Simular actividad del punto de atención")
        print("7. Regresar Menu principal")
        print("")
        n=int(input("Ingrese la opcion: "))
        if n==1:
            if pto_obj!=None:
                lista_escri=pto_obj.lista_objetos_escritorios
                print("\n======Estado del punto de Atencion======")
                print("Escritorios Activos: "+str(lista_escri.contar_escritorios_activos()))
                print("Escritorios Inactivos: "+str(lista_escri.contar_escritorios_desactivados()))
                if lista_clientes.lista_vacia()==True:
                    print("\nNo hay clientes en espera")
                else:    
                    print("Clientes en Espera: "+str(lista_clientes.contar_elementos()))
                    print("Tiempo Promedio de Espera: "+str(lista_clientes.tiempo_medio_espera())+" Minutos")
                    print("Tiempo Maximo de Espera: "+str(lista_clientes.tiempo_maximo_espera())+" Minutos")
                    print("Tiempo Minimo de Espera: "+str(lista_clientes.tiempo_minimo_espera())+" Minutos")
                    print("Tiempo Promedio de atencion: "+str(lista_clientes.tiempo_medio_atencion())+" Minutos")
                    print("Tiempo Maximo de atencion: "+str(lista_clientes.tiempo_maximo_atencion())+" Minutos")
                    print("Tiempo Minimo de atencion: "+str(lista_clientes.tiempo_minimo_atencion())+" Minutos\n")
                #lista_escri.imprimir_lista_escritorios()
            else:
                print("\nAun no se ha elegido un punto de atencion")    
        elif n==2:
            if pto_obj!=None:
                lista_escri=pto_obj.lista_objetos_escritorios
                lista_escri.imprimir_lista_escritorios()
                acti=int(input("\nCual escritorio quiere activar: "))
                nodo=lista_escri.obtener_nodo(acti)
                nodo.set_activo()
                print("\nActivado Correctamente")
            else:
                print("\nAun no se ha elegido un punto de atencion")
        elif n==3:
            if pto_obj !=None:
                lista_escri=pto_obj.lista_objetos_escritorios
                lista_escri.imprimir_lista_escritorios()
                desacti=int(input("\nCual escritorio quiere desactivar: "))   
                nodo=lista_escri.obtener_nodo(desacti)
                nodo.set_desactivar()
                print("\nDesactivado Correctamente")
            else:
                print("\nAun no se ha elegido un punto de atencion")        
        elif n==4:
            print("\nEl primer cliente en la cola fue atendido ")
            lista_clientes.eliminar_inicio()
            #lista_clientes.imprimir_lista_clientes()            
        elif n==5:
            list_tran=emp.lista_transacciones
            t_t=0
            dpi=input("Ingrese el dpi del Cliente: ")
            nombre=input("Ingrese el nombre: ")
            n_tran=int(input("Cuantas Transacciones realizara: "))
            i=0
            while i!=n_tran:
                id_tran=input("Ingrese Id de la operacion: ")
                if list_tran.obtener_transaccion(id_tran)!=None:
                    objeto_t=list_tran.obtener_transaccion(id_tran)
                    t_t+=int(objeto_t.tiempo)
                    i+=1
                    print("\nTransaccion Agregada\n")
                else:
                    print("\nEsta empresa no reconoce el id de esta transaccion\n") 
            nuevo_cliente=Cliente(dpi,nombre,None,t_t)
            nuevo_cliente.set_tiempo_espera(lista_clientes.sumar_tiempos_atencion())  
            lista_clientes.append(nuevo_cliente)
            print("\nTiempo promedio de espera: "+str(lista_clientes.tiempo_medio_espera())+" Minutos\n")
            #lista_clientes.imprimir_lista_clientes()
            
        elif n==6:
            atendidos=0
            for i in range(lista_clientes.contar_elementos()):
                atendidos+=1
                lista_clientes.eliminar_inicio()
            print("\nEl total de clientes atendidos fue :"+str(atendidos))
        elif n==7:
            print("\nRegresando al menu de inicio....\n")
        else:
            print("\nelija opcion entre 1-6")






while int(opcion) !=4 :
    menu()