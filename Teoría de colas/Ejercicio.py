import random
import datetime as dt

QGral= QPrio= PS= ZN= tZN= T= caso= S= 0
#tLlegadaGrali= tLlegadaGralf= tAtencioni= tAtencionf= tDescansoi= tDescansof= tTrabajoi= tTrabajof= tAbandonoGrali= tAbandonoGralf= 0
tLlegadaGral= tLlegadaPrio= tAtencion= tDescanso= tTrabajo= tAbandonoGral= tAbandonoPrio= [0,0]
horaActual= horaFinal= SigFinServicio= SigLlegadaGral= SigLlegadaPrio= SigLlegadaServ= SigSalidaServ= dt.datetime(2000,1,1,0,0,0)

vAbandonoGral= vAbandonoPrio= [horaFinal]

def VectorInicial():
    global QGral, QPrio, PS, ZN, tZN, T, caso, S, tLlegadaGral, tLlegadaPrio, tAtencion, tDescanso, tTrabajo, tAbandonoGral, tAbandonoPrio, horaActual, horaFinal, SigFinServicio, SigLlegadaGral, SigLlegadaPrio, SigLlegadaServ, SigSalidaServ, vAbandonoGral, vAbandonoPrio
    
    aux = dt.timedelta(hours=int(input("Ingrese hora de inicio de la simulación: ")))
    horaActual = horaActual + aux
    PS = int(input("Ingrese el estado inicial del puesto de trabajo (ocupado = 1; libre = 0): "))
    T = int(input("Ingrese la duración de la simulación (en minutos): "))
    horaFinal = horaActual + dt.timedelta(minutes=T)
    SigFinServicio= SigLlegadaGral= SigLlegadaPrio= SigLlegadaServ= SigSalidaServ= vAbandonoGral[0]= vAbandonoPrio[0]= horaFinal
    
    print("Ingrese el intervalo que tarda el puesto de servicio en atender los clientes: ")
    tAtencion[0] = int(input("Mínimo: "))
    tAtencion[1] = int(input("Máximo: "))
    
    if int(input("¿Existen clientes con prioridad? (Si = 1; No = 0): ")) == 1:
        QGral = int(input("Ingrese la cantidad inicial de clientes en cola SIN prioridad: "))
        print("Ingrese el intervalo en el que llegan los clientes SIN prioridad: ") 
        tLlegadaGral[0] = int(input("Mínimo: "))
        tLlegadaGral[1] = int(input("Máximo: "))
        QPrio = int(input("Ingrese la cantidad inicial de clientes en cola CON prioridad: "))
        print("Ingrese el intervalo en el que llegan los clientes CON prioridad: ") 
        tLlegadaPrio[0] = int(input("Mínimo: "))
        tLlegadaPrio[1] = int(input("Máximo: "))
        
        if int(input("¿Los clientes pueden abandonar la cola de espera? (Si = 1; No = 0): ")) == 1:
            print("Ingrese el intervalo de los abandonos de los clientes SIN prioridad: ")
            tAbandonoGral[0] = int(input("Mínimo: "))
            tAbandonoGral[1] = int(input("Máximo: "))
            print("Ingrese el intervalo de los abandonos de los clientes CON prioridad: ")
            tAbandonoPrio[0] = int(input("Mínimo: "))
            tAbandonoPrio[1] = int(input("Máximo: "))
            
            if int(input("¿El servidor puede abandonar el puesto de trabajo? (Si = 1; No = 0): ")) == 1:
                S = int(input("Ingrese el valor inicial del servidor del puesto de trabajo (presente = 1; ausente = 0): "))
                print("Ingrese el intervalo de duración de los descansos: ")
                tDescanso[0] = int(input("Mínimo: "))
                tDescanso[1] = int(input("Máximo: "))
                print("Ingrese el intervalo de tiempo en el que trabaja el servidor: ")
                tTrabajo[0] = int(input("Mínimo: "))
                tTrabajo[1] = int(input("Máximo: "))
                
                if int(input("¿Existe una zona segura en el modelo? (Si = 1; No = 0): ")) == 1:
                    tZN = int(input("Ingrese el tiempo en minutos que demora un cliente en pasar por la zona de seguridad: "))
                    caso = 0
                else:
                    caso = 1
            else:
                S = 1
                
                if int(input("¿Existe una zona segura en el modelo? (Si = 1; No = 0): ")) == 1:
                    tZN = int(input("Ingrese el tiempo en minutos que demora un cliente en pasar por la zona de seguridad: "))
                    caso = 2
                else:
                    caso = 3
        else:
            if int(input("¿El servidor puede abandonar el puesto de trabajo? (Si = 1; No = 0): ")) == 1:
                S = int(input("Ingrese el valor inicial del servidor del puesto de trabajo (presente = 1; ausente = 0): "))
                print("Ingrese el intervalo de duración de los descansos: ")
                tDescanso[0] = int(input("Mínimo: "))
                tDescanso[1] = int(input("Máximo: "))
                print("Ingrese el intervalo de tiempo en el que trabaja el servidor: ")
                tTrabajo[0] = int(input("Mínimo: "))
                tTrabajo[1] = int(input("Máximo: "))
                
                if int(input("¿Existe una zona segura en el modelo? (Si = 1; No = 0): ")) == 1:
                    tZN = int(input("Ingrese el tiempo en minutos que demora un cliente en pasar por la zona de seguridad: "))
                    caso = 4
                else:
                    caso = 5
            else:
                S = 1
                
                if int(input("¿Existe una zona segura en el modelo? (Si = 1; No = 0): ")) == 1:
                    tZN = int(input("Ingrese el tiempo en minutos que demora un cliente en pasar por la zona de seguridad: "))
                    caso = 6
                else:
                    caso = 7
    else:
        QGral = int(input("Ingrese la cantidad inicial de clientes en cola: "))
        print("Ingrese el intervalo en el que llegan los clientes: ") 
        tLlegadaGral[0] = int(input("Mínimo: "))
        tLlegadaGral[1] = int(input("Máximo: "))
        
        if int(input("¿Los clientes pueden abandonar la cola de espera? (Si = 1; No = 0): ")) == 1:
            print("Ingrese el intervalo de los abandonos de los clientes: ")
            tAbandonoGral[0] = int(input("Mínimo: "))
            tAbandonoGral[1] = int(input("Máximo: "))
            
            if int(input("¿El servidor puede abandonar el puesto de trabajo? (Si = 1; No = 0): ")) == 1:
                S = int(input("Ingrese el valor inicial del servidor del puesto de trabajo (presente = 1; ausente = 0): "))
                print("Ingrese el intervalo de duración de los descansos: ")
                tDescanso[0] = int(input("Mínimo: "))
                tDescanso[1] = int(input("Máximo: "))
                print("Ingrese el intervalo de tiempo en el que trabaja el servidor: ")
                tTrabajo[0] = int(input("Mínimo: "))
                tTrabajo[1] = int(input("Máximo: "))
                
                if int(input("¿Existe una zona segura en el modelo? (Si = 1; No = 0): ")) == 1:
                    tZN = int(input("Ingrese el tiempo en minutos que demora un cliente en pasar por la zona de seguridad: "))
                    caso = 8
                else:
                    caso = 9
            else:
                S = 1
                
                if int(input("¿Existe una zona segura en el modelo? (Si = 1; No = 0): ")) == 1:
                    tZN = int(input("Ingrese el tiempo en minutos que demora un cliente en pasar por la zona de seguridad: "))
                    caso = 10
                else:
                    caso = 11
        else:
            
            if int(input("¿El servidor puede abandonar el puesto de trabajo? (Si = 1; No = 0): ")) == 1:
                S = int(input("Ingrese el valor inicial del servidor del puesto de trabajo (presente = 1; ausente = 0): "))
                print("Ingrese el intervalo de duración de los descansos: ")
                tDescanso[0] = int(input("Mínimo: "))
                tDescanso[1] = int(input("Máximo: "))
                print("Ingrese el intervalo de tiempo en el que trabaja el servidor: ")
                tTrabajo[0] = int(input("Mínimo: "))
                tTrabajo[1] = int(input("Máximo: "))
                
                if int(input("¿Existe una zona segura en el modelo? (Si = 1; No = 0): ")) == 1:
                    tZN = int(input("Ingrese el tiempo en minutos que demora un cliente en pasar por la zona de seguridad: "))
                    caso = 12
                else:
                    caso = 13
            else:
                S = 1
                
                if int(input("¿Existe una zona segura en el modelo? (Si = 1; No = 0): ")) == 1:
                    tZN = int(input("Ingrese el tiempo en minutos que demora un cliente en pasar por la zona de seguridad: "))
                    caso = 14
                else:
                    caso = 15

