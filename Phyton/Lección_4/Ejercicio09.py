# Ejercicio nº9: mostrar una frase sin espacios y mostrar su longitud
# Hacer un programa donde el usuario ingrese una frase
# Se le devolverá la misma frase pero sin espacios en blanco, y además un contador
# de cuántos caracteres tiene esa frase
# (sin contar los espacios en blanco)
# ejemplo: Vivir por siempre en paz
# frase final: Vivirporsiempreenpaz
# número de caracteres:21
frase1 = input('Diga una frase')
frase2 = ' '
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f'frase final {frase1}')
print(f'Número de caracteres: {len(frase1)}')
