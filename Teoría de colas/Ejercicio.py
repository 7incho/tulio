import datetime as dt

ps = 0
q = 0
horaActual = dt.timedelta(hours=8)
deltaLLegadas = 45
deltaFS = 40
horaProximoFinServicio = 0 

def VectorInicial():
    return

def LlegadaCliente():
    global ps, q, horaActual, horaProximaLlegada, deltaLLegadas
   
    if ps==0:
        ps=1
    else:
        q+=1
    #generar horario de proxima llegada
    horaProximaLlegada = horaActual + dt.timedelta(seconds=deltaLLegadas)
         
    print('ps: ',ps, ' q:',q, 'Hora Actual: ', horaActual, 'Proxima llegada: ', horaProximaLlegada)
   

def FinServicio():
    global ps, q, deltaFS, horaActual, horaProximoFinServicio, deltaFS
    if q>0:
        ps=1    #esta linea es opcional (por que si es un fin de servicio entonces ps==1)
        q=q-1
        #calcular proximo fin de servicio
        horaProximoFinServicio = horaActual + dt.timedelta(seconds=deltaFS)
    else:  
        ps=0
    print('ps: ', ps, ' q:', q, 'Hora Actual: ', horaActual, 'Proxima llegada: ', horaProximaLlegada, 'Hora prox. fin servicio: ', horaProximoFinServicio)
    return