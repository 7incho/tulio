import datetime

fecha_inicial = datetime.datetime(2023, 6, 1, 12, 30, 0)  # Fecha y hora inicial
duracion = datetime.timedelta(days=1, hours=3)  # Duración de 1 día y 3 horas

fecha_final = fecha_inicial + duracion  # Sumar el timedelta a la fecha inicial

print(fecha_final)  # Imprimir la fecha y hora final

timestamp = fecha_final.timestamp()
print (timestamp)
hora = datetime.datetime.fromtimestamp(timestamp)
print (hora)
