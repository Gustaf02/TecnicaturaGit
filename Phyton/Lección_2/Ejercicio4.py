# Ejercicio Etapas de la vida según la edad
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
print(f"Tu edad es {edad} , {mensaje}")
