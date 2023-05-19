#from datetime import timedelta, datetime, tzinfo, timezone, time
import datetime as dt

def fib(n):
    a,b = 0,1
    while a<n:
        print(a, end=' - ')



        a,b = b, a+b

#fib(1000)
    
#Suponiendo que S=cte 1
ps = 0
q = 0
horaActual = dt.timedelta(hours=8)
deltaLLegadas = 45
deltaFS = 40
horaProximoFinServicio = 0 

def llegadas():
    global ps, q, horaActual, horaProximaLlegada, deltaLLegadas
   
    if ps==0:
        ps=1
    else:
        q+=1
    #generar horario de proxima llegada
    horaProximaLlegada = horaActual + dt.timedelta(seconds=deltaLLegadas)
    
        
    print('ps: ',ps, ' q:',q, 'Hora Actual: ', horaActual, 'Proxima llegada: ', horaProximaLlegada)
    


#termina de atender a un cliente
def finservicio():
  global ps, q, deltaFS, horaActual, horaProximoFinServicio, deltaFS
  if q>0:
    ps=1    #esta linea es opcional (por que si es un fin de servicio entonces ps==1)
    q=q-1
    #calcular proximo fin de servicio
    horaProximoFinServicio = horaActual + dt.timedelta(seconds=deltaFS)
  else:  
    ps=0
  print('ps: ', ps, ' q:', q, 'Hora Actual: ', horaActual, 'Proxima llegada: ', horaProximaLlegada, 'Hora prox. fin servicio: ', horaProximoFinServicio)
  

llegadas()
llegadas()
finservicio()
