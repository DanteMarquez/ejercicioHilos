#importamos librerias
import socket
import threading
#se crea clase para el hilo
class hilo_servidor(threading.Thread):
    #se define el metodo constructor para inicializar el hilo y le pasamos los parametros
    def __init__(self,conexion,direccion,sockets):
        threading.Thread.__init__(self)
        self.conexion = conexion
        self.direccion = direccion
        self.socket = sockets
    #se define el metodo constructor para correr el hilo y le pasamos los parametros
    def run(self):
        #impirmir mensaje
        print("\nNueva conexion : ", self.direccion[0])
        #recorremos todos los sockets
        for sock in self.socket:
            try:
                data = "\n"+self.direccion[0]+": Conectado"
                b = bytes(data,'utf-8')
                sock.send(b)
            #siempre se reciben datos con while
            except Exception as identifier:
                continue
        while True:
            data = self.conexion.recv(2048)
            #decodificamos bytes a string
            dt = data.decode()
            #condicion para continuar
            if (dt == ''):
                continue
            #impirmir mensaje
            print(self.direccion[0], " > ", dt)
#se crea clase para el servidor
class servidor():
    #se define metodo inciar
    def iniciar():
        #variable que guarda los sockets que se conectan
        clientes_sockets = []
        #se crea un array para guardar los hilos
        hilos = []
        #definimos el socket
        socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #indicamos el puerto del socket
        socket_server.bind(('localhost', 8080))
        #indicamos que el socket escuche
        socket_server.listen(3)
        #imprimir socket establecido
        print("\nSocket establecido")
        print("\nEsperando...")
        #siempre se reciben datos con while
        while True:
            #establecemos la conexion
            conexion_socket, direccion = socket_server.accept()
            #definiendo el hilo
            hilo = hilo_servidor(conexion_socket,direccion,clientes_sockets)
            #iniciamos el hilo
            hilo.start()
            #se agrega el hilo al array
            hilos.append(hilo)
            #se agrega el cliente al array
            clientes_sockets.append(conexion_socket)
#llamamos el metodo iniciar
servidor.iniciar()

