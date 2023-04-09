import random 
import time
import threading



class Barbero(threading.Thread):
    #estados del barbero: trabajando, dormido
    def __init__(self):
        super().__init__()
        self.estado = True #True dormir
    
    def get(self): #getter
        return self.estado
    
    def setter(self, nuevo):
        self.estado = nuevo #cambiamos el estado del barbero
    
    def run(self):
        while True:
            barbero_durmiendo.release() #subimos al barbero
            cliente_esperando.acquire() #bajamos 1 cliente
            print(f'barbero peina al cliente\n')
            time.sleep(3)
            cliente_atendido.release()
                

class Cliente(threading.Thread):
    #estados del cliente: esperando en una silla, atendido o se va(no hay sitio para él)
    #posición si está en la barbería: silla 1, silla 2, silla 3 o barbero
    #si está siendo atendido, tiene que tener un tiempo (para que le corte el pelo o lo que sea)
    time.sleep(random.randint(5,15))
    def __init__(self, id):
        super().__init__()
        self.id = id
        
    def get_id(self):
        return self.id
    def set_id(self, nuevo):
        self.id = nuevo
    
    def run (self):
        if sillas_ocupadas == sillas:
            print('El cliente se fue al no haber sillas')
        else:
            if barbero.estado:
               cliente_esperando.release()#un cliente tiene al barbero
               sillas_ocupadas += 1
               print(f'El cliente {self.id} está con el barbero\n')
               barbero.setter(False) #despierto
               barbero_durmiendo.acquire()#bloquear barbero
            else:
                sillas_ocupadas += 1 #Un cliente más
                print(f'El cliente {self.id} se sienta en la silla {sillas_ocupadas}\n')
                barbero_durmiendo.acquire() #Bajamos al barbero para bloquearle
                
    

#Main

sillas = 4
clientes = 8
sillas_ocupadas = 0
barbero_durmiendo = threading.Semaphore(0)
cliente_esperando = threading.Semaphore(0)
cliente_atendido = threading.Semaphore(0)

lista= []
barbero = Barbero()
lista.append(barbero)

for i in range(clientes):
    lista.append(Cliente(i))

for a in lista:
    a.start()

for e in lista:
    e.join()



