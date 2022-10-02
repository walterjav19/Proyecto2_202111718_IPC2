import xml.etree.ElementTree as ET
from cliente import Cliente
#varias cosas
from empresa import Empresa
from lista_doble import doubleList
lista_empresas=doubleList()
lista_clientes=doubleList()
class leer:
    def leer_xml_empresas(path):
        try:   
            tree=ET.parse(path)
            root=tree.getroot()
            for elem in root:
                id=elem.attrib['id']
                for subelem in elem:
                    if subelem.tag=="nombre":
                        nombre=subelem.text
                    elif subelem.tag=="abreviatura":
                        abreviatura=subelem.text
                    elif subelem.tag=="listaPuntosAtencion":
                        atencion=subelem
                    elif subelem.tag=="listaTransacciones":
                        transac=subelem                                                      
                empresa=Empresa(id,nombre,abreviatura,atencion,transac)
                empresa.iniciar_puntos_atencion()
                empresa.iniciar_transacciones()        
                lista_empresas.append(empresa)


        except FileNotFoundError:
            print("")
            print("!!!!!Archivo inexistente!!!!")
            print("")


    def leer_xml_config(path):
        try:
            tree=ET.parse(path)
            root=tree.getroot()
            for elem in root:
                id_config=elem.attrib['id']
                id_empresa=elem.attrib['idEmpresa']
                id_punto=elem.attrib['idPunto']
                for subelem in elem:
                    if subelem.tag=="escritoriosActivos":
                        escritorios_activos=subelem
                    elif subelem.tag=="listadoClientes":
                        clientes=subelem
            if lista_empresas.obtener_empresa(id_empresa)!=None: 
                emp=lista_empresas.obtener_empresa(id_empresa)
                puntos=emp.lista_atencion
                if puntos.obtener_punto(id_punto)!=None:
                    pto_atencion=puntos.obtener_punto(id_punto)
                    lista_escri=pto_atencion.lista_objetos_escritorios
                    for esc in escritorios_activos:
                        codes=esc.attrib['idEscritorio']
                        if lista_escri.obtener_escritorio(codes)!=None:
                            escritorito=lista_escri.obtener_escritorio(codes)
                            escritorito.set_activo()
    
                        else:
                            print("Escitorio no existe")     
                else:
                    print("Id de Punto de atencion no existe")                 
            else:
                print("Id de Empresa no existe")     
   
            

            #iniciamos clientes
            for cliente in clientes:
                cui=cliente.attrib['dpi']
                for subelem in cliente:
                    if subelem.tag=="nombre":
                        nom=subelem.text
                    elif subelem.tag=="listadoTransacciones":
                        trans=subelem
                cli=Cliente(cui,nom,trans)
                lista_clientes.append(cli)

        except FileNotFoundError:
            print("")
            print("!!!!!Archivo inexistente!!!!")
            print("")
            
leer.leer_xml_empresas("sistema.xml")
leer.leer_xml_config("configsistema.xml")