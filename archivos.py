import os #libreria que permite la manipulacion de archivos mediante Sistema Operativo
import chardet #libreria que permite obetenr la codificacion de archivos
from documento import Documento as doc#Importamos la clase Documento ubicada en el directorio actual
arregloDocumentos = []
salirPrograma = False

while salirPrograma == False:
    print(">>Bienvenido estos archivos existen en el directorio")
    #se llen los archivos existentes el directorio indicado
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
    #Se obtiene el tamano del archivo en bytes
    tamano = os.path.getsize(rutaArchivo);
    #Se obtiene la codificacion de archivo con apoyo de la libreria chardet
    rawdata = open(rutaArchivo, "rb").read()
    result = chardet.detect(rawdata)
    codificacionArchivo = result['encoding']
    #Se crea objeto con las propiedades definidas en la clase documento
    objetoDocumento = doc(nombreArchivo,tamano,codificacionArchivo)
    #Se agrega objeto a arreglo
    arregloDocumentos.append(objetoDocumento)
    print(">>Documentos Sin Ordenar ")
    for i in arregloDocumentos:
        print (">> Nombre: ",i.nombre," Tamaño: ",i.tamano,"Bytes ","Codificacón: "+i.codificacion);
    print(">>Documentos Ordenados en base a su Tamaño")
    #Se ordena areglo de documento en base a la propiedad tamano
    arregloDocumentosOrdenado = sorted(arregloDocumentos, key=lambda objeto: objeto.tamano)
    for i in arregloDocumentosOrdenado:
        print (">> Nombre: ",i.nombre," Tamaño: ",i.tamano,"Bytes ","Codificacón: "+i.codificacion)
    salirProgramaTxt = input("Salir del programa (teclea si o no): ")
    if salirProgramaTxt == "si":
        salirPrograma = True
    else:
        salirPrograma = False