def LlegadaCliente(case):
    a=random.randint(tAtencion[0], tAtencion[1])
    b=random.randint(tLlegadaGral[0], tLlegadaGral[1])
    global QGral, QPrio, PS, horaActual, SigFinServicio, SigLlegadaGral, caso, vAbandonoGral
    
    if case == "Gral":
        if PS == 0 and S == 1:
            PS = 1
            SigFinServicio = horaActual + dt.timedelta(minutes=a)
            if casoCliente == 1:
                vAbandonoGral[0] = horaFinal
        else:
            QGral = QGral + 1
            if casoCliente == 1:
                c = random.randint(tAbandonoGral[0], tAbandonoGral[1])
                if vAbandonoGral[0] == horaFinal:
                    vAbandonoGral[0] = horaActual + dt.timedelta(minutes=c)
                else:
                    vAbandonoGral.append(horaActual + dt.timedelta(minutes=c))
    elif case == "Prio":
        if PS == 0 and S == 1:
            PS = 1
            SigFinServicio = horaActual + dt.timedelta(minutes=a)
            if casoCliente == 1:
                vAbandonoGral[0] = horaFinal
        else:
            QGral = QGral + 1
            if casoCliente == 1:
                c = random.randint(tAbandonoGral[0], tAbandonoGral[1])
                if vAbandonoGral[0] == horaFinal:
                    vAbandonoGral[0] = horaActual + dt.timedelta(minutes=c)
                else:
                    vAbandonoGral.append(horaActual + dt.timedelta(minutes=c))
    SigLlegadaGral = horaActual + dt.timedelta(minutes=b)

