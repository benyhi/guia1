segundos = input('Ingresa un tiempo expresado en segundos: ')
segundos = int(segundos)

dias = int(segundos / 86400)
segundos = int(segundos % 86400)
horas = int(segundos / 3600)
segundos = int(segundos % 3600)
minutos = int(segundos / 60)
segundos = int(segundos %60)

print ('Tu tiempo equivale a: ', dias , ':dias', horas, ':horas', minutos, ':minutos', segundos,':segundos')