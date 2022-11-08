import threading

import socket
import threading
import logging
from time import sleep


# define logging 
logging.basicConfig(
    format='(%(threadName)-10s) %(asctime)s %(message)s', level=logging.DEBUG)


def client_handler(conn, addr):
    """ CONEXION CON EL CLIENTE """
    # conexion log
    logging.debug('Conectado ' + str(addr))

    # crear
    try:
        # leer index.html
        with open('index.html', 'r') as f:
            file_data = f.read()
            print(file_data)
            f.close()
        
        # enviar respuesta http
        conn.send(b'HTTP/1.0 200 OK\r\n')
        conn.send(b'Content-Type: text/html\n')
        conn.send(b'\n')

        # enviar index.html
        conn.send(file_data.encode())

        # imprimir mensaje
        logging.debug('Conexion cerrada ' + str(addr))
        return
    finally:
        # imprimir mensajee
        logging.debug('Conexion cerrada ' + str(addr))
        # cerrar conexion
        conn.close()

if __name__ == '__main__':
    # crear TCP/IP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # configurar socket
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # definir host y puerto
    host = 'localhost'
    port = 8080

    # bind al puerto
    server.bind((host, port))

    # fila de 5 peticiones
    server.listen(10)

    # iniciar log del servidor
    logging.debug("Escuchando " + host + ":" + str(port))

    while True:
        # establecer conexion
        conn, addr = server.accept()

        clientThread = threading.Thread(
            target=client_handler, args=(conn, addr))

        # iniciar el hilo cliente
        clientThread.start()