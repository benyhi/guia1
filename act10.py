nombre = input('Ingresa tu nombre: ')
carrera = input('Ingresa la carrera que deseas cursar: ')
ciudad = input('Ingresa la ciudad en la que residis: ')
por = 15
cuota = 7000

if carrera == 'electromecanica' and ciudad != 'rio cuarto': 
    descuento = cuota%por 
    print(nombre)
    print(ciudad)
    print(carrera)
    print('El monto final de tu cuota es de: ', cuota - descuento)

else: 
    print(nombre)
    print(ciudad)
    print(carrera) 

