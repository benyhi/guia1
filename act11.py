#El costo del pasaje a Córdoba es de $2000. La empresa realiza un
#descuento de un 40 % sobre el costo del boleto a los niños que tienen
#entre 5 y 10 años y a los jubilados (mayores de 65). Pedir nombre y edad
#y mostrar el nombre y el valor final del pasaje.

pasaje = 2000
des = 40
total = (pasaje/100)*40
nombre = input('Ingresa tu nombre: ')
edad = int(input('Ingresa tu edad: '))

if 5 <= edad <= 10: 
    print(nombre)
    print('El valor del pasaje es de: ', total)

elif edad > 65: 
    print(nombre)
    print('El valor del pasaje es de: ', total)


