import random
import datetime as dt

Q= PS =T= casoServidor= casoCliente= S= header= 0
tci= tcf= tai= taf= tdi= tdf= tti= ttf= tAbandonoi= tAbandonof= 0
HA = HF = SigFinServicio = SigLlegada = SigLlegadaS = SigSalidaS = dt.datetime(2000,1,1,0,0,0)

vAbandono = [HF]

def VectorInicial():
    global Q, PS, T, tci, tcf, tai, taf, casoServidor, casoCliente, S, tdi, tdf, tti, ttf, header, SigFinServicio, SigLlegada, SigLlegadaS, SigSalidaS, HF, HA, tAbandonoi, tAbandonof
    
    aux = dt.timedelta(hours=int(input("Ingrese hora de inicio de la simulación: ")))
    HA = HA + aux
    Q = int(input("Ingrese la cantidad inicial de clientes en cola: "))
    PS = int(input("Ingrese el estado inicial del puesto de trabajo (ocupado = 1; libre = 0): "))
    T = int(input("Ingrese la duración de la simulación (en minutos): "))
    HF = HA + dt.timedelta(minutes=T)
    SigFinServicio= SigLlegada= SigLlegadaS= SigSalidaS= vAbandono[0]= HF
    
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
        header = ["Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "H. Prox Abandono", "Q", "PS"]
    elif casoCliente == 0 and casoServidor == 1:
        header = ["Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "H.Prox Salida servidor", "H.Prox Llegada servidor", "Q", "PS", "S"]
    elif casoCliente == 0 and casoServidor == 0:
        header = ["Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "Q", "PS"]
        
def LlegadaCliente():
    a=random.randint(tai, taf)
    b=random.randint(tci, tcf)
    global Q, PS, HA, SigFinServicio, SigLlegada, casoCliente, vAbandono
    
    if PS == 0 and S == 1:
        PS = 1
        SigFinServicio = HA + dt.timedelta(minutes=a)
        if casoCliente == 1:
            vAbandono[0] = HF
    else:
        Q = Q + 1
        if casoCliente == 1:
            c = random.randint(tAbandonoi, tAbandonof)
            if vAbandono[0] == HF:
                vAbandono[0] = HA + dt.timedelta(minutes=c)
            else:
                vAbandono.append(HA + dt.timedelta(minutes=c))
    SigLlegada = HA + dt.timedelta(minutes=b)

def FinServicio():
    a=random.randint(tai, taf)
    global Q, PS, SigFinServicio
    if Q >= 1:
        Q = Q - 1
        if casoCliente == 1:
            if len(vAbandono) == 1:
                vAbandono[0] = HF
            else:
                del vAbandono[0]
        SigFinServicio = HA + dt.timedelta(minutes=a)
        #print(SigFinServicio)
    else:
        PS = 0
        SigFinServicio = HF 
        if casoCliente == 1:
              vAbandono[0] = HF  

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
    if len(vAbandono) == 1:
        vAbandono[0] = HF
    else:
        del vAbandono[0]
    
def Simulacion():
    global HA, PS, T, Q, SigFinServicio, SigLlegada, vAbandono
    #print (vAbandono[0])
    
    print("-------------- Inicio de Simulación --------------")
    print(header)
    LlegadaCliente()
    print("Hora final: ", horaMin(HF))
    print("Hora inicial: ", horaMin(HA))
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
            #"Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "Q", "PS"
            print(HA.hour,":", HA.minute,"        ", SigLlegada.hour, ":", SigLlegada.minute, "                 ", SigFinServicio.hour, ":", SigFinServicio.minute, "              ", Q,"  ", PS) 
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
            #"Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "H.Prox Salida servidor", "H.Prox Llegada servidor", "Q", "PS", "S"
            print(HA.hour,":", HA.minute,"        ", SigLlegada.hour, ":", SigLlegada.minute, "                 ", SigFinServicio.hour, ":", SigFinServicio.minute, "              ", SigSalidaS.hour, ":", SigSalidaS.minute, "                ", SigLlegadaS.hour, ":", SigLlegadaS.minute,  "                   ", Q,"  ", PS, "  ", S) 
            if HA >= HF:
                print("-------------- Fin de la simulación -------------- ") 
                break
    elif casoCliente == 1 and casoServidor == 0:
        while True:
            HA = min(SigFinServicio, SigLlegada, vAbandono[0])
            if min(SigFinServicio, SigLlegada, vAbandono[0]) == SigFinServicio:
                FinServicio()
            elif min(SigFinServicio, SigLlegada, vAbandono[0]) == SigLlegada:
                LlegadaCliente()
            elif min(SigFinServicio, SigLlegada, vAbandono[0]) == vAbandono[0]:
                AbandonoCliente()
            elif SigFinServicio == SigLlegada == vAbandono[0]:
                print ("Error")
                break
            #"Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "H. Prox Abandono", "Q", "PS"
            print(HA.hour,":", HA.minute,"        ", SigLlegada.hour, ":", SigLlegada.minute, "                 ", SigFinServicio.hour, ":", SigFinServicio.minute, "              ",vAbandono[0].hour, ":", vAbandono[0].minute," ", Q,"  ", PS) 
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
            #"Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "H.Prox Salida servidor", "H.Prox Llegada servidor", "H. Prox Abandono", "Q", "PS", "S"
            print(HA,"        ", SigLlegada, "                 ", SigFinServicio, "              ", SigSalidaS, "                ", SigLlegadaS, "                   ", vAbandono[0], " ", Q,"  ", PS, "  ", S) 
            if HA >= HF:
                print("-------------- Fin de la simulación -------------- ") 
                break
    return

#un intento de poner bien el formato, borrenlo si quieren
def horaMin(a):
    x = a.hour, ":", a.minute
    return x

def ImprimirVector():
    print("Clientes en cola:", Q)
    print("Puesto de servicio:", PS)
    print("Duración de la simulación:", T)
    print("Tiempo actual:", HA)
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