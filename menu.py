from leer import leer, lista_empresas
opcion=0
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
        pass
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