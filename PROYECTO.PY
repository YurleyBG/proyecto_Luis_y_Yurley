import json
def abrirArchivo():
    datos=[]
    with open("info.json", encoding="utf-8") as openfile:
        datos=json.load(openfile)
    return datos

def guardarArchivo(midato):
    with open("info.json", "w") as file:
        json.dump(midato,file)

def menu():
    print("")
    print(":::::::::BIENBENIDO A NUESTRA PLATAFORMA::::::::\n"
          "1 MODULO DE COORDINACION ACADEMICA\n"
          "2 MODULO DE TRAINER\n"
          "3 MODULO DE REPORTE\n"
          "4 SALIR")
    
def menucoordinador():
    print("::::::::::MENU::::::::::\n"
          "1 listar estudiantes\n"
          "2 asignar notas\n"
          "3 crear rutas academicas con los modulos\n"
          "4 asignar rutas de entrenamiento a los traniers\n"
          "5 modulo de matriculas\n"
          "6 consultar campers con riesgo alto\n"
          "7 volver al menu principal")

def menureportes():
     print("::::::::::MENU::::::::::\n"
           "1 listar campers inscritos\n"
           "2 listar los campers que aprobaron el examen principal\n"
           "3 listar todos los entrenadores\n"
           "4 listar campers de bajo rendimiento\n"
           "5 listar campers y trainers que tienen ruta de entrenamiento\n"
           "6 mostrar cuantos campers perdieron y aprobaron cada uno de los modulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado\n"
           "7 volver al menu principal")
     

miArchivo=[]
miArchivo=abrirArchivo()
menu()
bool=True
while bool==True:
    try:
        opc=int(input("ingrese su opcion por favor: "))
        if opc==1:
            print("MODULO DE COORDINACION ACADEMICA")
            print("")
            menucoordinador()
            ver=True
            while ver==True:
                try:
                    opc=int(input("ingrese su opcion por favor: "))
                    if opc==1:
                        for i in range(len(miArchivo[0]["grupos"])):
                            print("--------")
                            print(miArchivo[0]["grupos"][i]["nombres"])
                            cont=0
                        gru=input("que grupo quieres listar\n")
                        for i in range(len(miArchivo[0]["grupos"])):
                            if miArchivo[0]["grupos"][i]["nombres"]==gru:
                                for z in miArchivo[0]["grupos"][i]["grupo"]:
                                    cont+=1
                                    print(" ")
                                    print("==================== CAMPER # ",cont,"==============================")
                                    print("id: ",z["id"])
                                    print("nombre: ", z["nombre"])
                                    print("apellido: ", z["apellido"])
                                    print("edad: ", z["edad"])
                                    print("direccion: ", z["direccion"])
                                    print("acudiente: ", z["acudiente"])
                                    print("telefono: ", z["telefono"])
                                    print("estado: ", z["estado"])
                                    print("riesgo: ", z["riesgo"])
                                    print("=========================================================")
                                    print("")
                    if opc==2:
                        pedir=input("ingresa el id del estudiante al que le quieres asignar notas\n")
                        for i in miArchivo[0]["grupos"]:
                            for z in i["grupo"]:
                                if z["id"]==pedir:
                                    print("ingresa las notas para ",z["nombre"])
                                    nota1=float(input("nota 1: "))
                                    nota2=float(input("nota 2: "))

                except ValueError:
                    print("solo se pueden ingresar numeros")
    except ValueError:
       print("solo se pueden ingresar numeros")

    