import json
def error(msg):
    print("\r!!!!!! Error: ",msg.upper())
    input("\t Digite cualquier tecla para continuar")

def leer_string(msg):
    while True: # numero de horas 
        try:
            string_agregar= input(msg)
            if  string_agregar.isalpha():
                return string_agregar
            error("Valor invalido")
            continue
        except ValueError:
            error("Valor invalido")
            continue
def leer_numero(msg):
    while True: # numero
        try:
            numero_agregar=int(input(msg))
            if numero_agregar>0:
                return numero_agregar
                
            error("Valor negativo")
            continue
                    
        except ValueError:
            error("Valor invalido")
            continue
def leer_numerof(msg):
    while True: # numero
        try:
            numero_agregar=int(input(msg))
            if numero_agregar>0:
                return numero_agregar
                
            error("Valor negativo")
            continue
                    
        except ValueError:
            error("Valor invalido")
            continue
def leer_documento(msg):
    while True: # id
        try:
            id_agregar=int(input(msg))
            if id_agregar>0:
                return id_agregar
                
            error("Valor negativo")
            continue
                    
        except ValueError:
            error("Valor invalido")
            continue

def leer_nota(msg):
    while True: # numero de horas 
        try:
            nota_agregar= float(input(msg))
            if  nota_agregar>0 and nota_agregar<= 5:
                return nota_agregar
            error("Valor invalido")
            continue
        except ValueError:
            error("valor invalido")
            continue
def validar_otro_ciclo(msg):
    while True:
        try:
            y=input(msg)
            if y.lower() == "si":
                return True
            if y.lower() == "no":
                return False
            print("!@ valor invalido")
        except ValueError:
            print("!@ valor invalido")
            continue
def menu():
    while True:
        try:
            print("="*30)
            print("\tMENU")
            print("\t1- Mostrar en pantalla todas las mascotas\n\t2- Crear nueva mascota con multiples servicios\n\t3- Mostrar los datos de mascotas por tipo elegido(raza,precio y servicios)\n\t4- Actualizar los datos de una mascota consultada por indice\n\t5- Eliminar una mascota de la tienda por indice\n\t6- Salir")
            print("="*30)
            op=int(input("\t>> escoja una opción (1-6)"))
            
            if op <1 or op >8:
                error("!@ Valor invalido")
                continue
            return op
        except ValueError:
            error("!@ Valor invalido")
            continue
def services():
    lista=[]
    while True:
        try:
            servicio=input("\tDigite un servicio: ")
            if servicio.isalpha() and servicio not in lista:
                lista.append(servicio)
                if validar_otro_ciclo("\t@Desea ingresar otro servicio ? (si|no) "):
                    continue
                return lista
            error("valor invalido o repetido")
        except ValueError:
            error("valor invalido.")
            continue

def leer_sexo(msg):
    while True:
        try:
            lista=["m","f","masculino","femenino","M","F","MASCULINO","FEMENINO"]
            sexo=leer_nombre(msg)
            if sexo in lista:
                return sexo
            error("Sexo no valido, solo se permite")
            [print(elemento,end=",") for elemento in lista]
            continue
        except:
            error("valor invalido")
def ingresar_datos():
    # nombre, sexo y grado
    estudiantes=leer_json()    
    while True:  
        nom=len(estudiantes)+1
        print(" "*15,f"\n\tDigite para la mascota #{nom}\n"," "*15)

        id=str(leer_numero(f"\tDigite el Id del estudiante "))
        if id in estudiantes.keys():
            error("La id ingresada ya existe, ingrese otra por favor")
            continue
        nombre=leer_string(f"\tDigite el nombre ")
        sexo=leer_sexo(f"\tDigite el sexo: (ingrese la primera letra o la palabra completa)")
        grado=leer_numero(f"\tdigite el grado: ")
        #servicios=services()
        #definitiva= (nota1+nota2+nota3)/3
        estudiantes[id]={
            "nombre":nombre,
            "sexo":sexo,
            "grado":grado
        }


        if validar_otro_ciclo("\t@¿Quiere seguir agregando mascotas? (si|no) "):
            continue
        subir_json(estudiantes)

        break
def validar_entero_string(key,value):
    if type(value) is int:
        print(f"\t{key} --->${value:,.0f}")
    
    else:
        print(f"\t{key} --->{value}")
