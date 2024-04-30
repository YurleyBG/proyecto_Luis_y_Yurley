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
          "2 asignar notas a los campers que estan en progreso de ingreso\n"
          "3 crear rutas academicas con los modulos\n"
          "4 asignar rutas de entrenamiento a los traniers\n"
          "5 modulo de matriculas\n"
          "6 notas de modulos"
          "7 consultar campers con riesgo alto\n"
          "8 volver al menu principal")

def menutrainer():
    print("::::::::::::::MENU:::::::::::::\n"
          "1 mostrar horarios y ruta de los trainers\n"
          "2 volver al menu principal")


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
                        menucoordinador()

                    if opc==2:
                        miArchivo=abrirArchivo()
                        print("estos son los estudiantes que estan en estado de ingreso")
                        for i in miArchivo[0]["ingreso"]:
                            if i["estado"]=="en progreso de ingreso":
                                print("=========================================================")
                                print("id:  ",i["id"])
                                print("nombre:  ",i["nombre"])
                                print("apellido:  ",i["apellido"])
                                print("estado:  ",i["estado"])
                                print("=========================================================")
                                print("")
                        pedir=input("ingresa el id del estudiante al que le quieres asignar notas\n")
                        for i in miArchivo[0]["ingreso"]:
                            if i["id"]==pedir:
                                print("ingresa las notas")
                                nota1=float(input("nota de la prueba teorica:  "))
                                nota2=float(input("nota de la prueba practica:  "))
                                nota1=nota1*30/90
                                nota2=nota2*60/90
                                resul=nota1+nota2
                                print(resul)
                                if resul>=60:
                                    pregunta1=input("esta persona aprobó quieres cambiar su estado a aprobado (si)(no):  ")
                                    if pregunta1=="si":
                                        i["estado"]="aprobado"
                                        print("estos son los grupos que existen")
                                        for i in range(len(miArchivo[0]["grupos"])):
                                            print("--------")
                                            print(miArchivo[0]["grupos"][i]["nombres"])
                                        pregunta2=input("a que grupo deseas agregarlo")
                                        
                                        print("se han aplicado los cambios")
                                        
                        menucoordinador()

                except ValueError:
                    print("solo se pueden ingresar numeros")
        elif opc==3:
            print("MODULO DE REPORTES")
            print("")
            menureportes()
            bool=True
            while bool==True:
                try:
                    opc=int(input("ingrese su opcion porfavor: "))
                    if opc==1:
                        for i in range(len(miArchivo[0]["grupos"])):
                                    print("--------")
                                    print(miArchivo[0]["grupos"][i]["nombres"])
                                    cont=0
                        grip=input("que grupo quieres listar\n")
                        for i in range(len(miArchivo[0]["grupos"])):
                                    if miArchivo[0]["grupos"][i]["nombres"]==grip:
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
                        menureportes()                    
                    if opc==3:
                        print("") 
                        print("::::::::::::::TRAINERS:::::::::::::::") 
                        for i in miArchivo[0]["trainers"]:
                            print(" ")
                            print("==================================================")
                            print("id: ",i["id"])
                            print("nombre: ", i["nombre"])
                            print("apellido: ", i["apellido"])
                            print("edad: ", i["edad"])
                            print("ruta: ", i["ruta"])
                            print("grupos: ", i["grupos"])
                            print("===================================================")
                        menureportes()  
                    if opc==4:
                        print("") 
                        print("")
                        print("::::::::::::::CAMPERS DE BAJO RENDIMIENTO:::::::::::::::") 
                        print("Todos aquellos campers que cuenta con un riesgo alto equivale a un rendimiento bajo")
                        for i in miArchivo[0]["grupos"]:
                            for a in i["grupo"]:
                        
                                if a["riesgo"]=="alto":
                                    print(" ")
                                    print("==================================================")
                                    print("id: ",a["id"])
                                    print("nombre: ", a["nombre"])
                                    print("apellido: ", a["apellido"])
                                    print("riesgo: ", a["riesgo"])
                                    print("===================================================")
                                    print("")
                        menureportes() 
                    if opc==7:
                        menu()

                except ValueError:
                    print("solo se pueden ingresar numeros")
    except ValueError:
       print("solo se pueden ingresar numeros")

    