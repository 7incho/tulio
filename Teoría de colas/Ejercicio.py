import random
import datetime as dt

Q=PS=T=HF=tci=tcf=tai=taf=caso=S=tdi=tdf=tti=ttf = 0
P = dt.timedelta(hours=8)
SigFinServicio = dt.timedelta
SigLlegada = dt.timedelta
SigLlegadaS = dt.timedelta
SigSalidaS= dt.timedelta


def VectorInicial():
    global Q, PS, T, P, S, HF, tci, tcf, tai, taf, tdi, tdf, tti, ttf

    Q = int(input("Ingrese la cantidad inicial de clientes en cola: "))
    PS = int(input("Ingrese el estado inicial del puesto de trabajo (ocupado = 1; libre = 0): "))
    T = int(input("Ingrese la duración de la simulación (en minutos): "))
    
    HF=P+dt.timedelta(minutes=T)
 
    
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
        SigFinServicio = P + dt.timedelta(minutes=a)
        print(SigFinServicio)
    else:
        Q = Q + 1
    SigLlegada = SigLlegada + random.randint(tci, tcf)#revisar si el rango es el mismo q arriba

def FinServicio():
    global Q, PS, SigFinServicio

    a = random.randint(tai, taf)
    if Q >= 1:
        Q = Q - 1
        SigFinServicio = P + dt.timedelta(minutes=a)
        print(SigFinServicio)
    else:
        PS = 0

def SalidaServidor():
    global S, SigLlegadaS, SigFinServicio

    a = random.randint(tdi, tdf)
    S = 0
    SigLlegadaS = P + a
    if PS == 1:
        SigFinServicio = SigFinServicio + dt.timedelta(minutes=a)

def LlegadaServidor():
    global S, SigSalidaS

    a = random.randint(tti, ttf)
    S = 1
    SigSalidaS = P + dt.timedelta(minutes=a)

def ImprimirVector():
    print("Q:", Q, "PS:", PS, "Hora actual:", P, "Próxima Llegada Cliente: ", SigLlegada , "Próximo fin Servicio: ",SigFinServicio)
 
# CUERPO PRINCIPAL
print("---DEFINICIÓN DEL VECTOR INCIAL---")
VectorInicial()
LlegadaCliente()
ImprimirVector()
# LlegadaCliente()
# FinServicio()
# SalidaServidor()
# LlegadaServidor()
# ImprimirEventos()