import logging
import random
import threading
import time

def trabajador():
    """funcion del trabajador"""
    pausa = random.randint(1, 5) / 10
    logging.debug('sleeping %0.2f', pausa)
    time.sleep(pausa)
    logging.debug('ending')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(3):
    h = threading.Thread(target=trabajador, daemon=True)
    h.start()

hilo_principal = threading.main_thread()
for h in threading.enumerate():
    if h is hilo_principal:
        continue
    logging.debug('joining %s', h.name)
    h.join()