def mostrar(dic_persona,i):
    print(" "*15,f"\n  Mascota {i+1} \n"," "*15)
    [[print(f"\tservicio {i+1} ---> {value[i]}") for i in range(len(value))] if type(value) is list else validar_entero_string(key,value) for key,value in dic_persona.items()]
    #[ ( [print(f"nota {i+1} ---> {value[i]}") for i in range(len(value))] if type(value) is list else print(key," ---> ",value)) for key,value in dic_persona.items() ]

def buscar_tipo():
    mascotas=leer_json()
    print(" "*15,f"\n Mostrar por tipo \n"," "*15)
    while True:
        codigo = leer_nombre("\tDigite el tipo de mascota que quiere buscar: ")
        if True in [True for x in range(len(mascotas["pets"])) if mascotas["pets"][x]["tipo"]==codigo]:
            [mostrar(mascotas["pets"][i],i) for i in range(len(mascotas["pets"])) if mascotas["pets"][i]["tipo"]==codigo]
            if validar_otro_ciclo("\t¿Desea buscar otro tipo? (si|no)"):
                continue
            break
        error("Codigo repetido")
        continue

def leer_talla(msg):
    lista=["pequeño","pequeña","mediano","mediana","grande"]
    while True:
        talla=leer_nombre(msg)
        if talla in lista:
            return talla
        error("talla incorrecta")
        continue
def Actualizar(funcion):
    if funcion== "modificar_datos":
        lista=["nombre","sexo","grado","todos"]
        [print(f"\n\t{i+1}- {elemento}") for i,elemento in enumerate(lista)]
        op=leer_id("Ingrese el indice que desa modificar modificar")


    tipo=leer_nombre(f"\tDigite el tipo: ")
    raza=leer_nombre(f"\tDigite la raza: ")
    talla=leer_talla(f"\tDigite la talla: ")
    precio=leer_documento(f"\tDigite el precio: ")
    servicios=services()

    datos={
            "tipo":tipo,
            "raza":raza,
            "talla":talla,
            "precio":precio,
            "servicios":servicios
            
        }
    
    return datos
    
def modificar_datos():
    estudiantes=leer_json()
    while True:
        mostrar_todos()
        id=leer_numero("Digite el numero de la mascota que quiere actualizar: ")-1
        if id not in estudiantes:
            error("Estudiante inexistente")
            continue

        datos_agregar=Actualizar()
        estudiantes["pets"][codigo]=datos_agregar
        
        
        if validar_otro_ciclo("\t@Desea modificar otra mascota? (si|no) "):
            continue
        subir_json(estudiantes)
        break
        
def borrar_datos():
    mascotas=leer_json()
    while True:
        mostrar_todos()
        codigo=leer_id("\tDigite el numero de la mascota que quiere borrar ")-1
        if codigo < 0 or codigo >len(mascotas["pets"]):
            error("Mascota inexistente")
            continue

        #datos_agregar=Actualizar()
        
        mascotas["pets"].pop(codigo)
        print("se ha borrado")
        
        
        if validar_otro_ciclo("\t@Desea eliminar otra mascota? (si|no)"):
            continue
        subir_json(mascotas)
        break
        
            
def mostrar_todos():
    estudiantes=leer_json()
    [mostrar(i,key,diccionarios) for i,(key,diccionarios) in enumerate(estudiantes.items())]
    #[mostrar(estudiantes["pets"][i],i) for i in range(len(estudiantes["pets"]))]
def leer_json():
    with open("estudiantes.json","r") as file:
        data=json.load(file)
    return data
def subir_json(data):
    with open("estudiantes.json","w") as file:
        json.dump(data,file,indent=4)
    
def inicializar_json():
    with open("estudiantes.json","w") as file:
        mascotas={}
        
        json.dump(mascotas,file,indent=4)
def main():
    inicializar_json()
    while True:
        op=menu()
        if op ==1:
            ingresar_datos()
            #mostrar_todos()## mostrar 
        elif op==2:
            modificar_datos()
            #ingresar_datos()
        elif op==3:
            buscar_tipo()
        elif op==4:
            modificar_datos()
        elif op==5:
            borrar_datos()
        elif op==6:
            print("hasta luego")
            break
        
        
main()  

{
    "userId": 1,
    "id": 1,
    "title": "delectus aut autem",
    "completed": false
}
# Map of userId to number of complete TODOs for that user
todos_by_user = {}

# Increment complete TODOs count for each user.
for todo in todos:
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1

# Create a sorted list of (userId, num_complete) pairs.
top_users = sorted(todos_by_user.items(), 
                   key=lambda x: x[1], reverse=True)

# Get the maximum number of complete TODOs.
max_complete = top_users[0][1]

# Create a list of all users who have completed
# the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)