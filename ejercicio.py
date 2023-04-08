'''
Barbero tiene 3 sillas, atiende a n clientes. No clientes barbero duerme, llega uno este le despierta
Llega un cliente y el barbero está ocupado, se sienta en la silla 1, si llega otro en la 2 y luego en la 3
estos esperan en las sillas. 3 sillas ocupadas y barbero también entonces cliente se va 

'''
class Barbero:
    #estados del barbero: trabajando, dormido
    def __init__(self):
        self.estado = None #No tiene estado hasta q llega un cliente
    
    def get(self): #getter
        return self.estado
    
    def setter(self, nuevo):
        self.estado = nuevo #cambiamos el estado del barbero

class Cliente:
    #estados del cliente: esperando en una silla, atendido o se va(no hay sitio para él)
    #posición si está en la barbería: silla 1, silla 2, silla 3 o barbero
    #si está siendo atendido, tiene que tener un tiempo (para que le corte el pelo o lo que sea)
    def __init__(self):
        self.estado = None #no tiene estado
        self.lugar = None #donde está el cliente
    def get_estado(self):
        return self.estado
    def get_posicion(self):
        return self.lugar
    
    def set_estado(self, nuevo):
        self.estado = nuevo
    def set_posicion(self, nuevo):
        self.lugar = nuevo