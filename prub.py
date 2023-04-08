import random 
import random 
import time

class Barbero:
    #estados del barbero: trabajando, dormido
    def __init__(self):
        self.estado = False #No tiene estado hasta q llega un cliente
    
    def get(self): #getter
        return self.estado
    
    def setter(self, nuevo):
        self.estado = nuevo #cambiamos el estado del barbero

class Cliente:
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
    
class Cola:
    def __init__(self):
        #cola vacia
        self.items= []
    
    def encolar(self, x):
        self.items.append(x)
    def get(self):
        lista = []
        for d in self.items:
        
            a = [d.get_id(), d.get_estado()]
            lista.append(a)
        return lista
    def desencolar(self):
        try:
            return self.items.pop(0)
        except:
            raise ValueError('La cola esta vacia')
    def longitud ( self):
        return len(self.items)
    def vacia(self):
        return self.items == []
    
    def first(self):
        try:
             a= self.items[0]
        except:
            raise ValueError('No hay primer elemento')
        return a
#Main

barbero = Barbero()
cola = Cola()
num = 0
i = 0
usuario = input('Quieres empezar?  Si/No\n')
while usuario == 'Si':
    
    if i % 10 == 0:
        usuario =  input('Llegó un nuevo cliente\nQuiéres continuar? Si/No\n')
        num +=1
        if cola.vacia(): #añadimos un cliente
            cliente = Cliente(num, 'Barbero')
            cola.encolar(cliente)
            barbero.setter(True)
    
        elif cola.longitud() == 1:
            cliente = Cliente(num, 'Silla 1')
            cola.encolar(cliente)
        elif cola.longitud() == 2:
            cliente = Cliente(num, 'Silla 2')
            cola.encolar(cliente)
        elif cola.longitud() == 3:
            cliente = Cliente(num, 'Silla 3')
            cola.encolar(cliente)
        else:
            print('El cliente se fue porque no había hueco disponible\n')
            num -= 1 #Se nos fue un cliente
        print('Posiciones totales: Barbero, Silla 1, Silla 2, Silla 3\n')
        c = cola.get()
        print(f'Posiciones ocupadas : {c} \n')
        
    if not cola.vacia():
        if cola.first().tiempo_espera == cola.first().tiempoEsperando:
            cola.desencolar()
            print('Salió un  cliente\n')
            if not cola.vacia():
                cola.first().set_estado('Barbero')
                barbero.setter(True)
            else:
                barbero.setter(False)
            k = 0 #contador de sillas
            for r in cola.items:
                if not k ==0:
                    r.set_estado(f'En Silla {k} ')
                k +=1
            print('Posiciones totales: Barbero, Silla 1, Silla 2, Silla 3\n')
            c = cola.get()
            print(f'Posiciones ocupadas : {c} \n')

        else: 
            cola.first().set_tiempo_esperando(cola.first().tiempoEsperando + 1) #Aumentamos el tiempo del cliente para llegar al tiempo espera
    i +=2            