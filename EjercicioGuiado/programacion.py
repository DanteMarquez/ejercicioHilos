import datetime

class Programacion:
    def get_programacion_info(self):
        return f'{self._hora_entrada:%H:%M:%S} - {self._hora_salida:%H:%M:%S}'
        
class Matutino(Programacion):
    _hora_entrada = datetime.time(8, 0, 0)
    _hora_salida = datetime.time(16, 0, 0)

class Vespertino(Programacion):
    _hora_entrada = datetime.time(12, 0, 0)
    _hora_salida = datetime.time(20, 0, 0)