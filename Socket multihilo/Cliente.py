#importamos librerias
import socket
import threading
#creamos clase hilo cliente
class hilo_cliente(threading.Thread):
    #inicializamos el hilo
    def __init__(self,socket):
        threading.Thread.__init__(self)
        self.socket = socket
        #definimos run
    def run(self):
        #siempre recibe lo que mande el servidor
        while True:
            data = self.socket.recv(2048)
            #decodificamos bytes a string
            dt = data.decode()
            #condicion para continuar
            if (dt == ''):
                continue
            #imprimimos mensaje
            print(dt)
#creamos clase cliente
class cliente():
    #definimos metodo iniciar
    def iniciar():
        #establecer socket cliente
        socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #imprimir socket establecido
        print("\nSocket establecido")
        #indicamos el puerto del socket
        socket_cliente.connect(('localhost', 8080))
        #imprimir socket conectado
        print("\nSocket conectado")
        #definimos el hilo cliente
        hl = hilo_cliente(socket_cliente)
        #iniciamos el hilo cliente
        hl.start()
        #condicion para instroducir datos
        while True:
            data = input(" Escriba un mensaje: ")
            #codificamos string a bytes
            dt = bytes(data,'utf-8')
            #inciamos el envio de datos
            socket_cliente.send(dt)
cliente.iniciar()