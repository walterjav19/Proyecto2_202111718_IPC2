from empresa import Empresa
from escritorios import Escritorio
from leer import leer, lista_empresas,lista_clientes
from lista_doble import doubleList
from punto_atencion import Punto_Atencion
from transaccion import Transaccion
opcion=0
lista_doble_escritorios=doubleList()
pto_obj=None
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
    global pto_obj
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



def manejo_puntos_atencion():
    print("")
    print("===MENU DE PUNTOS DE ATENCION===")
    print("1. Ver Estado del punto")
    print("2. Activar Escritorio")
    print("3. Desactivar escritorio")
    print("4. Atender Cliente")
    print("5. Solicitud de Atencion")
    print("")

while int(opcion) !=4 :
    menu()