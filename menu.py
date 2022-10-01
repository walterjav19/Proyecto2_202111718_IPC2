from escritorios import Escritorio
from leer import leer, lista_empresas
from lista_doble import doubleList
opcion=0
lista_doble_escritorios=doubleList()
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
        print("Estructuras limpias correctamente")
        lista_empresas.imprimir_lista()
    elif op==2:
        path=input("Coloque la Ruta del XML: ")
        leer.leer_xml_empresas(path)
    elif op==3:
        pass


#varias cosas
def opcion_2():
    lista_empresas.imprimir_lista_empresas()
    print("")
    empresa=int(input("Elegir empresa: "))
    puntos_atencion=lista_empresas.obtener_nodo(empresa)
    for elem in puntos_atencion.puntos_atencion:
            id_punto=elem.attrib['id']
            for subelem in elem:
                if subelem.tag=="nombre":
                    nombre_punto=subelem.text
                elif subelem.tag=="direccion":
                    direccion=subelem.text
                elif subelem.tag=="listaEscritorios":
                    lista_escritorios=subelem
            print("==========Puntos de Atencion==========")        
            print("id: "+id_punto)
            print("nombre:"+nombre_punto)
            print("direccion:"+direccion)
            print("")

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