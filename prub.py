import random 
import time
import threading

class Barbero(threading.Thread):
    #estados del barbero: trabajando, dormido
    def __init__(self):
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

def empezar(hilo):
    hilo.start()

lista= []

for i in range(2):
    lista.append(Barbero())
for a in lista:
    empezar(a)

cont = 2
client = []
num = 1
for c in range(cont):
    client.append(Cliente(num, 'esperando'))
    num +=1

for r in client:
    for h in lista:
        if h.get() == False:
            r.start()
            r.set_estado('atendido')

for u in client:
    print(u.get())




