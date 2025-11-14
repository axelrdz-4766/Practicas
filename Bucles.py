# En este archivo sera meramente puro ejercicios y practicas sobre los bucles y algunos comentarios sobre ideas,
# pensamientos y cosas que se me ocurran mientras hago los ejercicios.
# Estos ejercicios seran basados en varias partes, actualmente estoy en codedex entocnes tomare ejercicios de ahi pero
# para ir practicando el uso de VSCode y GitHub los hare por aca y los subire al repo.
# Tambien tomare ejercicios de varios lugares y retos que vaya encontrando, siempre dejare un comentario de
# donde lo saque.

# La idea es ir practicando y mejorando mis habilidades de programacion en python desde un nivel basico hasta un
# nivel avanzado.

# Cuando un comentario tenga ### es porque es un comentario original mio no como los que solo tendran uno, que son
# las explicaciones de los retos.


#Codedex - Cuenta atras para año nuevo
#Dentro del bucle, imprime los números del 10 al 1, cada uno en su propia línea.
#Cuando el bucle termine la cuenta atrás, imprime esta cadena exacta Happy New Year! 🥳
for i in range(10, 0, -1):

    if i != 1:
        print(i)
    else:
        print("Happy New Year! 🥳")

#Codedex - Ya llegamos?
#Primero, pregúntele al usuario “¿Ya llegamos?” utilizando la funcion input() y guárdela en una variable
#Luego, crea un bucle que pregunte al usuario "¿Ya llegamos?" de nuevo. Sigue preguntándole esto una y otra vez hasta que responda "Sí".
answer = input("Are we there yet? ").lower() ### asi nos aseguramos que si el usuario la pone con mayuscula si coincida el string

while answer != "yes":
    answer = input("Are we there yet? ").lower()

#Codedex - Sneak Eyes
#Utilizando un bucle, comprueba si totales 2. Si no lo es, imprime la cadena 'Nope' y sigue "volviendo a tirar" los dados.
import random

total = 0

while total != 2:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    if total != 2:
        print('Nope')
    else:
        print('Snake eyes!')

#Codedex - Asterisks
#Crea una escalera de asteriscos comenzando con un solo asterisco en la primera línea y terminar con un total de 24 asteriscos en la última línea
for i in range(1, 25):
  print('* ' * i)

#ChatGPT (modo estudio) - Contador selectivo
#Crea un for que recorra los numeros del 10 al 40 y que solo imprima los numeros pares.
#Si el numero termina en 6, NO lo imprimas, si el numero es 32, deten todo el ciclo inmediatamente.
for i in range(10, 40):

    if i == 32:
        print('Se acaba el codigo porque no queremos el 32 y ya me enoje no quiero nada mas')
        break
    elif i % 10 == 6:
        continue
    elif i % 2 == 0:
        print(i)

