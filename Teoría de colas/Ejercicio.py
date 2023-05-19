import random
import datetime as dt


Q= P=PS =T= tci= tcf= tai= taf= caso = S=tdi= tdf= tti= ttf= header = 0

SigFinServicio = dt.timedelta
SigLlegada = dt.timedelta
SigLlegadaS = dt.timedelta
SigSalidaS= dt.timedelta
HF=dt.timedelta
HA=dt.timedelta

def VectorInicial():
    global Q, PS, T, P, tci, tcf, tai, taf, caso, S, tdi, tdf, tti, ttf, header, SigFinServicio, SigLlegada, SigLlegadaS, SigSalidaS, HF, HA

    P=int(input("Ingrese hora de inicio de la simulación: "))
    HA= dt.timedelta(hours=int(P))
    Q = int(input("Ingrese la cantidad inicial de clientes en cola: "))
    PS = int(input("Ingrese el estado inicial del puesto de trabajo (ocupado = 1; libre = 0): "))
    T = int(input("Ingrese la duración de la simulación (en minutos): "))
    HF=HA +dt.timedelta(minutes=int(T))
    SigFinServicio = HF
    SigLlegada = HF
    SigLlegadaS = HF
    SigSalidaS = HF
    
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
        header = ["Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "H.Prox Salida servidor", "H.Prox Llegada servidor", "Q", "PS", "S"]
    else:
        S = 1
        header = ["Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "Q", "PS"]

def LlegadaCliente():
    a=random.randint(tai, taf)
    b=random.randint(tci, tcf)
    global Q, PS, HA, SigFinServicio, SigLlegada
    if PS == 0 and S == 1:
        PS = 1
        SigFinServicio = HA + dt.timedelta(minutes=a)
        #print(SigFinServicio)
    else:
        Q = Q + 1
    SigLlegada = HA + dt.timedelta(minutes=b)
    #print(SigLlegada)

def FinServicio():
    a=random.randint(tai, taf)
    global Q, PS, SigFinServicio
    if Q >= 1:
        Q = Q - 1
        SigFinServicio = HA + dt.timedelta(minutes=a)
        #print(SigFinServicio)
    else:
        PS = 0
        SigFinServicio = HF
        

def SalidaServidor():
    global S, SigLlegadaS, SigFinServicio, SigSalidaS
    a = random.randint(tdi, tdf)
    S = 0
    SigLlegadaS = HA + dt.timedelta(minutes=a)
    if PS == 1:
        SigFinServicio = SigFinServicio + dt.timedelta(minutes=a)
    if SigFinServicio == SigSalidaS:
        FinServicio()
    SigSalidaS = HF

def LlegadaServidor():
    a=random.randint(tti, ttf)
    global S, SigSalidaS, SigLlegadaS
    S = 1
    SigSalidaS = HA + dt.timedelta(minutes=a)
    SigLlegadaS = HF
    
def Simulacion():
    global HA, PS, T, Q, SigFinServicio, SigLlegada
    print("-------------- Inicio de Simulación --------------")
    print(header)
    LlegadaCliente()
    if caso == 0:
        while True:
            HA = min(SigFinServicio, SigLlegada)
            if min(SigFinServicio, SigLlegada) == SigFinServicio:
                FinServicio()
            elif min(SigFinServicio, SigLlegada) == SigLlegada:
                LlegadaCliente()
            elif SigFinServicio == SigLlegada:
                print ("Error")
                break
            #tabla = [P, SigLlegada, SigFinServicio, Q, PS]
            print(HA,"        ", SigLlegada, "                 ", SigFinServicio, "              ", Q,"  ", PS) 
            if HA >= HF:
                print("-------------- Fin de la simulación -------------- ") 
                break
    elif caso == 1:
        LlegadaServidor()
        while True:
            HA = min(SigFinServicio, SigLlegada, SigLlegadaS, SigSalidaS)
            if min(SigFinServicio, SigLlegada, SigLlegadaS, SigSalidaS) == SigFinServicio:
                FinServicio()
            elif min(SigFinServicio, SigLlegada, SigLlegadaS, SigSalidaS) == SigLlegada:
                LlegadaCliente()
            elif min(SigFinServicio, SigLlegada, SigLlegadaS, SigSalidaS) == SigLlegadaS:
                LlegadaServidor()
            elif min(SigFinServicio, SigLlegada, SigLlegadaS, SigSalidaS) == SigSalidaS:
                SalidaServidor()
            elif SigFinServicio == SigLlegada == SigLlegadaS == SigSalidaS:
                print ("Error")
                break
            #tabla = [P, SigLlegada, SigFinServicio, SigSalidaS, SigLlegadaS, Q, PS, S]
            print(HA,"        ", SigLlegada, "                 ", SigFinServicio, "              ", SigSalidaS, "                ", SigLlegadaS, "                   ", Q,"  ", PS, "  ", S) 
            if HA >= HF:
                print("-------------- Fin de la simulación -------------- ") 
                break
    return

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

Simulacion()

# ImprimirVector()
#LlegadaCliente()
#FinServicio()
# SalidaServidor()
# LlegadaServidor()
# ImprimirEventos()