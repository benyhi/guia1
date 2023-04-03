num1 = input('Ingresa un numero: ')
num2 = input('Ingresa otro numero: ')

num1 = int(num1)
num2 = int(num2)

operacion = input('Si desea sumar los numeros ingresa + (suma) y si desea restarlos ingresa - (resta): ')

if operacion == '+':
    print('Este es tu resultado: ', num1+num2)

else:
    print('Este es tu resultado: ', num1-num2)