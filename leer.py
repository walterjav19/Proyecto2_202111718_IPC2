import xml.etree.ElementTree as ET

from empresa import Empresa
from lista_doble import doubleList
lista_empresas=doubleList()
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
                lista_empresas.append(empresa)
            lista_empresas.imprimir_lista()

        except FileNotFoundError:
            print("")
            print("!!!!!Archivo inexistente!!!!")
            print("")

            
leer.leer_xml_empresas("sistema.xml")