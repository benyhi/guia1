# Calcular el sueldo a cobrar teniendo en cuenta que los empleados que
#no han faltado y cuya antigüedad es superior a 5 años, tienen un
#adicional del 30% sobre el sueldo básico ($47.000). Pedir la cantidad de
#días no trabajados y año de ingreso en la empresa.

sueldo = 47000
ad = 30 
plus = 47000 + 14100 
año = int(2023)
dias_no = input('Cuantos dias no trabajaste en el año: ')
antiguedad = int(input('En que año ingresaste a la empresa: '))
año_empresa = año - antiguedad

if dias_no == 0 and año_empresa > 5: 
    print('Tu cobro es de: ', plus)

else:
    print('Tu sueldo es de: ', sueldo)