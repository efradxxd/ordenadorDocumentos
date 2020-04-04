import os #libreria que permite la manipulacion de archivos mediante Sistema Operativo
import chardet #libreria que permite obetenr la codificacion de archivos
from documento import Documento as doc#Importamos la clase Documento ubicada en el directorio actual
arregloDocumentos = []
salirPrograma = False

while salirPrograma == False:
    print(">>Bienvenido estos archivos existen en el directorio")
    for dirpath, dirnames, filenames in os.walk("./archivos"):
        print("Ruta actual:", dirpath)
        print("Carpetas:", ", ".join(dirnames))
        print("Archivos:", ", ".join(filenames))
    print(">>Teclea el nombre del archivo que deseas seleccionar")
    nombreArchivo = input()
    rutaArchivo = "./archivos/" + nombreArchivo
    while os.path.isfile(rutaArchivo) == False:
        print(">>La ruta que selecionaste no existe, Teclea una ruta valida")
        nombreArchivo = input()
        rutaArchivo = "./archivos/" + nombreArchivo
    # print(">>Nombre Archivo: ",nombreArchivo)
    # print(">>Tamaño Archivo: ", os.path.getsize(nombreArchivo)," Bytes")
    tamano = os.path.getsize(rutaArchivo);
    rawdata = open(rutaArchivo, "rb").read()
    result = chardet.detect(rawdata)
    codificacionArchivo = result['encoding']
    # print(">>Codificación Archivo:")
    # print(codificacionArchivo)
    objetoDocumento = doc(nombreArchivo,tamano,codificacionArchivo)
    arregloDocumentos.append(objetoDocumento)
    print(">>Documentos Sin Ordenar ")
    for i in arregloDocumentos:
        print (">> Nombre: ",i.nombre," Tamaño: ",i.tamano,"Bytes ","Codificacón: "+i.codificacion);
    print(">>Documentos Ordenados en base a su Tamaño")
    arregloDocumentosOrdenado = sorted(arregloDocumentos, key=lambda objeto: objeto.tamano)
    for i in arregloDocumentosOrdenado:
        print (">> Nombre: ",i.nombre," Tamaño: ",i.tamano,"Bytes ","Codificacón: "+i.codificacion)
    salirProgramaTxt = input("Salir del programa (teclea si o no): ")
    if salirProgramaTxt == "si":
        salirPrograma = True
    else:
        salirPrograma = False