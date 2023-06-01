from datetime import datetime
from datetime import timedelta

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.timedelta()

# Obtener el timestamp
timestamp = fecha_hora_actual.timestamp()

print("Fecha y hora actual:", fecha_hora_actual)
print(type(fecha_hora_actual))
print("Timestamp:", timestamp)
print(type(timestamp))

hora_reconvertida = datetime.fromtimestamp(timestamp)

print("Hora reconvertida:", hora_reconvertida)
print(type(hora_reconvertida))