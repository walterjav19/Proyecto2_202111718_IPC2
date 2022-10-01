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
                empresa.iniciar_escritorios()        
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
            
            emp=lista_empresas.recorrer_id_empresa(id_empresa)
            escritorios_desactivados=emp.lista_escritorios
            pts_atencion=emp.puntos_atencion
            for pt_atencion in pts_atencion:
                if pt_atencion.attrib['id']==id_punto:
                    for escritorio_activo in escritorios_activos:
                        a=escritorio_activo.attrib['idEscritorio']
                        b=escritorios_desactivados.recorrer_id_escritorio(a)
                        if b is not None:
                            b.set_activo()
                            
                    



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