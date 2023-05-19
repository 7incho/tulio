import random

Q, PS, T, P, SigLlegada, SigFinServicio, SigLlegadaS, SigSalidaS, tci, tcf, tai, taf, caso, S, tdi, tdf, tti, ttf, header = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

def VectorInicial():
    global Q, PS, T, P, tci, tcf, tai, taf, caso, S, tdi, tdf, tti, ttf, header

    Q = int(input("Ingrese la cantidad inicial de clientes en cola: "))
    PS = int(input("Ingrese el estado inicial del puesto de trabajo (ocupado = 1; libre = 0): "))
    T = int(input("Ingrese la duración de la simulación (en minutos): "))
    P = 0
    
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
    global Q, PS, P, SigFinServicio
    if PS == 0 and S == 1:
        PS = 1
        SigFinServicio = P + random.randint(tai, taf)
    else:
        Q = Q + 1
    SigLlegada = SigLlegada + random.randint(tci, tcf)

def FinServicio():
    global Q, PS, SigFinServicio
    if Q >= 1:
        Q = Q - 1
        SigFinServicio = P + random.randint(tai, taf)
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
    S = 1
    SigSalidaS = P + random.randint(tti, ttf)
    
def Simulacion():
    global P, PS, T, Q, SigFinServicio, SigLlegada
    print("-------------- Inicio de Simulación --------------")
    print(header)
    tabla = [P, SigLlegada, SigFinServicio, Q, PS] 
    LlegadaCliente
    while True:
        print(tabla)
        P = min(SigFinServicio, SigLlegada)
        
        if min(SigFinServicio, SigLlegada) == SigFinServicio:
            FinServicio
        elif min(SigFinServicio, SigLlegada) == SigLlegada:
            LlegadaCliente
        if P >= T:
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
# LlegadaCliente()
# FinServicio()
# SalidaServidor()
# LlegadaServidor()
# ImprimirEventos()
