import random 
import time
import threading



class Barbero(threading.Thread):
    #estados del barbero: trabajando, dormido
    def __init__(self):
        super().__init__()
        self.estado = False #No tiene estado hasta q llega un cliente
    
    def get(self): #getter
        return self.estado
    
    def setter(self, nuevo):
        self.estado = nuevo #cambiamos el estado del barbero

class Cliente(threading.Thread):
    #estados del cliente: esperando en una silla, atendido o se va(no hay sitio para él)
    #posición si está en la barbería: silla 1, silla 2, silla 3 o barbero
    #si está siendo atendido, tiene que tener un tiempo (para que le corte el pelo o lo que sea)
    def __init__(self, id, estado):
        super().__init__()
        self.id = id
        self.estado = estado #no tiene estado
        self.tiempo_espera = random.randint(5, 25)
        self.tiempoEsperando = 8 #Solo aumenta si ya está con el barbero
    def get_estado(self):
        return self.estado
    def get_id(self):
        return self.id
    def set_tiempo_esperando(self, nuevo):
        self.tiempoEsperando = nuevo
    def set_estado(self, nuevo):
        self.estado = nuevo
    def set_id(self, nuevo):
        self.id = nuevo
    

#Main

sillas = 4
clientes = 8
barbero_durmiendo = threading.Semaphore(0)
cliente_esperando = threading.Semaphore(0)

lista= []
barbero = Barbero()
lista.append(barbero)

for i in range(clientes):
    lista.asppend(Cliente())

for a in lista:
    a.start()

for e in lista:
    e.join()


