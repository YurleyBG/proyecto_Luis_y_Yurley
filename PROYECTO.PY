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
          "6 modulo de matriculas\n"
          "4 crear rutas academicas con los modulos\n"
          "5 asignar rutas de entrenamiento a los traniers\n"
          "6 notas de modulos\n"
          "7 consultar campers con riesgo alto\n"
          "8 actualizar datos de campers\n"
          "9 volver al menu principal\n"
          ":::::::::::::::::::::::::\n")


def menutrainer():
    print("::::::::::::::MENÚ:::::::::::::\n"
          "1 mostrar horarios y ruta de los trainers\n"
          "2 ver menu de reportes\n"
          "3 volver al menu principal")


def menureportes():
     print("::::::::::MENÚ::::::::::\n"
           "1 listar campers inscritos\n"
           "2 listar los campers que aprobaron el examen principal\n"
           "3 listar todos los entrenadores\n"
           "4 listar campers de bajo rendimiento\n"
           "5 listar campers y trainers que tienen ruta de entrenamiento\n"
           "6 mostrar cuantos campers perdieron y aprobaron cada uno de los modulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado\n"
           "7 volver al menu principal")

def menumodificaciones():
    print(":::::::::MENÚ MODIFICACIONES:::::::::::\n"
          "1 modificar nombre\n"
          "2 modificar apellido \n"
          "3 modificar edad \n"
          "4 modificar direccion\n"
          "5 modificar acudiente\n"
          "6 modificar numero de celular\n"
          "7 modificar numero fijo\n"
          "8 finalizar\n"
          ":::::::::::::::::::::::::::::::::::::\n")
    
def notasmodulos():
    print("------------MODULOS------------")
    print("1 fundamentos de programacion")
    print("2 programacion web")
    print("3 programacion formal")
    print("4 bases de datos")
    print("5 backend")
    print("6 finalizar")

