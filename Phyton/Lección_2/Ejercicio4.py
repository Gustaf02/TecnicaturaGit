# Ejercicio Etapas de la vida según la edad
'''
edad = int(input("Digite su edad "))
mensaje = None
if 0 <= edad < 10: #Sintaxis simplificada
    mensaje = "La infancia es increíble y bella"
elif 10 <= edad < 20:
    mensaje = "Tienes muchos cambios, mucho que estudiar"
elif 20 <= edad < 30:
    mensaje = "Amor y comienza el trabajo"
elif 30 <= edad < 100:
    mensaje = "Estás en la plenitud de la vida"
else:
    mensaje = "Error, etapa de vida no reconocida"
print(f"Tu edad es {edad} , {mensaje}") '''



Dueno = [28957346,  'Juan',  'Perez', 4789689,  'Belgrano 101']
DNI = Dueno[0]
if DNI > 26000000:
   print (4789689)

Dueno2 = [23546987, 'Maria', 'Perez', 4789689, 'Pueyrredon 811']
DNI = Dueno2[0]
Apellido = Dueno2[2]
for i in Dueno2:
    if i != DNI and i != Apellido:
        print(i)

Historial = (2350, 5960, 23000, 1000, 8900)
TuplaSum = sum(Historial)
print(TuplaSum)
if TuplaSum < 30000:
    print(TuplaSum)
else:
    print("Gastos por encima de los presupuestado")

Historial2 = (23500, 5960, 2300, 10200, 8900)
TuplaSum = sum(Historial2)
print("Frida ha gastado: ", TuplaSum)

Historial3 = (9530, 4120, 4580, 1500, 890,7516,426)
TuplaSum = sum(Historial3)
Prom = TuplaSum / 7
print ("El promedio es ", Prom)
if Prom > 4500:
    print("Se ha excedido en el gasto promedio para su mascota")

Perro2 = [14,  'Fido',  12/12/2012 , 'Macho', 23546987]
print(Perro2)
Perro2.reverse()
print(Perro2)

Historial4= (7510, 7960, 76180, 800, 4100)
print(min(Historial4))

Historial5 = (8520, 9510, 7530, 3570, 1590)
print(max(Historial5))

Clientes = ["Juan", "Mario", "Ariel", "Josefina", "Marianella"]
Clientes.sort()
print(Clientes)

#Ejercicio 2
Dueno2 = [23546987, 'Maria', 'Perez', 4789689, 'Pueyrredon 811']
DNI = Dueno2[0]
Apellido = Dueno2[2]
for i in Dueno2:
    if i != DNI and i != Apellido:
        print(i)







