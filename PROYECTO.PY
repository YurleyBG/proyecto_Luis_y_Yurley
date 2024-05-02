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
    print("::::::::::MENÚ::::::::::\n"
          "1 listar estudiantes\n"
          "2 ingresar nuevos campers\n"
          "3 asignar notas a los campers que estan en progreso de ingreso y asignación de grupo\n"
          "4 crear rutas academicas con los modulos\n"
          "5 asignar rutas de entrenamiento a los traniers\n"
          "6 modulo de matriculas\n"
          "7 notas de modulos"
          "8 consultar campers con riesgo alto\n"
          "9 actualizar datos de campers\n"
          "10volver al menu principal\n"
          ":::::::::::::::::::::::::\n")


def menutrainer():
    print("::::::::::::::MENÚ:::::::::::::\n"
          "1 mostrar horarios y ruta de los trainers\n"
          "2 volver al menu principal")


def menureportes():
     print("::::::::::MENÚ::::::::::\n"
           "1 listar campers inscritos\n"
           "2 listar los campers que aprobaron el examen principal\n"
           "3 listar todos los entrenadores\n"
           "4 listar campers de bajo rendimiento\n"
           "5 listar campers y trainers que tienen ruta de entrenamiento\n"
           "6 mostrar cuantos campers perdieron y aprobaron cada uno de los modulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado\n"
           "7 volver al menu principal")
def menumodulo():
     print("==========MENÚ DE MODULOS============\n"
            "1 fundamentos de programacion\n"
            "2 programacion web\n"
            "3 programacion formal\n"
            "4 bases de datos\n"
            "5 backend\n")
     