def modifmatriculas():
    print("-----------DATOS-----------")
    print("1 Fecha de inicio")
    print("2 Fecha de finalizacion")
    print("3 salon de entrenamiento")
    print("4 volver al menu de coordinador")

     

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
                        bucle=True
                        while bucle==True:
                            print("")
                            print(":::::::::AÑADIR NUEVO CAMPER:::::::::")
                            id=input("ingrese la id que quiere ing: ")
                            nombre=input("ingrese el nombre: ")
                            apellido=input("ingrese el apellido: ")
                            edad=input("ingrese la edad: ")
                            direccion=input("ingrese la direccion: ")
                            acudiente=input("ingrese el nombre del acudiente:  ")
                            uno=True
                            while uno==True:
                                try:
                                    celular=int(input("ingrese el numero:  "))
                                    uno=False
                                except ValueError:
                                    print("ingresa un numero valido")
                            uno=True
                            while uno==True:
                                try:
                                    fijo=int(input("ingrese numero fijo:  "))
                                    uno=False
                                except ValueError:
                                    print("ingresa un numero valido")
                        
                            miArchivo[0]["ingreso"].append({"id":id,"nombre":nombre,"apellido":apellido,"edad":edad, "direccion":direccion, "acudiente":acudiente, "telefono": {"celular":celular, "fijo":fijo},"estado":"progreso de ingreso", "riesgo":"", "modulos":{}})
                            print("se ha creado con exito!!")
                            guardarArchivo(miArchivo)
                            print("")
                            si=input("quieres agregar otro camper(si)\n"
                                     "preciona enter para volver al menú\n")
                            if si!="si":
                                bucle=False
                        menucoordinador()
                    

                    if opc==3:
                        miArchivo=abrirArchivo()
                        hola=True
                        while hola==True:
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
                                if pedir==i["id"]:
                                    hola=False
                                else:
                                    print("ingresa un id existente")
                                    print("")
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
                                    pregunta1=input("esta persona aprobó quieres cambiar su estado a cursando (si)(no):  ")
                                    if pregunta1=="si":
                                        i["estado"]="cursando"
                                        print("estas son las rutas que estan disponibles")
                                        for i in miArchivo[0]["grupos"]:
                                            if len(i["grupo"])<33:
                                                print("--------")
                                                print(i["nombres"])
                                                print(i["ruta"])
                                                print(i["modulos"])
                                        pregunta2=input("ingresa el nombre del grupo que tiene la ruta que deseas:\n")
                                        for i in miArchivo[0]["grupos"]:
                                            if pregunta2==i["nombres"]:
                                                i["grupo"].append(archivo)
                                                
                                        print("se han aplicado los cambios")
                        for i in range(len(miArchivo[0]["ingreso"])-1,-1,-1):
                            if miArchivo[0]["ingreso"][i]["estado"]=="cursando":
                                miArchivo[0]["ingreso"].pop(i)
                        guardarArchivo(miArchivo)
                        menucoordinador()
                    if opc==4:
                        miArchivo=abrirArchivo()
                        print("")

                        print(":::::::::: CREAR RUTAS ACADEMICAS CON LOS MODULOS ::::::::::::::")
                        yo=True
                        while yo==True:
                            uno=True
                            ruta=input("ingresa el nombre de la nueva ruta\n")
                            while uno==True:
                                print("escoje una opcion para programacin formal")
                                try:
                                    modulo1=int(input("1.Java  2.JavaScript  3.C#)\n"))
                                    if modulo1==1:
                                        num1="Java"
                                        uno=False
                                    if modulo1==2:
                                        num1="JavaScrip"
                                        uno=False
                                    if modulo1==3:
                                        num1="C#"
                                        uno=False
                                except ValueError:
                                    print("ingrese una opción valida")
                            
                            dos=True
                            while dos==True:
                                print("escoje el modulo principal para bases de datos")
                                try:
                                    modulo21=int(input("1.Mysql  2.MongoDB  3.PostGresql)\n"))
                                    if modulo21==1:
                                        num2="Mysql"
                                        dos=False
                                    if modulo21==2:
                                        num2="MongoDB"
                                        dos=False
                                    if modulo21==3:
                                        num2="PostGresql"
                                        dos=False
                                except ValueError:
                                    print("ingrese una opción valida")

                            tres=True
                            while tres==True:
                                print("escoje el modulo secundario para bases de datos")
                                try:
                                    modulo22=int(input())
                                    if modulo22==1:
                                        num3="Mysql"
                                        tres=False
                                    if modulo22==2:
                                        num3="MongoDB"
                                        tres=False
                                    if modulo22==3:
                                        num3="PostGresql"
                                        tres=False
                                except ValueError:
                                    print("ingrese una opción valida")

                            cuatro=True
                            while cuatro==True:
                                print("escoje el modulo principal para BACKEND")
                                try:
                                    modulo31=int(input("1.NetCore  2.Spring Boot  3.NodeJS  4.Expres)\n"))
                                    if modulo31==1:
                                        num4="NetCore"
                                        cuatro=False
                                    if modulo31==2:
                                        num4="Spring Boot"
                                        cuatro=False
                                    if modulo31==3:
                                        num4="NodeJS"
                                        cuatro=False
                                    if modulo31==4:
                                        num4="Expres"
                                        cuatro=False
                                except ValueError:
                                    print("ingrese una opción valida")
                            
                            cinco=True
                            while cinco==True:
                                print("escoje el modulo secundario para BACKEND")
                                try:
                                    modulo32=int(input())
                                    if modulo32==1:
                                        num5="NetCore"
                                        cinco=False
                                    if modulo32==2:
                                        num5="Spring Boot"
                                        cinco=False
                                    if modulo32==3:
                                        num5="NodeJS"
                                        cinco=False
                                    if modulo32==4:
                                        num5="Expres"
                                        cinco=False
                                except ValueError:
                                    print("ingrese una opción valida")
                            

                            
                            nuevonombre=input("ingresa el nombre del nuevo grupo\n")
                            miArchivo[0]["grupos"].append({"ruta":ruta, "modulos":{"fundamentos de programacion": ["introduccion a la algoritmia", "PSeint", "Python"],
                                                                                    "programacion web": ["HTML", "CSS", "booststrap"],
                                                                                    "programacion formal":num1,
                                                                                    "bases de datos":[num2,num3],
                                                                                    "backend":[num4,num5]}, "nombres":nuevonombre, "grupo":[]})
                            cambio=input("SE HA CREADO LA RUTA CON EXITO\n"
                                            "crear otra ruta: (si)\n"
                                            "volver al menu: (no)\n")
                            if cambio=="no":
                                yo=False
                        guardarArchivo(miArchivo)
                        menucoordinador()

                    if opc==5:
                        miArchivo=abrirArchivo()
                        ole=True
                        while ole==True:
                            for i in miArchivo[0]["trainers"]:
                                if len(i["ruta"])<4:
                                    print("")
                                    print("--------------------------------")
                                    print("id:  ", i["id"])
                                    print("nombre: ", i["nombre"])
                                    print("apellido", i["apellido"])
                                    print("--------------------------------")
                                    print("")
                            miau=True
                            while miau==True:
                                cont=0
                                try:
                                    seleccion=int(input("ingresa el id del trainer al que le quieres asignar una ruta\n"))
                                    for i in miArchivo[0]["trainers"]:
                                        if len(i["ruta"])<4 and seleccion==i["id"]:
                                            cont=1
                                            miau=False
                                    if cont==0:
                                        print("ingresa un id de los que muestran")
                                except ValueError:
                                    print("ingresa un id valido")
                                
                        menucoordinador()
                    
                    if opc==6:
                        miArchivo=abrirArchivo()
                        for z in miArchivo[0]["grupos"]:
                            print("-------------------------------")
                            print("ruta: ", z["ruta"])
                            print("MODULOS")
                            print("fundamentos de programacion: ", z["modulos"]["fundamentos de programacion"])
                            print("programacion web: ", z["modulos"]["programacion web"])
                            print("programacion formal: ", z["modulos"]["programacion formal"])
                            print("bases de datos: ", z["modulos"]["bases de datos"])
                            print("backend: ", z["modulos"]["backend"])
                            print("grupo: ", z["nombres"])
                            print("-------------------------------")
                            print("")

                        opc7=True
                        while opc7==True:
                            contador=0
                            modificar=input("ingresa el nombre del grupo donde vas a asignar notas\n")
                            for i in miArchivo[0]["grupos"]:
                                if i["nombres"]==modificar:
                                    contador=1
                            if contador==0:
                                print("este grupo no existe")
                            parki=0
                            if contador==1:
                                for i in miArchivo[0]["grupos"]:
                                    if i["nombres"]==modificar and len(i["grupo"])>0:
                                        for x in i["grupo"]:
                                            print("")
                                            print("--------------------------------")
                                            print("id:  ", x["id"])
                                            print("mombre:  ", x["nombre"])
                                            print("apellido:  ", x["apellido"])
                                            print("--------------------------------")
                                            print("")
                                        
                                        idmod=input("ingresa el id del estudiante al que le quieres asignar notas de algun modulo\n")
                                        for x in i["grupo"]:
                                            if idmod==x["id"]:
                                                notasmodulos()
                                                men=True
                                                while men==True:
                                                    try:
                                                        escojer=int(input("escoje de que modulo le asignaras las notas: "))
                                                        if escojer>=1 and escojer<=5:
                                                            duki=True
                                                            while duki==True:
                                                                try:
                                                                    teorica=float(input("nota de la prueba teorica: "))
                                                                    if teorica>=0 and teorica<=100:
                                                                        duki=False
                                                                    else:
                                                                        print("la nota deveria ser entre 0 y 100")
                                                                except ValueError:
                                                                    print("ingresa un numero valido")

                                                            teorica=teorica*0.3
                                                            duki=True
                                                            while duki==True:
                                                                try:
                                                                    practica=float(input("nota de la prueba practica: "))
                                                                    if practica>=0 and practica<=100:
                                                                        duki=False
                                                                    else:
                                                                        print("la nota deveria ser entre 0 y 100")
                                                                except ValueError:
                                                                    print("ingresa un numero valido")
                                                            
                                                            practica=practica*0.6
                                                            duki=True
                                                            while duki==True:
                                                                try:
                                                                    a=float(input("ingresa el promedio de las notas de los quizes/trabajos"))
                                                                    if a>=0 and a<=100:
                                                                        duki=False
                                                                    else:
                                                                        print("la nota deveria ser entre 0 y 100")
                                                                except ValueError:
                                                                    print("ingresa un numero valido")
                                                            a=a*0.1
                                                            
                                                            total=teorica+practica+a
                                                            if escojer==1:
                                                                if total<60:
                                                                    x["modulos"]["modulo1"]="desaprobado"
                                                                if total>=60:
                                                                    x["modulos"]["modulo1"]="aprobado"
                                                                notasmodulos()
                                                            if escojer==2:
                                                                if total<60:
                                                                    x["modulos"]["modulo2"]="desaprobado"
                                                                if total>=60:
                                                                    x["modulos"]["modulo2"]="aprobado"
                                                                notasmodulos()
                                                            if escojer==3:
                                                                if total<60:
                                                                    x["modulos"]["modulo3"]="desaprobado"
                                                                if total>=60:
                                                                    x["modulos"]["modulo3"]="aprobado"
                                                                notasmodulos()
                                                            if escojer==4:
                                                                if total<60:
                                                                    x["modulos"]["modulo4"]="desaprobado"
                                                                if total>=60:
                                                                    x["modulos"]["modulo4"]="aprobado"
                                                                notasmodulos()
                                                            if escojer==5:
                                                                if total<60:
                                                                    x["modulos"]["modulo5"]="desaprobado"
                                                                if total>=60:
                                                                    x["modulos"]["modulo5"]="aprobado"
                                                                notasmodulos()
                                                            
                                                            if escojer==6:
                                                                men=False
                                                    except ValueError:
                                                        print("ingresa una opción valida")
                                                print("cambio realizado")
                                                guardarArchivo(miArchivo)
                                                repit=input("quieres quieres repetir el proceso con otro camper (si)(no)\n")
                                                if repit=="no":
                                                    opc7=False
                                    else:
                                        parki=1
                                if parki==1:
                                        print("este grupo no tiene estudiantes")
                                            
                        menucoordinador()

                    if opc==7:
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
                    if opc==8:
                        miArchivo=abrirArchivo()
                        raw=True
                        while raw==True:
                            
                            print(":::::::::::::ACTUALIZAR DATOS DE CAMPERS:::::::::::::")
                            for i in miArchivo[0]["grupos"]:
                                print(i["nombres"])
                            grum=input("ingrese el nombre del grupo en que desea actualizar datos:  ")
                            for i in miArchivo[0]["grupos"]:
                                    if i["nombres"]==grum:
                                        for a in i["grupo"]:
                                            print(" ")
                                            print("==================================================")
                                            print("id: ",a["id"])
                                            print("nombre: ", a["nombre"])
                                            print("apellido: ", a["apellido"])
                                            print("edad: ", a["edad"])
                                            print("direccion: ", a["direccion"])
                                            print("acudiente: ", a["acudiente"])
                                            print("telefono: ", a["telefono"])
                                            print("riesgo: ", a["riesgo"])
                                            print("===================================================")
                                            print("")

                                        menumodificaciones()
                                        nada=True
                                        while nada==True:
                                            try:
                                                opc=int(input("ingrese su opcion para modificar: "))
                                                if opc>8 or opc<1:
                                                    print("ingresa una opción de las que se muestran")        
                                                if opc==1:
                                                    miArchivo=abrirArchivo()
                                                    print("======= MODIFICAR NOMBRE ========")
                                                    ingid=input("ingrese la id del campers a modificar: ")
                                                    for i in miArchivo[0]["grupos"]:
                                                        for a in i["grupo"]:
                                                            if a["id"]==ingid:
                                                                nuevoNombre=input("ingrese el nuevo nombre del camper: ")
                                                                a["nombre"]=nuevoNombre
                                                                guardarArchivo(miArchivo)
                                                                print("cambio realizado con exito") 
                                                                print("")
                                                    menumodificaciones() 
                                                            
                                                if opc==2:
                                                    miArchivo=abrirArchivo()
                                                    print("======= MODIFICAR APELLIDO ========")
                                                    ingid=input("ingrese la id del campers a modificar: ")
                                                    for i in miArchivo[0]["grupos"]:
                                                        for a in i["grupo"]:
                                                            if a["id"]==ingid:
                                                                nuevoApellido=input("ingrese el apellido del camper: ")
                                                                a["apellido"]=nuevoApellido
                                                                guardarArchivo(miArchivo)
                                                                print("cambio realizado con exito")
                                                                print("")
                                                    menumodificaciones()
                                                if opc==3:
                                                    miArchivo=abrirArchivo()
                                                    print("======= MODIFICAR EDAD ========")
                                                    ingid=input("ingrese la id del campers a modificar: ")
                                                    for i in miArchivo[0]["grupos"]:
                                                        for a in i["grupo"]:
                                                            if a["id"]==ingid:
                                                                nuevoEdad=input("ingrese la edad del camper: ")
                                                                a["edad"]=nuevoEdad
                                                                guardarArchivo(miArchivo)
                                                                print("cambio realizado con exito")
                                                                print("")
                                                    menumodificaciones()
                                                if opc==4:
                                                    miArchivo=abrirArchivo()
                                                    print("======= MODIFICAR DIRECCION========")
                                                    ingid=input("ingrese la id del campers a modificar: ")
                                                    for i in miArchivo[0]["grupos"]:
                                                        for a in i["grupo"]:
                                                            if a["id"]==ingid:
                                                                nuevaDireccion=input("ingrese la direccion del camper: ")
                                                                a["direccion"]=nuevaDireccion
                                                                guardarArchivo(miArchivo)
                                                                print("cambio realizado con exito")
                                                                print("")
                                                    menumodificaciones() 
                                                            
                                                if opc==5:
                                                    miArchivo=abrirArchivo()
                                                    print("======= MODIFICAR ACUDIENTE ========")
                                                    ingid=input("ingrese la id del campers a modificar: ")
                                                    for i in miArchivo[0]["grupos"]:
                                                        for a in i["grupo"]:
                                                            if a["id"]==ingid:
                                                                nuevoAcudiente=input("ingrese el acudiente del camper: ")
                                                                a["acudiente"]=nuevoAcudiente
                                                                guardarArchivo(miArchivo)
                                                                print("cambio realizado con exito")
                                                                print("")
                                                    menumodificaciones() 
                                                            
                                                if opc==6:
                                                    miArchivo=abrirArchivo()
                                                    print("======= MODIFICAR NUMERO DE TELEFONO========")
                                                    ingid=input("ingrese la id del campers a modificar: ")
                                                    for i in miArchivo[0]["grupos"]:
                                                        for a in i["grupo"]:
                                                            if a["id"]==ingid:
                                                                nuevoNumeroCelular=int(input("ingrese el numero del celular del camper: "))
                                                                a["telefono"]["celular"]=nuevoNumeroCelular
                                                                guardarArchivo(miArchivo)
                                                                print("cambio realizado con exito")
                                                                print("")
                                                    menumodificaciones() 
                                                        
                                                if opc==7:
                                                    miArchivo=abrirArchivo()
                                                    print("======= MODIFICAR NUMERO FIJO========")
                                                    ingid=input("ingrese la id del campers a modificar: ")
                                                    for i in miArchivo[0]["grupos"]:
                                                        for a in i["grupo"]:
                                                            if a["id"]==ingid:
                                                                nuevoNumeroFijo=int(input("ingrese el numero fijo del camper: "))
                                                                a["telefono"]["fijo"]=nuevoNumeroFijo
                                                                guardarArchivo(miArchivo)
                                                                print("cambio realizado con exito")
                                                                print("")
                                                    menumodificaciones() 
                                                if opc==8:
                                                    print("... ")
                                                    nada=False
                                            except ValueError:
                                                print("ingresa una opcion valida")
                                        sino=input("quieres repetir el proceso con otro camper(si)\n"
                                                   "para volver al menu de coordinador presiona enter")
                                        if sino!="si":
                                            raw=False
                        menucoordinador()
                    if opc==9:
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
                                if d["estado"]=="cursando":
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
                            if i["ruta"]!="":
                                
                                print(" ")
                                print("==================================================")
                                print("id: ",i["id"])
                                print("nombre: ", i["nombre"])
                                print("apellido: ", i["apellido"])
                                print("ruta: ", i["ruta"]["ruta"])
                                print("modulos", i["ruta"]["modulos"])
                                print("===================================================")
                                print("")
                        for i in  miArchivo[0]["grupos"]:
                                
                            if i["ruta"]=="NetCore" or i["ruta"]=="java" or i["ruta"]=="nodeJS":
                                print(" ")
                                print(":::::CAMPERS CON RUTA:::::::")
                                for a in i["grupo"]:
                                    print(" ")
                                    print("ruta: ", i["ruta"])
                                    print("modulos: ", i["modulos"])
                                    print("nombre:  ", i["nombres"])
                                    print("==================================================")
                                    print("id: ",a["id"])
                                    print("nombre: ", a["nombre"])
                                    print("apellido: ", a["apellido"])
                                    print("===================================================")
                                    print("")
                        menureportes()

                    if opc==6:
                        miArchivo=abrirArchivo()
                        opcion6=True
                        while opcion6==True:
                            for i in miArchivo[0]["grupos"]:
                                print("")
                                print("--------------------------------")
                                print("ruta:  ", i["ruta"])
                                print("")
                            pregunt=input("que ruta quieres ver")
                            for i in miArchivo[0]["grupos"]:
                                if pregunt==i["ruta"]:
                                    print("--------------------------------")
                                    print("ruta:  ", i["ruta"])
                                    print("")
                                    for z in miArchivo[0]["trainers"]:
                                        if z["ruta"]==i["ruta"]:
                                            print("trainer encargado")
                                            print("")
                                            print("id: ", z["id"])
                                            print("nomdre: ", z["nombre"])
                                            print("apellido: ", z["apellido"])
                                            print("")
                                    notasmodulos()
                                    diez=True
                                    while diez==True:
                                        try:
                                            opc6=int(input("que modulo quieres ver\n"))
                                            if opc6==1:
                                                print("campers que aprobaron el modulo")
                                                print("fundamentos de programacion:  ", i["modulos"]["fundamentos de programacion"])
                                                print("")
                                                for r in i["grupo"]:
                                                    if "modulo1" in r["modulos"]:
                                                        if r["modulos"]["modulo1"]=="aprobado":
                                                            print("------------------------")
                                                            print("id: ", r["id"])
                                                            print("nomdre: ", r["nombre"])
                                                            print("apellido: ", r["apellido"])
                                                            print("resultado del modulo: ", r["modulos"]["modulo1"])
                                                            print("------------------------")
                                                            print("")
                                                print("campers que no aprobaron el modulo")
                                                print("fundamentos de programacion:  ", i["modulos"]["fundamentos de programacion"])
                                                print("")
                                                for r in i["grupo"]:
                                                    if "modulo1" in r["modulos"]:
                                                        if r["modulos"]["modulo1"]=="desaprovado":
                                                            print("------------------------")
                                                            print("id: ", r["id"])
                                                            print("nomdre: ", r["nombre"])
                                                            print("apellido: ", r["apellido"])
                                                            print("resultado del modulo: ", r["modulos"]["modulo1"])
                                                            print("------------------------")
                                                            print("")
                                                notasmodulos()
                                            if opc6==2:
                                                print("campers que aprobaron el modulo")
                                                print("programacion web: ", i["modulos"]["programacion web"])
                                                print("")
                                                for r in i["grupo"]:
                                                    if "modulo2" in r["modulos"]:
                                                        if r["modulos"]["modulo2"]=="aprobado":
                                                            print("------------------------")
                                                            print("id: ", r["id"])
                                                            print("nomdre: ", r["nombre"])
                                                            print("apellido: ", r["apellido"])
                                                            print("resultado del modulo: ", r["modulos"]["modulo2"])
                                                            print("------------------------")
                                                            print("")
                                                print("campers que no aprobaron el modulo")
                                                print("programacion web: ", i["modulos"]["programacion web"])
                                                print("")
                                                for r in i["grupo"]:
                                                    if "modulo2" in r["modulos"]:
                                                        if r["modulos"]["modulo2"]=="desaprovado":
                                                            print("------------------------")
                                                            print("id: ", r["id"])
                                                            print("nomdre: ", r["nombre"])
                                                            print("apellido: ", r["apellido"])
                                                            print("resultado del modulo: ", r["modulos"]["modulo2"])
                                                            print("------------------------")
                                                            print("")
                                                notasmodulos()
                                            if opc6==3:
                                                print("campers que aprobaron el modulo")
                                                print("programacion formal:  ", i["modulos"]["programacion formal"])
                                                print("")
                                                for r in i["grupo"]:
                                                    if "modulo3" in r["modulos"]:
                                                        if r["modulos"]["modulo3"]=="aprobado":
                                                            print("------------------------")
                                                            print("id: ", r["id"])
                                                            print("nomdre: ", r["nombre"])
                                                            print("apellido: ", r["apellido"])
                                                            print("resultado del modulo: ", r["modulos"]["modulo3"])
                                                            print("------------------------")
                                                            print("")
                                                print("campers que no aprobaron el modulo")
                                                print("programacion formal:  ", i["modulos"]["programacion formal"])
                                                print("")
                                                for r in i["grupo"]:
                                                    if "modulo3" in r["modulos"]:
                                                        if r["modulos"]["modulo3"]=="desaprovado":
                                                            print("------------------------")
                                                            print("id: ", r["id"])
                                                            print("nomdre: ", r["nombre"])
                                                            print("apellido: ", r["apellido"])
                                                            print("resultado del modulo: ", r["modulos"]["modulo3"])
                                                            print("------------------------")
                                                            print("")
                                                notasmodulos()
                                            if opc6==4:
                                                print("campers que aprobaron el modulo")
                                                print("bases de datos:  ", i["modulos"]["bases de datos"])
                                                print("")
                                                for r in i["grupo"]:
                                                    if "modulo4" in r["modulos"]:
                                                        if r["modulos"]["modulo4"]=="aprobado":
                                                            print("------------------------")
                                                            print("id: ", r["id"])
                                                            print("nomdre: ", r["nombre"])
                                                            print("apellido: ", r["apellido"])
                                                            print("resultado del modulo: ", r["modulos"]["modulo4"])
                                                            print("------------------------")
                                                            print("")
                                                print("campers que no aprobaron el modulo")
                                                print("bases de datos:  ", i["modulos"]["bases de datos"])
                                                print("")
                                                for r in i["grupo"]:
                                                    if "modulo4" in r["modulos"]:
                                                        if r["modulos"]["modulo4"]=="desaprovado":
                                                            print("------------------------")
                                                            print("id: ", r["id"])
                                                            print("nomdre: ", r["nombre"])
                                                            print("apellido: ", r["apellido"])
                                                            print("resultado del modulo: ", r["modulos"]["modulo4"])
                                                            print("------------------------")
                                                            print("")
                                                notasmodulos()
                                            if opc6==5:
                                                print("campers que aprobaron el modulo")
                                                print("backend:  ", i["modulos"]["backend"])
                                                print("")
                                                for r in i["grupo"]:
                                                    if "modulo5" in r["modulos"]:
                                                        if r["modulos"]["modulo5"]=="aprobado":
                                                            print("------------------------")
                                                            print("id: ", r["id"])
                                                            print("nomdre: ", r["nombre"])
                                                            print("apellido: ", r["apellido"])
                                                            print("resultado del modulo: ", r["modulos"]["modulo5"])
                                                            print("------------------------")
                                                            print("")
                                                print("campers que no aprobaron el modulo")
                                                print("backend:  ", i["modulos"]["backend"])
                                                print("")
                                                for r in i["grupo"]:
                                                    if "modulo5" in r["modulos"]:
                                                        if r["modulos"]["modulo5"]=="desaprovado":
                                                            print("------------------------")
                                                            print("id: ", r["id"])
                                                            print("nomdre: ", r["nombre"])
                                                            print("apellido: ", r["apellido"])
                                                            print("resultado del modulo: ", r["modulos"]["modulo5"])
                                                            print("------------------------")
                                                            print("")
                                                notasmodulos()
                                            if opc6==6:
                                                diez=False
                                        except ValueError:
                                            print("ingresa una opcion valida")
                            lola=input("quieres volver al menu de reportes (si)(no)\n")
                            if lola=="si":
                                opcion6=False
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

#desarrollado por Caicedo Bermon Luis Miguel c.c: 1090381345
#desarrollado por Botello Garcia Yurley t.i: 1066085539