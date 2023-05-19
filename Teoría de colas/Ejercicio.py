import random
global Q, PS, T, P, SigLlegada, SigFinSevicio, SigLlegadaS, SigSalidaS, tci, tcf, tai, taf, caso, S, tdi, tdf, tti, ttf

def VectorInicial():
    Q = input("Ingrese la cantidad inicial de clientes en cola: ")
    PS = input("Ingrese el estado inicial del puesto de trabajo (ocupado = 1; libre = 0): ")
    T = input("Ingrese la duración de la simulación (en minutos): ")
    P = 0
    SigLlegada = 0
    SigFinServicio = 0
    SigLlegadaS = 0
    SigSalidaS = 0
    
    print("Ingrese el intervalo en el que llegan los clientes: ") 
    tci = input("Mínimo: ")
    tcf = input("Máximo: ")
    
    print("Ingrese el intervalo que tarda el puesto de servicio en atender los clientes: ")
    tai = input("Mínimo: ")
    taf = input("Máximo: ")
    
    caso = input("¿El sevidor puede abandonar el puesto de trabajo? (Si = 1; No = 0)" )
    
    if caso == 1:
        S = input("Ingrese el valor inicial del servidor del puesto de trabajo (presente = 1; ausente = 0): ")
        print("Ingrese el intervalo de duración de los descansos: ")
        tdi = input("Mínimo: ")
        tdf = input("Máximo: ")
        print("Ingrese el intervalo de tiempo en el que trabaja el servidor: ")
        tti =input("Mínimo: ")
        ttf= input("Máximo: ")
    return

def LlegadaCliente():
    a = random.randint(tci, tcf)
    if PS == 0:
        PS==1
        SigFinServicio = P + a
    else:
        Q=Q+1
    return

def FinServicio():
    a = random.randint(tai, taf)
    if Q >= 1:
        Q=Q-1
        SigFinServicio = P + a
    else:
        PS=0
    return

def SalidaServidor():
    a = random.randint(tdi, tdf)
    S = 0
    SigLlegadaS = P + a
    if PS == 1:
        SigFinServicio = SigFinServicio + a
    return

def LlegadaServidor():
    a = random.randint(tti, ttf)
    S = 1
    SigSalidaServidor = P + a
    return

def ImprimirVector():
    print("Clientes en cola: {Q}")
    print("Puesto de servicio: {PS}")
    print("Duración de la simulación {T}")
    print("Tiempo actual: {P}")
    print("Clientes en cola: {Q}")
    print("Clientes en cola: {Q}")
    print("Intervalo de atención: {tai}, {taf}")
    print("Intervalo de llegada: {tci}, {tcf}")
    print("Abandona el servidor?: {caso}")
    print("Intervalo de trabajo: {tti}, {ttf}")
    print("Intervalo de descanso: {tdi}, {tdf}")
    
def ImprimirEventos():
    print("Siguiente llegada de cliente: {SigLlegada}")
    print("Siguiente Fin de servicio: {SigFinServicio}")
    print("Siguiente salida del servidor: {SigSalidaS}")
    print("Siguiente llegada del servidor: {SigLlegadaS}")

VectorInicial()
ImprimirVector