miArchivo=[]
miArchivo=abrirArchivo()
menu()
bool=True
while bool==True:
    try:
        opc=int(input("ingrese su opcion por favor: "))
        if opc==1:
            print("")
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
                        print("")
                        print(":::::::::AÑADIR NUEVO CAMPER:::::::::")
                        id=input("ingrese la id que quiere ing: ")
                        nombre=input("ingrese el nombre: ")
                        apellido=input("ingrese el apellido: ")
                        edad=input("ingrese la edad: ")
                        direccion=input("ingrese la direccion: ")
                        acudiente=input("ingrese el nombre del acudiente:  ")
                        celular=int(input("ingrese el numero:  "))
                        fijo=int(input("ingrese numero fijo:  "))
                    
                        miArchivo[0]["ingreso"].append({"id":id,"nombre":nombre,"apellido":apellido,"edad":edad, "direccion":direccion, "acudiente":acudiente, "telefono": {"celular":celular, "fijo":fijo},"estado":"progreso de ingreso", "riesgo":""})
                        print("se ha creado con exito!!")
                        guardarArchivo(miArchivo)
                        menucoordinador()
                    

                    if opc==3:
                        miArchivo=abrirArchivo()
                        print("estos son los estudiantes que estan en estado de ingreso")
                        for i in miArchivo[0]["ingreso"]:
                            if i["estado"]=="progreso de ingreso":
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
                                archivo=i
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
                                        print("estos son los grupos que estan disponibles")
                                        for i in range(len(miArchivo[0]["grupos"])):
                                            if len(miArchivo[0]["grupos"][i]["grupo"])<33:
                                                print("--------")
                                                print(miArchivo[0]["grupos"][i]["nombres"])
                                        pregunta2=input("a que grupo deseas agregarlo")
                                        for i in miArchivo[0]["grupos"]:
                                            if pregunta2==i["nombres"]:
                                                i["grupo"].append(archivo)
                                                
                                        print("se han aplicado los cambios")
                        for i in range(len(miArchivo[0]["ingreso"])-1,-1,-1):
                            if miArchivo[0]["ingreso"][i]["estado"]=="aprobado":
                                miArchivo[0]["ingreso"].pop(i)
                        guardarArchivo(miArchivo)
                        menucoordinador()
                    if opc==4:
                        miArchivo=abrirArchivo()
                        print("")

                        print(":::::::::: CREAR RUTAS ACADEMICAS CON LOS MODULOS ::::::::::::::")
                        nuevo=input("ingresa el nombre de la nueva ruta\n")
                        nuevonombre=input("ingresa el nombre del nuevo grupo\n")
                        miArchivo[0]["grupos"].append({"ruta":nuevo, "nombres":nuevonombre, "grupo":[]})
                        guardarArchivo(miArchivo)
                        menucoordinador()
                        
                    if opc==7:
                        miArchivo=abrirArchivo()
                        print(":::::::notas de modulos:::::::")
                        nomru=input("a que ruta de entrenamiento le asignaras las notas:  ")
                        for i in miArchivo[0]["grupos"]:
                            if i["ruta"]==nomru:
                                print("grupo: ", i["nombres"])
                                for a in i["grupo"]:
                                    print("id:  ", a["id"])
                                    print("nombre:  ", a["nombre"])
                                    print("apellido:  ", a["apellido"])
                        pregun=input("ingresa el id del camper al que le quieres asignar notas:  ")
                        for i in miArchivo[0]["grupos"]:
                            for z in i["grupo"]:
                                if z["id"]==pregun:
                                    nota1=float(input("ingresa la nota de la prueba teorica\n"))
                        menucoordinador()

                    if opc==8:
                        print("") 
                        print("::::::::::::::CAMPERS CON RIESGO ALTO:::::::::::::::") 
                        print("")
                        print("::::::Estos campers recibiran un llamado de atencion:::::::::")
                        for i in miArchivo[0]["grupos"]:
                            for b in i["grupo"]:
                        
                                if b["riesgo"]=="alto":
                                    print(" ")
                                    print("==================================================")
                                    print("id: ",b["id"])
                                    print("nombre: ", b["nombre"])
                                    print("apellido: ", b["apellido"])
                                    print("riesgo: ", b["riesgo"])
                                    print("===================================================")
                                    print("")
                        menucoordinador()
                    
                    if opc==10:
                        ver=False
                        menu()
                except ValueError:
                    print("INGRESA UNA OPCIÓN VALIDA")
        elif opc==3:
            print("MODULO DE REPORTES")
            print("")
            menureportes()
            mjb=True
            while mjb==True:
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
                    if opc==2:
                        print("")    
                        print("=========CAMPERS QUE APROBARON EL EXAMEN PRINCIPAL =============")   
                        for i in miArchivo[0]["grupos"]:
                            for d in i["grupo"]:
                                if d["estado"]=="aprobado":
                                    print("=========================================================")
                                    print("id:  ",d["id"])
                                    print("nombre:  ",d["nombre"])
                                    print("apellido:  ",d["apellido"])
                                    print("estado:  ",d["estado"])
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
                    if opc==5:
                        print(":::::::: CAMPERS Y TRAINERS CON RUTA DE ENTRENAMIENTO:::::::")
                        print("")
                        print(":::::::TRAINERS:::::::::::")
                        for i in  miArchivo[0]["trainers"]:
                            if i["ruta"]=="NetCore" or i["ruta"]=="java" or i["ruta"]=="nodeJS":
                                print(" ")
                                print("==================================================")
                                print("id: ",i["id"])
                                print("nombre: ", i["nombre"])
                                print("apellido: ", i["apellido"])
                                print("ruta: ", i["ruta"])
                                print("===================================================")
                                print("")
                        for i in  miArchivo[0]["grupos"]:
                                
                            if i["ruta"]=="NetCore" or i["ruta"]=="java" or i["ruta"]=="nodeJS":
                                print(" ")
                                print(":::::CAMPERS CON RUTA:::::::")
                                for a in i["grupo"]:
                                    print(" ")
                                    print("ruta: ", i["ruta"])
                                    print("nombre:  ", i["nombres"])
                                    print("==================================================")
                                    print("id: ",a["id"])
                                    print("nombre: ", a["nombre"])
                                    print("apellido: ", a["apellido"])
                                    print("===================================================")
                                    print("")
                        menureportes()

                    if opc==7:
                        mjb=False
                        menu()

                except ValueError:
                    print("INGRESA UNA OPCIÓN VALIDA")
        if opc==4:
            print("HASTA LA PROXIMA\nPROGRAMA FINALIZADO :)")
            bool=False
    except ValueError:
       print("INGRESA UNA OPCIÓN VALIDA")