def FinServicio():
    a=random.randint(tAtencion[0], tAtencion[1])
    global QGral, PS, SigFinServicio
    if QGral >= 1:
        QGral = QGral - 1
        if casoCliente == 1:
            if len(vAbandonoGral) == 1:
                vAbandonoGral[0] = horaFinal
            else:
                del vAbandonoGral[0]
        SigFinServicio = horaActual + dt.timedelta(minutes=a)
        #print(SigFinServicio)
    else:
        PS = 0
        SigFinServicio = horaFinal 
        if casoCliente == 1:
              vAbandonoGral[0] = horaFinal  

def SalidaServidor():
    global S, SigLlegadaServ, SigFinServicio, SigSalidaServ
    a = random.randint(tDescanso[0], tDescanso[1])
    S = 0
    SigLlegadaServ = horaActual + dt.timedelta(minutes=a)
    if PS == 1:
        SigFinServicio = SigFinServicio + dt.timedelta(minutes=a)
    if SigFinServicio == SigSalidaServ:
        FinServicio()
    SigSalidaServ = horaFinal

def LlegadaServidor():
    a=random.randint(tTrabajo[0], tTrabajo[1])
    global S, SigSalidaServ, SigLlegadaServ
    S = 1
    SigSalidaServ = horaActual + dt.timedelta(minutes=a)
    SigLlegadaServ = horaFinal
    
def AbandonoCliente():
    global QGral
    QGral = QGral-1
    if len(vAbandonoGral) == 1:
        vAbandonoGral[0] = horaFinal
    else:
        del vAbandonoGral[0]

