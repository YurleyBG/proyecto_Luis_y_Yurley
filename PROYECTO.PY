import json 
from datetime import datetime,timezone
def abrirArchivo():
    datos=[]
    with open("info.json", encoding="utf-8") as openfile:#esto es para abrir el json
        datos=json.load(openfile)
    return datos

def guardarArchivo(midato):
    with open("info.json", "w") as file:
        json.dump(midato,file)#esto nos permite guardar las modificaciones  que se hagan dentro del archivo python al json

def menu():#menu principal
    print("")
    print(":::::::::BIENBENIDO A NUESTRA PLATAFORMA::::::::\n"
          "1 MODULO DE COORDINACION ACADEMICA\n"
          "2 MODULO DE TRAINER\n"
          "3 MODULO DE REPORTE\n"
          "4 REGISTRAR ENTRADA\n"
          "5 SALIR")
    
def menucoordinador():#submenu principal del coordinador
    print("::::::::::MENÚ::::::::::\n"
          "1 listar estudiantes\n"
          "2 ingresar nuevos campers\n"
          "3 modulo de matriculas\n"
          "4 crear rutas academicas con los modulos\n"
          "5 asignar rutas de entrenamiento a los traniers\n"
          "6 notas de modulos\n"
          "7 consultar campers con riesgo alto\n"
          "8 actualizar datos de campers\n"
          "9 volver al menu principal\n"
          ":::::::::::::::::::::::::\n")
def menumodiftrainer():#submenu de trainer para actualizaciones de datos
    print(":::::::::: MENÚ DE DATOS ::::::::::\n"
          "1 Nombre\n"
          "2 Apellido\n"
          "3 Telefono\n"
          "4 User\n"
          "5 Contraseña\n"
          "6 Edad\n"
          "7 Finalizar\n"
          ":::::::::::::::::::::::::::::::::::\n")



def menutrainer():#submenu principal del trainer
    print("::::::::::::::MENÚ:::::::::::::\n"
          "1 mostrar horarios y ruta\n"
          "2 actualizar datos\n"
          "3 salir")


def menureportes():#submenu para  el modulo de reporte 
     print("::::::::::MENÚ::::::::::\n"
           "1 listar campers inscritos\n"
           "2 listar los campers que aprobaron el examen principal\n"
           "3 listar todos los entrenadores\n"
           "4 listar campers de bajo rendimiento\n"
           "5 listar campers y trainers que tienen ruta de entrenamiento\n"
           "6 mostrar cuantos campers perdieron y aprobaron cada uno de los modulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado\n"
           "7 volver al menu principal")

def menumodificaciones():#submenu de modificaciones de datos de coordinador
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
    
def notasmodulos():#submenu del coordinador para la asignacion de notas en cada modulo
    print("------------MODULOS------------")
    print("1 fundamentos de programacion")
    print("2 programacion web")
    print("3 programacion formal")
    print("4 bases de datos")
    print("5 backend")
    print("6 finalizar")



     

