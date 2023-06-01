import random
import datetime as dt

Q= P=PS =T= tci= tcf= tai= taf= casoServidor= casoCliente= S= tdi= tdf= tti= ttf= header= aux= tAbandonoi= tAbandonof= 0

SigFinServicio = dt.timedelta
SigLlegada = dt.timedelta
SigLlegadaS = dt.timedelta
SigSalidaS = dt.timedelta
HF = dt.timedelta
HA = dt.timedelta

#guarda ta ak no anda, 1er aviso
vAbandono = [float(0)]

def VectorInicial():
    global Q, PS, T, P, tci, tcf, tai, taf, casoServidor, casoCliente, S, tdi, tdf, tti, ttf, header, SigFinServicio, SigLlegada, SigLlegadaS, SigSalidaS, HF, HA, tAbandonoi, tAbandonof

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
    
    casoServidor = int(input("¿El servidor puede abandonar el puesto de trabajo? (Si = 1; No = 0): "))
    
    if casoServidor == 1:
        S = int(input("Ingrese el valor inicial del servidor del puesto de trabajo (presente = 1; ausente = 0): "))
        print("Ingrese el intervalo de duración de los descansos: ")
        tdi = int(input("Mínimo: "))
        tdf = int(input("Máximo: "))
        print("Ingrese el intervalo de tiempo en el que trabaja el servidor: ")
        tti = int(input("Mínimo: "))
        ttf = int(input("Máximo: "))
    else:
        S = 1
        
    casoCliente = int(input("¿El cliente puede abandonar la cola de espera? (Si = 1; No = 0): "))
    
    if casoCliente == 1:
        print("Ingrese el intervalo de los abandonos: ")
        tAbandonoi = int(input("Mínimo: "))
        tAbandonof = int(input("Máximo: "))
    
    #Definimos el header para cada caso
    if casoCliente == 1 and casoServidor == 1:
        header = ["Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "H.Prox Salida servidor", "H.Prox Llegada servidor", "H. Prox Abandono", "Q", "PS", "S"]
    elif casoCliente == 1 and casoServidor == 0:
        header = ["Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "H. Prox Abandono", "Q", "PS", "S"]
    elif casoCliente == 0 and casoServidor == 1:
        header = ["Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "H.Prox Salida servidor", "H.Prox Llegada servidor", "Q", "PS", "S"]
    elif casoCliente == 0 and casoServidor == 0:
        header = ["Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "Q", "PS", "S"]
        
def LlegadaCliente():
    a=random.randint(tai, taf)
    b=random.randint(tci, tcf)
    
    global Q, PS, HA, SigFinServicio, SigLlegada, casoCliente, vAbandono, aux
    if PS == 0 and S == 1:
        PS = 1
        SigFinServicio = HA + dt.timedelta(minutes=a)
        #print(SigFinServicio)
    else:
        Q = Q + 1
        if casoCliente == 1:
            c=random.randint(tAbandonoi, tAbandonof)
            aux = HA + dt.timedelta(minutes=c)
            vAbandono.append(dt.timestamp(aux))
    SigLlegada = HA + dt.timedelta(minutes=b)
    
    #print(SigLlegada)

def FinServicio():
    a=random.randint(tai, taf)
    global Q, PS, SigFinServicio
    if Q >= 1:
        Q = Q - 1
        if casoCliente == 1:
            del vAbandono[0]
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
    
def AbandonoCliente():
    global Q
    Q = Q-1
    print("Chupala no espero más")
    
def Simulacion():
    global HA, PS, T, Q, SigFinServicio, SigLlegada, vAbandono
    
    print (vAbandono[0])
    del vAbandono[0]
    #print (vAbandono[0])
    
    print("-------------- Inicio de Simulación --------------")
    print(header)
    LlegadaCliente()
    if casoCliente == 0 and casoServidor == 0:
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
    elif casoCliente == 0 and casoServidor == 1:
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
    elif casoCliente == 1 and casoServidor == 0:
        while True:
            HA = min(SigFinServicio, SigLlegada, dt.fromtimestamp(vAbandono[0]))
            if min(SigFinServicio, SigLlegada, dt.fromtimestamp(vAbandono[0])) == SigFinServicio:
                FinServicio()
            elif min(SigFinServicio, SigLlegada, dt.fromtimestamp(vAbandono[0])) == SigLlegada:
                LlegadaCliente()
            elif min(SigFinServicio, SigLlegada, dt.fromtimestamp(vAbandono[0])) == dt.fromtimestamp(vAbandono[0]):
                AbandonoCliente()
            elif SigFinServicio == SigLlegada == dt.fromtimestamp(vAbandono[0]):
                print ("Error")
                break
            #tabla = [P, SigLlegada, SigFinServicio, Q, PS]
            print(HA,"        ", SigLlegada, "                 ", SigFinServicio, "              ",vAbandono," ", Q,"  ", PS) 
            if HA >= HF:
                print("-------------- Fin de la simulación -------------- ") 
                break
    elif casoCliente == 1 and casoServidor == 1:
        LlegadaServidor()
        while True:
            HA = min(SigFinServicio, SigLlegada, SigLlegadaS, SigSalidaS, vAbandono[0])
            if min(SigFinServicio, SigLlegada, SigLlegadaS, SigSalidaS, vAbandono[0]) == SigFinServicio:
                FinServicio()
            elif min(SigFinServicio, SigLlegada, SigLlegadaS, SigSalidaS, vAbandono[0]) == SigLlegada:
                LlegadaCliente()
            elif min(SigFinServicio, SigLlegada, SigLlegadaS, SigSalidaS, vAbandono[0]) == SigLlegadaS:
                LlegadaServidor()
            elif min(SigFinServicio, SigLlegada, SigLlegadaS, SigSalidaS, vAbandono[0]) == SigSalidaS:
                SalidaServidor()
            elif min(SigFinServicio, SigLlegada, SigLlegadaS, SigSalidaS, vAbandono[0]) == vAbandono[0]:
                AbandonoCliente()
            elif SigFinServicio == SigLlegada == SigLlegadaS == SigSalidaS == vAbandono[0]:
                print ("Error")
                break
            #tabla = [P, SigLlegada, SigFinServicio, SigSalidaS, SigLlegadaS, Q, PS, S]
            print(HA,"        ", SigLlegada, "                 ", SigFinServicio, "              ", SigSalidaS, "                ", SigLlegadaS, "                   ", vAbandono[0], " ", Q,"  ", PS, "  ", S) 
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
    print("Abandona el servidor?:", casoServidor)
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