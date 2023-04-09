import random 
import time
import threading


sillas = 4
clientes = 8
sillas_ocupadas = 0
barbero_durmiendo = threading.Semaphore(0)
cliente_entra = threading.Semaphore(0)
cliente_esperando = threading.Semaphore(0)
cliente_atendido = threading.Semaphore(0)

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
        global sillas_ocupadas
        while True:
            if barbero.estado == True: #está durmiendo
                '''
                primero pasa el hilo del barbero, pero al no haber ningún cliente tenemos q bloquearlo.
                Como cliente_entra es cero, va a bloquear al hilo del barbero hasta q suban el del cliente
                '''
                cliente_entra.acquire()
            
            barbero_durmiendo.release() #subimos al barbero
            cliente_esperando.acquire()

            print(f'Barbero peina al cliente \n')
            time.sleep(random.randint(1,2))
            cliente_atendido.release()
            print(f'Cliente atendido y se va \n')
                

class Cliente(threading.Thread):
    #estados del cliente: esperando en una silla, atendido o se va(no hay sitio para él)
    #posición si está en la barbería: silla 1, silla 2, silla 3 o barbero
    #si está siendo atendido, tiene que tener un tiempo (para que le corte el pelo o lo que sea)
    
    
    time.sleep(random.uniform(0,10))
    def __init__(self, id):
        super().__init__()
        self.id = id
        
    def get_id(self):
        return self.id
    def set_id(self, nuevo):
        self.id = nuevo
    
    def run (self):
        global sillas_ocupadas
        if sillas_ocupadas == sillas:
            print('El cliente se fue al no haber sillas\n')
        else:
            if barbero.estado == True: #barbero durmiendo
                cliente_entra.release()#un cliente tiene al barbero
                print(f'El cliente {self.id} está con el barbero.\n')
                sillas_ocupadas += 1
                barbero.setter(False) #despierto
                barbero_durmiendo.acquire()#bloquear barbero
                
            else:
                sillas_ocupadas += 1 #Un cliente más
                print(f'El cliente {self.id} se sienta en una silla\n')
                barbero_durmiendo.acquire() #Bajamos al barbero para bloquearle
                
            print(f'El cliente {self.id} se está peinando\n')  
            sillas_ocupadas -= 1 #se va el cliente
            cliente_esperando.release()  
            cliente_atendido.acquire()
            print(f'El cliente {self.id} termina y se va\n')
            
            
            if sillas_ocupadas == 0:
                print('El barbero se duerme porque no hay clientes\n')
                barbero.setter(True)
            
            

#Main


lista= []
barbero = Barbero()
lista.append(barbero)

for i in range(clientes):
    c = Cliente(i)
    lista.append(c)

for a in lista:
    a.start()

for e in lista:
    e.join()



