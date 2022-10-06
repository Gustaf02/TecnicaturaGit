# Ejercicio Nº10: Mostrar una frase sin espacios y contar su longitud. Hacer un programa donde se ingrese
# una frase y devuelva esa frase. Se le devolverá la misma frase, pero sin espacios en blanco. Además un
# contador de cuántos caracteres tiene la frase (sin contar los espacios en blanco).
# Ejemplo: frase = vivir por siempre en paz
# frase final = vivirporsiempreenpaz     Nº de caracteres: 21
frase1 = input('Digite una frase ')
frase2 = " "
for i in frase1:
    if i != ' ':
        frase2 += i
frase1 = frase2
print(f'La frase final es {frase1}')
print(f'El número de caracteres es {len(frase1)}')