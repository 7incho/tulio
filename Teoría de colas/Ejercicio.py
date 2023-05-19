import random

Q, PS, T, P, SigLlegada, SigFinServicio, SigLlegadaS, SigSalidaS, tci, tcf, tai, taf, caso, S, tdi, tdf, tti, ttf = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

def VectorInicial():
    global Q, PS, T, P, SigLlegada, SigFinServicio, SigLlegadaS, SigSalidaS, tci, tcf, tai, taf, caso, S, tdi, tdf, tti, ttf

    Q = int(input("Ingrese la cantidad inicial de clientes en cola: "))
    PS = int(input("Ingrese el estado inicial del puesto de trabajo (ocupado = 1; libre = 0): "))
    T = int(input("Ingrese la duración de la simulación (en minutos): "))
    P = 0
    SigLlegada = 0
    SigFinServicio = 0
    SigLlegadaS = 0
    SigSalidaS = 0
    
    print("Ingrese el intervalo en el que llegan los clientes: ") 
    tci = int(input("Mínimo: "))
    tcf = int(input("Máximo: "))
    
    print("Ingrese el intervalo que tarda el puesto de servicio en atender los clientes: ")
    tai = int(input("Mínimo: "))
    taf = int(input("Máximo: "))
    
    caso = int(input("¿El servidor puede abandonar el puesto de trabajo? (Si = 1; No = 0): "))
    
    if caso == 1:
        S = int(input("Ingrese el valor inicial del servidor del puesto de trabajo (presente = 1; ausente = 0): "))
        print("Ingrese el intervalo de duración de los descansos: ")
        tdi = int(input("Mínimo: "))
        tdf = int(input("Máximo: "))
        print("Ingrese el intervalo de tiempo en el que trabaja el servidor: ")
        tti = int(input("Mínimo: "))
        ttf = int(input("Máximo: "))

def LlegadaCliente():
    global Q, PS, P, SigFinServicio

    a = random.randint(tci, tcf)
    if PS == 0:
        PS = 1
        SigFinServicio = P + a
    else:
        Q = Q + 1

def FinServicio():
    global Q, PS

    a = random.randint(tai, taf)
    if Q >= 1:
        Q = Q - 1
        SigFinServicio = P + a
    else:
        PS = 0

def SalidaServidor():
    global S, SigLlegadaS, SigFinServicio

    a = random.randint(tdi, tdf)
    S = 0
    SigLlegadaS = P + a
    if PS == 1:
        SigFinServicio = SigFinServicio + a

def LlegadaServidor():
    global S, SigSalidaS

    a = random.randint(tti, ttf)
    S = 1
    SigSalidaS = P + a

def ImprimirVector():
    print("Clientes en cola:", Q)
    print("Puesto de servicio:", PS)
    print("Duración de la simulación:", T)
    print("Tiempo actual:", P)
    print("Intervalo de atención:", tai, "-", taf)
    print("Intervalo de llegada:", tci, "-", tcf)
    print("Abandona el servidor?:", caso)
    print("Intervalo de trabajo:", tti, "-", ttf)
    print("Intervalo de descanso:", tdi, "-", tdf)
    
def ImprimirEventos():
    print("Siguiente llegada de cliente:", SigLlegada)
    print("Siguiente fin de servicio:", SigFinServicio)
    print("Siguiente salida del servidor:", SigSalidaS)
    print("Siguiente llegada del servidor:", SigLlegadaS)

# Llamadas a las funciones

VectorInicial()
ImprimirVector()
# LlegadaCliente()
# FinServicio()
# SalidaServidor()
# LlegadaServidor()
# ImprimirEventos()