miArchivo=[]#lista vacia
miArchivo=abrirArchivo()#se abre el json dentro de la anterior lista
menu()#imprimimos el menu principal
bool=True
while bool==True:#utilizamos un while para la creacion de un bucle
    try:#nos permitira corregir aalgunos errores que se comentan al ingresar un valor invalido
        opc=int(input("ingrese su opcion por favor: "))#le pide al usuario ingresar su opcion
        if opc==1:
            print("")
            print("MODULO DE COORDINACION ACADEMICA")
            print("")
            menucoordinador()
            ver=True
            while ver==True:
                try:
                    opc=int(input("ingrese su opcion por favor: "))#le pide al coordinador ingresar su opcion
                    if opc==1:
                        for i in range(len(miArchivo[0]["grupos"])):#va contar la cantidad de grupos que hayan
                            print("--------")
                            print(miArchivo[0]["grupos"][i]["nombres"])#luego imprimira solo el nombre de cada grupo
                            cont=0#utilizamos un contador en cero para mas tarde cuando se imprima un camper vaya mostrando la cantidad que hay.
                        punch=True
                        while punch==True:
                            cell=0#contador en cero
                            gru=input("que grupo quieres listar\n")#le pedimos al coordinador ingresar el grupo que desea listar
                            for i in miArchivo[0]["grupos"]:#nos ubicamos a traves de un for en los grupos 
                                if i["nombres"]==gru:#luego comparams si los nombres dentro de ese grupo es igual al que ingreso el usuario
                                    cell=1 #si el contador pasaa a uno al verificar la anterior condicion quiere decir que esta secumple
                                    punch=False
                            if cell==0:#de lo contrario si la condicion no se cumple imprimira lo siguiente y le permitira nuevamente ingresar al usuario
                                print("escoje un grupo de los que se mostraron (escribelo igual)")
                        for i in range(len(miArchivo[0]["grupos"])):#va contar la cantidad de grupos que hayan
                            if miArchivo[0]["grupos"][i]["nombres"]==gru:#permite comprobar si se encuentra si esto es asi le imprimira 
                                for z in miArchivo[0]["grupos"][i]["grupo"]:#con esto nos ubicamos en las posiciones grupos y grupo que se encuentran dentro del json para asi ir recorriendo y llamar los datos de los campers dentro de ese grupo. 
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
                        menucoordinador()#al finalizar lo anterior nos volvera a imprimir el menu de coordinador

                    if opc==2:
                        miArchivo=abrirArchivo()
                        bucle=True
                        while bucle==True:
                            print("")
                            print(":::::::::AÑADIR NUEVO CAMPER:::::::::")
                            old=True
                            while old==True:
                                fon=0#contador en cero
                                id=input("ingrese la id: ")#le pide al cooordinador ingresar una id 
                                for i in miArchivo[0]["grupos"]:# con un for nos posicionamos en grupos
                                    for z in i["grupo"]:#con el siguiente for en la opcion grupo que guarda a los campers
                                        if z["id"]==id:#si la anterior id ingresada ya se encuentra le imprimira lo siguiente
                                            print("este id ya existe, prueba con otro")
                                            fon=1#si el contador anterior pasa a 1 le imprimira esto y le dara la opcion de ingresar nuevamente
                                if fon==0: #de lo contrario finalizara y cerrara el bucle
                                    old=False
                            #le pedira al coordinador todo los datos requeridoa para la agregación de un nuevo camper               
                            nombre=input("ingrese el nombre: ")
                            apellido=input("ingrese el apellido: ")
                            edad=input("ingrese la edad: ")
                            direccion=input("ingrese la direccion: ")
                            acudiente=input("ingrese el nombre del acudiente:  ")
                            uno=True
                            while uno==True:
                                try:#el siguiente try nos mandara un error si lo anterior no es un numero valido
                                    celular=int(input("ingrese el numero:  "))
                                    uno=False
                                except ValueError:
                                    print("ingresa un numero valido")
                            uno=True
                            while uno==True:
                                try:#el siguiente try nos mandara un error si lo anterior no es un numero valido
                                    fijo=int(input("ingrese numero fijo:  "))
                                    uno=False
                                except ValueError:
                                    print("ingresa un numero valido")
                            #nos ubicamos en ingreso que seria al lugar donde queremos agregar al anterior camper que quedaara en estado de progreso de ingreso
                            miArchivo[0]["ingreso"].append({"id":id,"nombre":nombre,"apellido":apellido,"edad":edad, "direccion":direccion, "acudiente":acudiente, "telefono": {"celular":celular, "fijo":fijo},"estado":"progreso de ingreso", "riesgo":"", "modulos":{}})
                            print("se ha creado con exito!!")
                            guardarArchivo(miArchivo)#nos guardar todo los datos anteriores dentro de nuestro json
                            print("")#le preguntara al coordinador si desea agregar un nuevo camper si es asi se repitira el bucle de lo contrario este finalizara y le mostrara nuevamente el menu de coordinador.
                            si=input("quieres agregar otro camper(si)\n"
                                     "preciona enter para volver al menú\n")
                            if si!="si":
                                bucle=False
                        menucoordinador()
                    

                    if opc==3:
                        miArchivo=abrirArchivo()
                        way=True
                        while way==True:#imprimira a todos los campers en estado de ingreso
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
                            hola=True
                            while hola==True:
                                co=0
                                pedir=input("ingresa el id del estudiante al que le quieres asignar notas\n")#le pedira al coordinador ingresar la id del estudiante a ingresar las notas de la prueba inicial
                                for i in miArchivo[0]["ingreso"]:
                                    if pedir==i["id"]:#verificara si la id se encuentra si es asi finalizara el bucle y continuara con lo demas de lo contrario le imprimira que ese id no se encuentra o es invalido.
                                        co=1
                                        hola=False
                                if co==0:
                                    print("ingresa un id de los que se muestran")
                            for i in miArchivo[0]["ingreso"]:#nos posicionamos en ingreso donde se encuentra todos los campers en progreso de ingreso
                                if i["id"]==pedir:#si es asi le pidira ingresar la notas de la prueba teorica y practica
                                    archivo=i
                                    print("ingresa las notas")
                                    puno=True
                                    while puno==True:
                                        try:#estas notas no podran ser menores a 0 ni mayores a 100
                                            nota1=float(input("nota de la prueba teorica:  "))
                                            if nota1>=0 and nota1<=100:
                                                puno=False
                                            else:
                                                print("ingresa una nota entre 0 y 100")
                                        except ValueError:
                                            print("ingresa una nota valida")
                                    puno=True
                                    while puno==True:
                                        try:
                                            nota2=float(input("nota de la prueba practica:  "))
                                            if nota2>=0 and nota2<=100:
                                                puno=False
                                            else:
                                                print("ingresa una nota entre 0 y 100")
                                        except ValueError:
                                            print("ingresa una nota valida")
                                    #se multiplica  la nota por el promedio ya anteriormente dividido en 100
                                    nota1=nota1*0.4
                                    nota2=nota2*0.6
                                    resul=nota1+nota2#se suman los resultado para obtener la nota final
                                    print(resul)#imprime el resultado para que el usuario lo vea
                                    if resul>=60:#si la nota es mayoro igual a 60
                                        print("esta persona aprobó")#automaticamente le dira que aprobo y su estado cambiara a cursando
                                        i["estado"]="cursando" 
                                        print("estas son las rutas que estan disponibles")#le mostrara la rutas disponibles
                                        grups=[]#utilizamos una lista vacia para que se vayan agregando las nuevas rutas si que este superen el limite de estudiantes que son 33
                                        for i in miArchivo[0]["grupos"]:
                                            if len(i["grupo"])<33:
                                                print("--------")
                                                print(i["nombres"])
                                                print(i["ruta"])
                                                grups.append(i["nombres"])#se iran agregando a grups todo los nombres de los grupos
                                        soccer=True
                                        while soccer==True:
                                            pregunta2=input("ingresa el nombre del grupo que tiene la ruta que deseas:\n")#le pide que ingrese el nombre del gr
                                            if pregunta2 in grups:#si el nombre del grupo se encuentra en la lista grups anterior se terminara el bucle
                                                soccer=False
                                            else:
                                                print("este grupo no existe (o escribe bien el nombre)")#sino imprimira lo siguiente
                                        for i in miArchivo[0]["grupos"]:
                                            if pregunta2==i["nombres"]:
                                                i["grupo"].append(archivo)#se agregara el nuevo grupo
                                        print("se han aplicado los cambios")#le notificara que se aplicaron los cambios
                                    if resul<60:#si la nota es menor a 60 le indicara que la persona desaprobo
                                        print("esta persona no aprobó")#se lo  notificara
                                    sol=input("quieres hacer otro cambio (si)\n"#le preguntara si dese continuar o no
                                              "o presiona enter para volver al menú")
                                    if sol!="si":#si la respuesta es diferente a si se finalizara 
                                        way=False
                            for i in range(len(miArchivo[0]["ingreso"])-1,-1,-1):
                                if miArchivo[0]["ingreso"][i]["estado"]=="cursando":
                                    miArchivo[0]["ingreso"].pop(i)#si el estudiante paso la prueba su estado pasara a cursando y se eliminara de  ingresados
                            guardarArchivo(miArchivo)#guardara los datos anteriores
                            
                        menucoordinador()
                    if opc==4:
                        miArchivo=abrirArchivo()
                        
                        print("")

                        print(":::::::::: CREAR RUTAS ACADEMICAS CON LOS MODULOS ::::::::::::::")
                        yo=True
                        while yo==True:
                            rutas=[]
                            xd=0
                            for i in miArchivo[0]["grupos"]:
                                for n in range(len(i["ruta"])):
                                    xd=n
                                    rutas.append(i["ruta"])#añadiremos las rutas existentes a nuestra lista vacia rutas
                            if xd<12:#si las rutas son menores a 12 le permitira seguir ingresando de lo contrario le indicara que el maximo de ruta ya se alcanzo
                                ace=True
                                while ace==True:
                                    ruta=input("ingresa el nombre de la nueva ruta\n")#le pide al coordinador el nuevo nombre de la ruta
                                    if ruta not in rutas:#si la ruta no se encuentra en la lista rutas va romper el bucle y continuara con lo siguiente
                                        ace=False
                                    else:
                                        print("este nombre no está disponible\ningresa uno valido")#de lo contrario imprimira la siguiente  notificacion
                                for h in range(len(rutas)-1,-1,-1):
                                    rutas.pop(h)#se iran borrando todo lo anterior para que a medida que se repita el bucle no se repitan de los nombres de la rutas ya existentes
                                uno=True
                                while uno==True:#le permite escoger al coordinador  los nombres de los modulos que le quiere agregar a la nueva ruta creada
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
                                        print("ingrese una opción valida")#si a la hora de ingresar un numero este no se encuentra se repetira
                                
                                dos=True
                                while dos==True:
                                    print("escoje el modulo principal para bases de datos")#le permite escoger al coordinador  los nombres de los modulos que le quiere agregar a la nueva ruta creada
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
                                        print("ingrese una opción valida")#si a la hora de ingresar un numero este no se encuentra se repetira

                                tres=True
                                while tres==True:
                                    print("escoje el modulo secundario para bases de datos")#le permite escoger al coordinador  los nombres de los modulos que le quiere agregar a la nueva ruta creada
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
                                        print("ingrese una opción valida")#si a la hora de ingresar un numero este no se encuentra se repetira

                                cuatro=True
                                while cuatro==True:
                                    print("escoje el modulo principal para BACKEND")#le permite escoger al coordinador  los nombres de los modulos que le quiere agregar a la nueva ruta creada
                                    try:
                                        modulo31=int(input("1.NetCore  2.Spring Boot  3.NodeJS  4.Expres\n"))
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
                                        print("ingrese una opción valida")#si a la hora de ingresar un numero este no se encuentra se repetira
                                
                                cinco=True
                                while cinco==True:
                                    print("escoje el modulo secundario para BACKEND")#le permite escoger al coordinador  los nombres de los modulos que le quiere agregar a la nueva ruta creada
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
                                        print("ingrese una opción valida")#si a la hora de ingresar un numero este no se encuentra se repetira
                                listasalones=[]#se ingresaran los salones de entrenamiento en la lista
                                for p in miArchivo[0]["grupos"]:
                                    listasalones.append(p["salon de entrenamiento"])
                                #haremos unn contador que empiece desde cero y vaya contado cada salon que se encuentre de los mismo para que este no llegue a superan su limite de uso que son 4 grupos.
                                salon1=0
                                salon2=0
                                salon3=0
                                for h in range(len(listasalones)):
                                    if listasalones[h]=="aula1":
                                        salon1=salon1+1
                                    if listasalones[h]=="aula2":
                                        salon2=salon2+1
                                    if listasalones[h]=="aula3":
                                        salon3=salon3+1
                                listaaula=[]#se creara una lista vacia dende se guardaran los 3 salones de entrenamineto disponibles
                                if salon1<4:
                                    print("aula1")
                                    listaaula.append("aula1")
                                if salon2<4:
                                    print("aula2")
                                    listaaula.append("aula2")
                                if salon3<4:
                                    print("aula3")#se imprimen para que el coordinador vea los salones que hay y escoja alguno para agregarlo a la nueva ruta ceada.
                                    listaaula.append("aula3")

                                yuju=True
                                while yuju==True:
                                    escoje=input("escoje un salon de entranamiento de los que acabo de mostrar\n")
                                    if escoje in listaaula: #si escoje se encuentra en la listaaula se rompera el bucle  y continuara
                                        yuju=False
                                    else:
                                        print("esta aula no esta disponible o lo escribiste mal")#de lo contrario le imprimira la siguiente notificacion
                                
                                fechaI=input("ingresa la fecha de INICIO DD-MM-AA\n")#le pide ingresar la fecha de inicio
                                fechaF=input("ingresa la fecha de FINALIZACIÓN DD-MM-AA\n")#le pide ingresar la fecha de finalizacion
                                nuevonombre=input("ingresa el nombre del nuevo grupo\n")#le pide ingresar el nuevo nombre del nuevo grupo 
                                miArchivo[0]["grupos"].append({"ruta":ruta, "modulos":{"fundamentos de programacion": ["introduccion a la algoritmia", "PSeint", "Python"],
                                                                                        "programacion web": ["HTML", "CSS", "booststrap"],
                                                                                        "programacion formal":num1,
                                                                                        "bases de datos":[num2,num3],
                                                                                        "backend":[num4,num5]}, "nombres":nuevonombre,"fecha de inicio":fechaI,"fecha de finalizacion":fechaF,"salon de entrenamiento":escoje, "grupo":[]})#agregara todo esos datos guardandolos en el json y asi mismo finalizando la creacion de la nueva ruta de entrenamiento.
                                cambio=input("SE HA CREADO LA RUTA CON EXITO\n"#le preguntara al coordinador si desea crear un anueva ruta
                                                "crear otra ruta: (si)\n"
                                                "volver al menu: preciona enter\n")
                                if cambio!="si":#si la respuesta es difernete de si, se rompera el bucle y volvera al menu de coordinado
                                    yo=False
                            else:
                                print("ya se alcanzó el maximo de rutas que se pueden crear")
                                yo=False
                            guardarArchivo(miArchivo)
                        menucoordinador()

                    if opc==5:
                        miArchivo=abrirArchivo()
                        ole=True
                        while ole==True:
                            for i in miArchivo[0]["trainers"]:
                                if len(i["ruta"])<4:#si la ruta es menor a 4 se imprimira los datos del trainers de lo contraio no se hara
                                    print("")
                                    print("--------------------------------")
                                    print("id:  ", i["id"])
                                    print("nombre: ", i["nombre"])
                                    print("apellido", i["apellido"])
                                    print("--------------------------------")
                                    print("")
                            miau=True
                            while miau==True:
                                cont=0#con este contador permitiremos verificar la condicion siguiente si esta se cumple el contador pasara a ser uno y le permitira continuar de lo contrario si ests sigue siendo igual a 0 le imprimira  una notificacion de error.
                                try:
                                    seleccion=int(input("ingresa el id del trainer al que le quieres asignar una ruta\n"))#le pide la id del trainer a ingresarle la ruta
                                    for i in miArchivo[0]["trainers"]:
                                        if len(i["ruta"])<4 and seleccion==i["id"]:
                                            cont=1
                                            miau=False
                                    if cont==0:
                                        print("ingresa un id de los que muestran")
                                except ValueError:
                                    print("ingresa un id valido")
                            if cont==1:
                                listarutas=[]
                                for a in miArchivo[0]["grupos"]:
                                    rutacont=0
                                    for i in miArchivo[0]["trainers"]:
                                        for z in range(len(i["ruta"])):
                                            if i["ruta"][z]==a["ruta"]:#si la ruta de los trainers e igual a la ruta de los campers  el contador debera ser igual a 0 asi le permitira seguir con el proceso.
                                                rutacont=1#al pasar a el contador a 1 quiere decir que la ruta ya se encuentra ocupada por algun trainers por lo tanto no se imprimira la ruta
                                    if rutacont==0:#si el contador es igual a 0 se imprimiran las rutas disponibles o que no tiene trainer 
                                        print("ruta: ", a["ruta"])
                                        listarutas.append(a["ruta"])
                                if len(listarutas)>0:
                                    for x in miArchivo[0]["trainers"]:
                                        if x["id"]==seleccion:#si la id de los trainers es igual a la anterior ingresada
                                            piece=True
                                            while piece==True:
                                                son=0
                                                qwerty=input("escoje una ruta:  ")#le permitira escojer la ruta a añadirle
                                                for m in range(len(listarutas)):
                                                    if listarutas[m]==qwerty:#si se encuentra rompera el bucle
                                                        son=1
                                                        piece=False
                                                if son==0:#si la ruta no se encuentra disponible imprimira lo siguiente
                                                    print("esta ruta no esta disponible")
                                                    print("ingresa una ruta de las que se mostraron")
                                            
                                            for l in range(len(listarutas)-1,-1,-1):
                                                listarutas.pop(l)
                                            x["ruta"].append(qwerty)
                                            guardarArchivo(miArchivo)#la ruta anterior escogida se agregara a la ruta del trainer y se eliminara de la lista anterior
                                            print("ruta agregada con exito")#le imprimira la siguiente notificacion
                                            pregun=input("quieres hacer otro cambio (si)\n"
                                                        "si no quieres preciona enter\n")#le preguntara si  desea escribirle 
                                            if pregun!="si":
                                                ole=False
                        menucoordinador()
                    
                    if opc==6:
                        miArchivo=abrirArchivo()
                        for z in miArchivo[0]["grupos"]:#nos posicionaremos en grupos para mostrar la rutas,modulos y grupos
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
                            modificar=input("ingresa el nombre del grupo donde vas a asignar notas\n")#le pedira al cordinador ingresar el grupo  en donde asignara notas
                            for i in miArchivo[0]["grupos"]:
                                if i["nombres"]==modificar:#si el nombre ingresado se encuentra entre los noombres de grupo
                                    contador=1#su contador pasara a ser 1 y le permitira continuar con el procesos de asignacion de notas
                            if contador==0:#si de lo contrario es 0
                                print("este grupo no existe")#le notificara lo siguiente
                            parki=0
                            if contador==1:
                                for i in miArchivo[0]["grupos"]:
                                    if i["nombres"]==modificar and len(i["grupo"])>0:#si nombre de grupo es igual al ingresado y estes es mayor a 0 en cantidad de estudiante continuara
                                        for x in i["grupo"]:
                                            print("")
                                            print("--------------------------------")
                                            print("id:  ", x["id"])
                                            print("mombre:  ", x["nombre"])
                                            print("apellido:  ", x["apellido"])
                                            print("--------------------------------")
                                            print("")
                                        
                                        idmod=input("ingresa el id del estudiante al que le quieres asignar notas de algun modulo\n")# le pedira la id del camper a asignar notas
                                        for x in i["grupo"]:
                                            if idmod==x["id"]:#y si la id es igual a la agregada 
                                                notasmodulos()#imprimira el menu de modulos
                                                men=True
                                                while men==True:
                                                    try:
                                                        escojer=int(input("escoje de que modulo le asignaras las notas: "))#le pide al coordinador escribir su opcion
                                                        if escojer>=1 and escojer<=5:#si la opciones son mayores o igual a 1  y  menor o igual a 5 continuara 
                                                            duki=True
                                                            while duki==True:
                                                                try:#le permite asignar la notas practica de 0 a 100 de lo contrario ci superan estos datos le imprimira una notificacion
                                                                    teorica=float(input("nota de la prueba teorica: "))
                                                                    if teorica>=0 and teorica<=100:
                                                                        duki=False
                                                                    else:
                                                                        print("la nota deveria ser entre 0 y 100")
                                                                except ValueError:
                                                                    print("ingresa un numero valido")

                                                            teorica=teorica*0.3#multiplicara la nota por el porcentaje ya dividido en 100
                                                            duki=True
                                                            while duki==True:
                                                                try:#le permite asignar la notas practica de 0 a 100 de lo contrario ci superan estos datos le imprimira una notificacion
                                                                    practica=float(input("nota de la prueba practica: "))
                                                                    if practica>=0 and practica<=100:
                                                                        duki=False#si esto se cumple continuara y rompera el bucle
                                                                    else:
                                                                        print("la nota deveria ser entre 0 y 100")
                                                                except ValueError:
                                                                    print("ingresa un numero valido")
                                                            
                                                            practica=practica*0.6#multiplicara la nota por el porcentaje ya dividido en 100
                                                            duki=True
                                                            while duki==True:
                                                                try:
                                                                    a=float(input("ingresa el promedio de las notas de los quizes/trabajos"))#le permitira ingresar el promedio de sus trabajos
                                                                    if a>=0 and a<=100:
                                                                        duki=False#si esto se cumple continuara y rompera el bucle
                                                                    else:
                                                                        print("la nota deveria ser entre 0 y 100")
                                                                except ValueError:
                                                                    print("ingresa un numero valido")
                                                            a=a*0.1#esa nota se multiplicara por el porcentaje que anteriormente se dividio en 100
                                                            
                                                            total=teorica+practica+a#se sumaran las notas y se sacara la calificacion final
                                                            if escojer==1:#dependiendo si la nota es mayor o menor a 60 le indicara si aprobo o desaprobo el modulo, asi con cada uno
                                                                if total<60:
                                                                    x["modulos"]["modulo1"]="desaprobado"#si el total es menor a 60 desaprueba
                                                                if total>=60:
                                                                    x["modulos"]["modulo1"]="aprobado"#si el total es mayor a 60 aprueba
                                                                notasmodulos()#seguira imprimiendo el menu de modulo
                                                            if escojer==2:
                                                                if total<60:
                                                                    x["modulos"]["modulo2"]="desaprobado"#si el total es menor a 60 desaprueba
                                                                if total>=60:
                                                                    x["modulos"]["modulo2"]="aprobado"#si el total es mayor a 60 aprueba
                                                                notasmodulos()#seguira imprimiendo el menu de modulo
                                                            if escojer==3:
                                                                if total<60:
                                                                    x["modulos"]["modulo3"]="desaprobado"#si el total es menor a 60 desaprueba
                                                                if total>=60:
                                                                    x["modulos"]["modulo3"]="aprobado"#si el total es mayor a 60 aprueba
                                                                notasmodulos()#seguira imprimiendo el menu de modulo
                                                            if escojer==4:
                                                                if total<60:
                                                                    x["modulos"]["modulo4"]="desaprobado"#si el total es menor a 60 desaprueba
                                                                if total>=60:
                                                                    x["modulos"]["modulo4"]="aprobado"#si el total es mayor a 60 aprueba
                                                                notasmodulos()#seguira imprimiendo el menu de modulo
                                                            if escojer==5:
                                                                if total<60:
                                                                    x["modulos"]["modulo5"]="desaprobado"#si el total es menor a 60 desaprueba
                                                                if total>=60:
                                                                    x["modulos"]["modulo5"]="aprobado"#si el total es mayor a 60 aprueba
                                                                notasmodulos()#seguira imprimiendo el menu de modulo
                                                            
                                                            if escojer==6:#si elige la opcion se saldra del menu modulo 
                                                                men=False#se finalizara el bucle
                                                    except ValueError:
                                                        print("ingresa una opción valida")#esto sera notificado sino se cumple lo anterior
                                                print("cambio realizado")#le notificara el cambio realizado
                                                guardarArchivo(miArchivo)#se guardara
                                                repit=input("quieres quieres repetir el proceso con otro camper (si)(no)\n")
                                                if repit=="no":#le preguntara si desea repetir el proceso con otro camper
                                                    opc7=False#si no finalizara 
                                    else:
                                        parki=1
                                if parki==1:
                                        print("este grupo no tiene estudiantes")#si el grupo ingresado no tiene campers imprimira esto.
                                            
                        menucoordinador()#volvera a mostrar el menu de coordinador

                    if opc==7:
                        miArchivo=abrirArchivo()
                        for i in miArchivo[0]["grupos"]:#nos posicionamos en grupos
                            for z in i["grupo"]:#luego en grupo donde se encuentran los campers
                                one=0#el contador ira guardando a cantidad de modulos desaprobado dependiendo de esto indicara su riesgo
                                #si los modulos1,2,3,4 y 5 se encuentran en estado desaprobado si es asise iran contando los modulos que tiene desaprobado dependiendo de si su cantida es mayor o igual a 3 se le asignara su tipo de riesgo
                                if "modulo1" in z["modulos"]:
                                    if z["modulos"]["modulo1"]=="desaprobado":
                                        one=one+1
                                if "modulo2" in z["modulos"]:
                                    if z["modulos"]["modulo2"]=="desaprobado":
                                        one=one+1
                                if "modulo3" in z["modulos"]:
                                    if z["modulos"]["modulo3"]=="desaprobado":
                                        one=one+1
                                if "modulo4" in z["modulos"]:
                                    if z["modulos"]["modulo4"]=="desaprobado":
                                        one=one+1
                                if "modulo5" in z["modulos"]:
                                    if z["modulos"]["modulo5"]=="desaprobado":
                                        one=one+1
                                if one>=3:
                                    z["riesgo"]="alto"#si su catidad de desaprobado es igual o mayor a 3 se encuentra en riesgo alto
                                else:
                                    z["riesgo"]="bajo"#de lo contrario su riesgo sera bajo
                        guardarArchivo(miArchivo)#se guradaran los cambios
                        print("") 
                        print("::::::::::::::CAMPERS CON RIESGO ALTO:::::::::::::::") 
                        print("")
                        print("::::::Estos campers recibiran un llamado de atencion:::::::::")
                        for i in miArchivo[0]["grupos"]:
                            for b in i["grupo"]:
                        
                                if b["riesgo"]=="alto":#imprimira a solo esos campers que se encuentran con un riesgo alto
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
                            for i in miArchivo[0]["grupos"]:#nos posicionamos en grupos
                                print(i["nombres"])#nos imprimira los umbres de los grupos
                            grum=input("ingrese el nombre del grupo en que desea actualizar datos:  ")#nos pidira que ingresemos el nombre del grupo donde se encuentra el camper que queremos modificar.
                            for i in miArchivo[0]["grupos"]:
                                    if i["nombres"]==grum:#si lo ingresado es igual al nombre del grupo imprimiras los estudiates ahi cursando
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

                                        menumodificaciones()#imprimimos menu de modificaciones
                                        nada=True
                                        while nada==True:
                                            try:
                                                opc=int(input("ingrese su opcion para modificar: "))#le pide al coordinador ingresar una opcion a modificar
                                                if opc>8 or opc<1:#si opcion es mayor a 8 omenor a 1 imprimira la siguiente notificacion
                                                    print("ingresa una opción de las que se muestran")        
                                                if opc==1:
                                                    miArchivo=abrirArchivo()
                                                    print("======= MODIFICAR NOMBRE ========")
                                                    ingid=input("ingrese la id del campers a modificar: ")#se ingresa la id  del camper a modificar
                                                    for i in miArchivo[0]["grupos"]:
                                                        for a in i["grupo"]:
                                                            if a["id"]==ingid:#se compara si la id ingresada si se encuentra
                                                                nuevoNombre=input("ingrese el nuevo nombre del camper: ")#si es asi le pedira ingresar el nuevo nombre
                                                                a["nombre"]=nuevoNombre#actualizara los datos en el json y lo guardara
                                                                guardarArchivo(miArchivo)
                                                                print("cambio realizado con exito") #le notificara que su cambio fue realizado
                                                                print("")
                                                    menumodificaciones() 
                                                            
                                                if opc==2:
                                                    miArchivo=abrirArchivo()
                                                    print("======= MODIFICAR APELLIDO ========")
                                                    ingid=input("ingrese la id del campers a modificar: ")#se ingresa la id  del camper a modificar
                                                    for i in miArchivo[0]["grupos"]:
                                                        for a in i["grupo"]:
                                                            if a["id"]==ingid:#se compara si la id ingresada si se encuentra
                                                                nuevoApellido=input("ingrese el apellido del camper: ")#si es asi le pedira ingresar el nuevo apellido
                                                                a["apellido"]=nuevoApellido#actualizara los datos en el json y lo guardara
                                                                guardarArchivo(miArchivo)
                                                                print("cambio realizado con exito")#le notificara que su cambio fue realizado
                                                                print("")
                                                    menumodificaciones()
                                                if opc==3:
                                                    miArchivo=abrirArchivo()
                                                    print("======= MODIFICAR EDAD ========")
                                                    ingid=input("ingrese la id del campers a modificar: ")#se ingresa la id  del camper a modificar
                                                    for i in miArchivo[0]["grupos"]:
                                                        for a in i["grupo"]:
                                                            if a["id"]==ingid:#se compara si la id ingresada si se encuentra
                                                                nuevoEdad=input("ingrese la edad del camper: ")#si es asi le pedira ingresar la nueva edad
                                                                a["edad"]=nuevoEdad#actualizara los datos en el json y lo guardara
                                                                guardarArchivo(miArchivo)
                                                                print("cambio realizado con exito")#le notificara que su cambio fue realizado
                                                                print("")
                                                    menumodificaciones()
                                                if opc==4:
                                                    miArchivo=abrirArchivo()
                                                    print("======= MODIFICAR DIRECCION========")
                                                    ingid=input("ingrese la id del campers a modificar: ")#se ingresa la id  del camper a modificar
                                                    for i in miArchivo[0]["grupos"]:
                                                        for a in i["grupo"]:
                                                            if a["id"]==ingid:#se compara si la id ingresada si se encuentra
                                                                nuevaDireccion=input("ingrese la direccion del camper: ")#si es asi le pedira ingresar la nueva direcccion
                                                                a["direccion"]=nuevaDireccion#actualizara los datos en el json y lo guardara
                                                                guardarArchivo(miArchivo)
                                                                print("cambio realizado con exito")#le notificara que su cambio fue realizado
                                                                print("")
                                                    menumodificaciones() 
                                                            
                                                if opc==5:
                                                    miArchivo=abrirArchivo()
                                                    print("======= MODIFICAR ACUDIENTE ========")
                                                    ingid=input("ingrese la id del campers a modificar: ")#se ingresa la id  del camper a modificar
                                                    for i in miArchivo[0]["grupos"]:
                                                        for a in i["grupo"]:
                                                            if a["id"]==ingid:#se compara si la id ingresada si se encuentra
                                                                nuevoAcudiente=input("ingrese el acudiente del camper: ")#si es asi le pedira ingresar el nuevo nombre del acudiente
                                                                a["acudiente"]=nuevoAcudiente#actualizara los datos en el json y lo guardara
                                                                guardarArchivo(miArchivo)
                                                                print("cambio realizado con exito")#le notificara que su cambio fue realizado
                                                                print("")
                                                    menumodificaciones() 
                                                            
                                                if opc==6:
                                                    miArchivo=abrirArchivo()
                                                    print("======= MODIFICAR NUMERO DE TELEFONO========")
                                                    ingid=input("ingrese la id del campers a modificar: ")#se ingresa la id  del camper a modificar
                                                    for i in miArchivo[0]["grupos"]:
                                                        for a in i["grupo"]:
                                                            if a["id"]==ingid:#se compara si la id ingresada si se encuentra
                                                                nuevoNumeroCelular=int(input("ingrese el numero del celular del camper: "))#si es asi le pedira ingresar el nuevo numero de celular
                                                                a["telefono"]["celular"]=nuevoNumeroCelular#actualizara los datos en el json y lo guardara
                                                                guardarArchivo(miArchivo)
                                                                print("cambio realizado con exito")#le notificara que su cambio fue realizado
                                                                print("")
                                                    menumodificaciones() 
                                                        
                                                if opc==7:
                                                    miArchivo=abrirArchivo()
                                                    print("======= MODIFICAR NUMERO FIJO========")
                                                    ingid=input("ingrese la id del campers a modificar: ")#se ingresa la id  del camper a modificar
                                                    for i in miArchivo[0]["grupos"]:
                                                        for a in i["grupo"]:
                                                            if a["id"]==ingid:#se compara si la id ingresada si se encuentra
                                                                nuevoNumeroFijo=int(input("ingrese el numero fijo del camper: "))#si es asi le pedira ingresar el nuevo numero fijo 
                                                                a["telefono"]["fijo"]=nuevoNumeroFijo#actualizara los datos en el json y lo guardara
                                                                guardarArchivo(miArchivo)
                                                                print("cambio realizado con exito")#le notificara que su cambio fue realizado
                                                                print("")
                                                    menumodificaciones() 
                                                if opc==8:#finalizar opciones de actualizaciones
                                                    print("... ")
                                                    nada=False
                                            except ValueError:
                                                print("ingresa una opcion valida")#le pregunta al coordinador si quiere coninuar actualizando 
                                        sino=input("quieres repetir el proceso con otro camper(si)\n"
                                                   "para volver al menu de coordinador presiona enter")
                                        if sino!="si":#si su respuesta es diferente a si finalizara
                                            raw=False
                        menucoordinador()
                    if opc==9:#permite salirse  del menu de coordinador y volver al principal
                        ver=False#rompe el bucle
                        menu()#vuelve a imprimir el menu principal
                except ValueError:
                    print("INGRESA UNA OPCIÓN VALIDA")#esto se imprimira se la condicion anterior no se hace cumplir.

        if opc==2:#abrir menu de  trainer
            miArchivo=abrirArchivo()
            read=True
            while read==True:
                #debe ingresar el usuario para poder entrar al modulo de trainers
                user=input("nombre de usuario (presiona enter si lo que quieres es salir)\n")#ingrese usuario
                if user!="":#si imprime enter saldra
                    contra=input("contraseña\n")#de lo contrario imprimira esto para que ingrese la contraseña
                else:
                    read=False
                for i in miArchivo[0]["trainers"]:
                    if i["user"]==user and i["contraseña"]==contra:#aqui verificara si la contraseña y el user son correctos
                        menutrainer()#si es asi imprimira el menu de trainers
                        tutu=True
                        while tutu==True:
                            try:
                                opctra=int(input("escoge una opción:  "))#le pedira elegir una opcion
                                if opctra==1:#la opcion 1 mostrar el horario del trainer
                                    if len(i["ruta"])==4:
                                        print("---(6am-10am)-----(10am-2pm)-----(2pm-6pm)-----(6pm-10pm)")
                                        print("---(",i["ruta"][0],")-----(",i["ruta"][1],")-----(",i["ruta"][2],")-----(",i["ruta"][3],")")
                                    if len(i["ruta"])==3:
                                        print("---(6am-10am)-----(10am-2pm)-----(2pm-6pm)")
                                        print("---(",i["ruta"][0],")-----(",i["ruta"][1],")-----(",i["ruta"][2],")")
                                    if len(i["ruta"])==2:
                                        print("---(6am-10am)-----(10am-2pm)")
                                        print("---(",i["ruta"][0],")-----(",i["ruta"][1],")")
                                    if len(i["ruta"])==1:
                                        print("---(6am-10am)-----")
                                        print("---(",i["ruta"][0],")-----")
                                    if len(i["ruta"])==0:
                                        print("no tienes ninguna ruta")
                                    menutrainer()#dependiendo de las rutas que tenga el trainer se le mostrara su horario
                                
                                if opctra==2:#la segunda opcion le permitira hacer unas actualizaciones
                                    menumodiftrainer()#muestra el menu de modificaciones del trainers
                                    totoro=True
                                    while totoro==True:
                                        try:
                                            red=int(input("ingrese su opcion: "))#le permite ingresar la opcion que va a modificar
                                            if red==1:
                                                nom=input("ingresa el nuevo nombre:  ")#le pedira lo nuevo y lo guardara en una variables
                                                i["nombre"]=nom#se hara el cambio y se guardara
                                                print("cambio realizado")
                                                guardarArchivo(miArchivo)
                                            if red==2:
                                                ape=input("ingrsa el nuevo apellido:  ")#le pedira lo nuevo y lo guardara en una variables
                                                i["apellido"]=ape#se hara el cambio y se guardara
                                                print("cambio realizado")
                                                guardarArchivo(miArchivo)
                                            if red==3:
                                                fus=True
                                                while fus==True:
                                                    try:
                                                        telefono=int(input("ingresa el nuevo numero de telefono:  "))
                                                        fus=False
                                                    except ValueError:
                                                        print("ingresa un numero valido")#le pedira lo nuevo y lo guardara en una variables
                                                i["telefono"]=telefono#se hara el cambio y se guardara
                                                print("cambio realizado")
                                                guardarArchivo(miArchivo)
                                            if red==4:
                                                use=input("ingresa el nuevo nombre de usuario:  ")#le pedira lo nuevo y lo guardara en una variables
                                                i["user"]=use#se hara el cambio y se guardara
                                                print("cambio realizado")
                                                guardarArchivo(miArchivo)
                                            if red==5:
                                                contraseña=input("ingresa la nueva contraseña:  ")#le pedira lo nuevo y lo guardara en una variables
                                                i["cotraseña"]=contraseña#se hara el cambio y se guardara
                                                print("cambio realizado")
                                                guardarArchivo(miArchivo)
                                            if red==6:
                                                edad=input(" ingrese su nueva edad: ")#le pedira lo nuevo y lo guardara en una variables
                                                i["edad"]=edad#se hara el cambio y se guardara
                                                print("cambio realizado")
                                                guardarArchivo(miArchivo)
                                            if red==7:
                                                totoro=False#finalizar y terminara el bucle
                                            if red<1 or red>7:
                                                print("ingresa una opción valida")#si la opcion es menor a 1 y mayor a 7 le imprimira una notificacion
                                        except ValueError:
                                            print("ingresa una opción valida")
                                    menutrainer()#vuelve a imprimir el modulo del trainer
                                if opctra==3:
                                    tutu=False
                            except ValueError:
                                print("ingresa una opción valida")
            menu()
        elif opc==3:#la opcion 3 es para el modulo de reportes
            print("MODULO DE REPORTES")
            print("")
            menureportes()#se imprime el menu
            mjb=True
            while mjb==True:#se inicia un bucle para que se pueda decidir cuando tarminarlo
                try:
                    opc=int(input("ingrese su opcion porfavor: "))
                    if opc==1:#la opcion 1 ya esta esplicada en el principio de todo el codigo
                        for i in range(len(miArchivo[0]["grupos"])):
                            print("--------")
                            print(miArchivo[0]["grupos"][i]["nombres"])
                            cont=0
                        punch=True
                        while punch==True:
                            cell=0
                            gru=input("que grupo quieres listar\n")
                            for i in miArchivo[0]["grupos"]:
                                if i["nombres"]==gru:
                                    cell=1
                                    punch=False
                            if cell==0:
                                print("escoje un grupo de los que se mostraron (escribelo igual)")
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
                        menureportes()
                    if opc==2:
                        print("")    
                        print("=========CAMPERS QUE APROBARON EL EXAMEN PRINCIPAL =============")   
                        for i in miArchivo[0]["grupos"]:#analiza cada grupo
                            for d in i["grupo"]:
                                if d["estado"]=="cursando":#y si el estado del estudiante es cursando significa que aprobo el examan de ingreso
                                    print("=========================================================")
                                    print("id:  ",d["id"])
                                    print("nombre:  ",d["nombre"])
                                    print("apellido:  ",d["apellido"])#se imprimen los datos de cada estudante
                                    print("estado:  ",d["estado"])
                                    print("=========================================================")
                                    print("")
                        menureportes()
                    if opc==3:
                        print("") 
                        print("::::::::::::::TRAINERS:::::::::::::::") 
                        for i in miArchivo[0]["trainers"]:#va a la ubicacion de cada trainer 
                            print(" ")
                            print("==================================================")
                            print("id: ",i["id"])
                            print("nombre: ", i["nombre"])
                            print("apellido: ", i["apellido"])# y imprime su informacion
                            print("edad: ", i["edad"])
                            print("ruta: ", i["ruta"])
                            print("===================================================")
                        menureportes()  
                    if opc==4:
                        miArchivo=abrirArchivo()
                        for i in miArchivo[0]["grupos"]:#va a la ubicacion de grupos
                            for z in i["grupo"]:#va a la ubicacion de cada camper
                                one=0#el contador comienza valiendo 0
                                if "modulo1" in z["modulos"]:#primero se verifica que el modulo este existente
                                    if z["modulos"]["modulo1"]=="desaprobado":#y si el modulo es desaprobado
                                        one=one+1#se suma uno al contador
                                if "modulo2" in z["modulos"]:
                                    if z["modulos"]["modulo2"]=="desaprobado":#y asi se hace con los otros
                                        one=one+1
                                if "modulo3" in z["modulos"]:
                                    if z["modulos"]["modulo3"]=="desaprobado":
                                        one=one+1
                                if "modulo4" in z["modulos"]:
                                    if z["modulos"]["modulo4"]=="desaprobado":
                                        one=one+1
                                if "modulo5" in z["modulos"]:
                                    if z["modulos"]["modulo5"]=="desaprobado":
                                        one=one+1
                                if one>=3:#si el contador es mayor o igual a 3 significa que el rezgo va a ser alto
                                    z["riesgo"]="alto"
                                else:# y si no el riesgo es bajo
                                    z["riesgo"]="bajo"
                        guardarArchivo(miArchivo)


                        print("") 
                        print("")
                        print("::::::::::::::CAMPERS DE BAJO RENDIMIENTO:::::::::::::::") 
                        print("Todos aquellos campers que cuentan con un riesgo alto equivale a un rendimiento bajo")
                        for i in miArchivo[0]["grupos"]:
                            for a in i["grupo"]:#va a la ubicacion de cada camper 
                        
                                if a["riesgo"]=="alto":#y si el riezgo es alto se imprimen los datos
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
                            if len(i["ruta"])>0:#si la cantidad de rutas es mayor a 3 
                                
                                print(" ")
                                print("==================================================")
                                print("id: ",i["id"])
                                print("nombre: ", i["nombre"])
                                print("apellido: ", i["apellido"])#se imprimen los datos de los trainers
                                print("ruta: ", i["ruta"])
                                print("===================================================")
                                print("")
                        for i in  miArchivo[0]["grupos"]:
                                
                            if len(i["grupo"])>0:#si la cantidad de estudiantes es mayor a 0
                                print(" ")
                                print(":::::CAMPERS CON RUTA:::::::")
                                for a in i["grupo"]:
                                    print("")
                                    print("ruta: ", i["ruta"])#se imprime la ruta
                                    print("==================================================")
                                    print("id: ",a["id"])
                                    print("nombre: ", a["nombre"])
                                    print("apellido: ", a["apellido"])#y los datos de ellos
                                    print("===================================================")
                                    print("")
                        menureportes()

                    if opc==6:
                        miArchivo=abrirArchivo()
                        opcion6=True
                        while opcion6==True:#se inicia bucle
                            for i in miArchivo[0]["grupos"]:
                                print("")
                                print("--------------------------------")
                                print("ruta:  ", i["ruta"])#se imprimen las rutas
                                print("")
                            pregunt=input("que ruta quieres ver")
                            for i in miArchivo[0]["grupos"]:
                                if pregunt==i["ruta"]:
                                    print("--------------------------------")
                                    print("ruta:  ", i["ruta"])#se imprime la ruta se es igual a la que se escogio
                                    print("")
                                    for z in miArchivo[0]["trainers"]:#va a la ubicacion de los trainers 
                                        for f in range(len(z["ruta"])):
                                            if z["ruta"][f]==i["ruta"]:#si la ruta que se escogio es igual a una ruta de algun trainer
                                                print("trainer encargado")
                                                print("")
                                                print("id: ", z["id"])
                                                print("nomdre: ", z["nombre"])#se imprimen los datos del trainer
                                                print("apellido: ", z["apellido"])
                                                print("")
                                    notasmodulos()#se imprime el menu
                                    diez=True
                                    while diez==True:#se inicia bucle
                                        try:
                                            opc6=int(input("que modulo quieres ver\n"))
                                            if opc6==1:
                                                print("campers que aprobaron el modulo")
                                                print("fundamentos de programacion:  ", i["modulos"]["fundamentos de programacion"])#se imprimen los detalles del modulo
                                                print("")
                                                for r in i["grupo"]:#va a la ubicacion donde esta el estudiante
                                                    if "modulo1" in r["modulos"]:#se verifica que haya nota del modulo
                                                        if r["modulos"]["modulo1"]=="aprobado":#si el modulo lo aprobó 
                                                            print("------------------------")
                                                            print("id: ", r["id"])
                                                            print("nomdre: ", r["nombre"])
                                                            print("apellido: ", r["apellido"])#se imprimen los datos de ese estudiante
                                                            print("resultado del modulo: ", r["modulos"]["modulo1"])
                                                            print("------------------------")
                                                            print("")
                                                print("campers que no aprobaron el modulo")
                                                print("fundamentos de programacion:  ", i["modulos"]["fundamentos de programacion"])
                                                print("")
                                                for r in i["grupo"]:
                                                    if "modulo1" in r["modulos"]:
                                                        if r["modulos"]["modulo1"]=="desaprovado":#se hace lo mismo que lo de arriba pero solo se imprimen los que no aprobaron
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
                                                            print("------------------------")#se repite lo mismo pero con el segundo modulo
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
                                                            print("------------------------")#se repite lo mismo pero con el tercer modulo
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
                                                            print("------------------------")#se repite lo mismo pero con el cuarto modulo
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
                                                            print("------------------------")#se repite lo mismo pero con el quinto modulo
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
                                                diez=False#si escoje la opcion 6 se termina el bucle
                                        except ValueError:
                                            print("ingresa una opcion valida")
                            lola=input("quieres volver al menu de reportes (si)(no)\n")
                            if lola=="si":
                                opcion6=False#si acepta se termina el bucle 
                        menureportes()#y se muestra el menu de reportes

                    if opc==7:
                        mjb=False#si escoje la opcion 7 se finaliza la opcion de reportes
                        menu()

                except ValueError:
                    print("INGRESA UNA OPCIÓN VALIDA")
        if opc==4:
            miArchivo=abrirArchivo()
            print("////REGISTRO DE ESTUDIANTES/////")
            x1=True
            while x1==True:
                pedir_nombre=input("Ingresa el nombre del estudiante: ")#Ingresar nombre de estudiante para traer la id 
                for i in miArchivo[0]["grupos"]:
                    for x in i["grupo"]:
                        if pedir_nombre==x["nombre"]:
                            id_registro_camper=x["id"]
                            x1=False
            fecha=datetime.now(timezone.utc)
            fecha_organizada=fecha.strftime("%Y-%m-%d %H:%M:%S")#traer l fecha del momento de ingreso
            actividades=input("Escribe las actividades realizadas\n")
            buclecito=True
            while buclecito==True:
                #ingreso del estado de la sesión
                opc_estado=input("""
                  ----Estado de la sesión----
                  1. Activa
                  2. Inactiva 
                  3. Finalizada
                  escoje una opción: 
                  """)
                if opc_estado=="1":
                    estado="Activa"
                    buclecito=False
                    
                if opc_estado=="2":
                    estado="Inactiva"
                    buclecito=False
                    
                if opc_estado=="3":
                    estado="Finalizada"
                    buclecito=False
            #guardar los registros en el json
            miArchivo[0]["Registro_de_Entrada"].append({"id":id_registro_camper,"fecha_entrada":fecha_organizada,"actividades_realizadas":actividades, "estado":estado})
            guardarArchivo(miArchivo)
            print("Se ha creado con exito el registro!")
            menu()
        if opc==5:
            print("HASTA LA PROXIMA\nPROGRAMA FINALIZADO :)")
            bool=False#se finaliza el programa
    except ValueError:
       print("INGRESA UNA OPCIÓN VALIDA")

#desarrollado por Caicedo Bermon Luis Miguel C.C: 1090381345
#desarrollado por Botello Garcia Yurley T.I: 1066085539