def header1():
    print("{:<13}{:<24}{:<21}{:<3}{:<4}".format("Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "QGral", "PS"))

def header2():
    print("{:<13}{:<24}{:<21}{:<24}{:<25}{:<3}{:<3}{:<4}".format("Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "H.Prox Salida servidor", "H.Prox Llegada servidor", "QGral", "PS", "S"))

def header3():
    print("{:<13}{:<24}{:<21}{:<18}{:<3}{:<4}".format("Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "H. Prox Abandono", "QGral", "PS"))

def header4():
    print("{:<13}{:<24}{:<21}{:<24}{:<25}{:<18}{:<3}{:<3}{:<4}".format("Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "H.Prox Salida servidor", "H.Prox Llegada servidor", "H. Prox Abandono", "QGral", "PS", "S"))

def Simulacion():
    global horaActual, PS, T, QGral, SigFinServicio, SigLlegadaGral, vAbandonoGral, S
    
    print("-------------- Inicio de Simulación --------------")
    if(header==1):
        header1()
    elif(header==2):
        header2()
    elif(header==3):
        header3()
    elif(header==4):
        header4()
    print("---------------------------------------------------------------")
    LlegadaCliente()
    if casoCliente == 0 and casoServidor == 0:
        while True:
            horaActual = min(SigFinServicio, SigLlegadaGral)
            if min(SigFinServicio, SigLlegadaGral) == SigFinServicio:
                FinServicio()
            elif min(SigFinServicio, SigLlegadaGral) == SigLlegadaGral:
                LlegadaCliente()
            elif SigFinServicio == SigLlegadaGral:
                print ("Error")
                break
            #"Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "QGral", "PS"
            print("{:>2}{:<1}{:<10}{:>2}{:<1}{:<21}{:>2}{:<1}{:<18}{:<3}{:<4}".format(horaActual.hour,":",horaActual.minute, SigLlegadaGral.hour,":", SigLlegadaGral.minute, SigFinServicio.hour,":", SigFinServicio.minute, QGral, PS, S)) 
            if horaActual >= horaFinal:
                print("-------------- Fin de la simulación -------------- ") 
                break
    elif casoCliente == 0 and casoServidor == 1:
        LlegadaServidor()
        while True:
            horaActual = min(SigFinServicio, SigLlegadaGral, SigLlegadaServ, SigSalidaServ)
            if min(SigFinServicio, SigLlegadaGral, SigLlegadaServ, SigSalidaServ) == SigFinServicio:
                FinServicio()
            elif min(SigFinServicio, SigLlegadaGral, SigLlegadaServ, SigSalidaServ) == SigLlegadaGral:
                LlegadaCliente()
            elif min(SigFinServicio, SigLlegadaGral, SigLlegadaServ, SigSalidaServ) == SigLlegadaServ:
                LlegadaServidor()
            elif min(SigFinServicio, SigLlegadaGral, SigLlegadaServ, SigSalidaServ) == SigSalidaServ:
                SalidaServidor()
            elif SigFinServicio == SigLlegadaGral == SigLlegadaServ == SigSalidaServ:
                print ("Error")
                break
            #"Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "H.Prox Salida servidor", "H.Prox Llegada servidor", "QGral", "PS", "S"
            print("{:>2}{:<1}{:<10}{:>2}{:<1}{:<21}{:>2}{:<1}{:<18}{:>2}{:<1}{:<21}{:>2}{:<1}{:<22}{:<3}{:<3}{:<4}".format(horaActual.hour,":", horaActual.minute, SigLlegadaGral.hour,":", SigLlegadaGral.minute, SigFinServicio.hour,":", SigFinServicio.minute, SigSalidaServ.hour,":", SigSalidaServ.minute,  SigLlegadaServ.hour,":", SigLlegadaServ.minute, QGral, PS, S)) 
            if horaActual >= horaFinal:
                print("-------------- Fin de la simulación -------------- ") 
                break
    elif casoCliente == 1 and casoServidor == 0:
        while True:
            horaActual = min(SigFinServicio, SigLlegadaGral, vAbandonoGral[0])
            if min(SigFinServicio, SigLlegadaGral, vAbandonoGral[0]) == SigFinServicio:
                FinServicio()
            elif min(SigFinServicio, SigLlegadaGral, vAbandonoGral[0]) == SigLlegadaGral:
                LlegadaCliente()
            elif min(SigFinServicio, SigLlegadaGral, vAbandonoGral[0]) == vAbandonoGral[0]:
                AbandonoCliente()
            elif SigFinServicio == SigLlegadaGral == vAbandonoGral[0]:
                print ("Error")
                break
            #"Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "H. Prox Abandono", "QGral", "PS"
            print("{:>2}{:<1}{:<10}{:>2}{:<1}{:<21}{:>2}{:<1}{:<18}{:>2}{:<1}{:<15}{:<3}{:<4}".format(horaActual.hour,":", horaActual.minute, SigLlegadaGral.hour,":", SigLlegadaGral.minute, SigFinServicio.hour,":", SigFinServicio.minute, vAbandonoGral[0].hour,":", vAbandonoGral[0].minute, QGral, PS)) 
            if horaActual >= horaFinal:
                print("-------------- Fin de la simulación -------------- ") 
                break
    elif casoCliente == 1 and casoServidor == 1:
        LlegadaServidor()
        while True:
            horaActual = min(SigFinServicio, SigLlegadaGral, SigLlegadaServ, SigSalidaServ, vAbandonoGral[0])
            if min(SigFinServicio, SigLlegadaGral, SigLlegadaServ, SigSalidaServ, vAbandonoGral[0]) == SigFinServicio:
                FinServicio()
            elif min(SigFinServicio, SigLlegadaGral, SigLlegadaServ, SigSalidaServ, vAbandonoGral[0]) == SigLlegadaGral:
                LlegadaCliente()
            elif min(SigFinServicio, SigLlegadaGral, SigLlegadaServ, SigSalidaServ, vAbandonoGral[0]) == SigLlegadaServ:
                LlegadaServidor()
            elif min(SigFinServicio, SigLlegadaGral, SigLlegadaServ, SigSalidaServ, vAbandonoGral[0]) == SigSalidaServ:
                SalidaServidor()
            elif min(SigFinServicio, SigLlegadaGral, SigLlegadaServ, SigSalidaServ, vAbandonoGral[0]) == vAbandonoGral[0]:
                AbandonoCliente()
            elif SigFinServicio == SigLlegadaGral == SigLlegadaServ == SigSalidaServ == vAbandonoGral[0]:
                print ("Error")
                break
            #"Hora actual", "H.Prox llegada cliente", "H.Prox fin servicio", "H.Prox Salida servidor", "H.Prox Llegada servidor", "H. Prox Abandono", "QGral", "PS", "S"
            print("{:>2}{:<1}{:<10}{:>2}{:<1}{:<21}{:>2}{:<1}{:<18}{:>2}{:<1}{:<21}{:>2}{:<1}{:<22}{:>2}{:<1}{:<15}{:<3}{:<3}{:<4}".format(horaActual.hour,":", horaActual.minute, SigLlegadaGral.hour,":", SigLlegadaGral.minute, SigFinServicio.hour,":", SigFinServicio.minute, SigSalidaServ.hour,":", SigSalidaServ.minute,  SigLlegadaServ.hour,":", SigLlegadaServ.minute, vAbandonoGral[0].hour,":", vAbandonoGral[0].minute, QGral, PS, S)) 
            if horaActual >= horaFinal:
                print("-------------- Fin de la simulación -------------- ") 
                break
    return

# def ImprimirVector():
#     print("Clientes en cola:", QGral)
#     print("Puesto de servicio:", PS)
#     print("Duración de la simulación:", T)
#     print("Tiempo actual:", horaActual)
#     print("Intervalo de atención:", tAtencioni, "-", tAtencionf)
#     print("Intervalo de llegada:", tLlegadaGrali, "-", tLlegadaGralf)
#     print("Abandona el servidor?:", casoServidor)
#     print("Intervalo de trabajo:", tTrabajoi, "-", tTrabajof)
#     print("Intervalo de descanso:", tDescansoi, "-", tDescansof)
    
# def ImprimirEventos():
#     print("Siguiente llegada de cliente:", SigLlegadaGral)
#     print("Siguiente fin de servicio:", SigFinServicio)
#     print("Siguiente salida del servidor:", SigSalidaServ)
#     print("Siguiente llegada del servidor:", SigLlegadaServ)

# Llamadas a las funciones

VectorInicial()
Simulacion()

# ImprimirVector()
# ImprimirEventos()