print('Hello, Django girls!')
lista=['Jeyn','Gaby']
print (lista)
num1=3
num2=5
if num1>num2:
    num3=num1*num2 
    print (num3)
else:
    print(f'{num1} es menor {num2}')

color1= "azul"
if color1== "amarillo":
    print("parte bandera ecuador")
elif color1 == "rojo":
    print("parte 3 de la bandera")
elif color1 == "azul":
    print ("parte 2 de la bandera")
else:
    print ("no pertenece a la bandera del Ecuador");
#uso del or con if
if color1 =="amarillo" or color1 =="rojo" or color1 =="azul":
        print("Es parte de la bandera")
else: 
   print ("no pertenece a la bandera del Ecuador");

def saludo (nombre):
    print ("Bienvenido" + nombre)

saludo ("Jeyn");

def operaciones (pnum1, pnum2, pnum3):
    num4 = pnum1 + pnum2
    num5 = num4 * pnum3
    print (num5)
    
operaciones (13,7,21)

def datosp(nombre, edad, ciudad):
    print (f"Me llamo {nombre} tengo {edad} y vivo en {ciudad}")

datosp ("Jeynneth",25,"Quito")

def saludo2 (listanombres):
    for nombres in listanombres:
        print (f"Hola {nombres} es un gusto conocerte")

saludo2 (["Jeyn","Gaby","Dani","Vero"])



