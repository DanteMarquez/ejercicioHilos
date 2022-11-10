# Importamos librerias

import time
from multiprocessing import Pool
import logging
import cv2 as cv
# ruta de la imagen
REL = ""
# Funcion principal descripcion del formato de la imagen
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s (%(threadName)-2s) %(message)s',
)

# Procesamiento de la imagen
def process_image(filename, threshold):
    logging.debug(f'Processing {filename}')
    image = cv.imread(REL+filename)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray, threshold, 255, cv.THRESH_BINARY)
    cv.imwrite(f'{REL}processed_{threshold}_{filename}', thresh)
    logging.debug(f'Finished processing {filename}')


# Funcion principal
if __name__ == '__main__':
    # Seleccion del numero de procesadores a utilizar
    p = Pool()
    thresholds = range(0, 255, 5)
    for thresh in thresholds:
        p.apply_async(process_image, args=(f'imagen.jpg', thresh))
    p.close()
    p.join()