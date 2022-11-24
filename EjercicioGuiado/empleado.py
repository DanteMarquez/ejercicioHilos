class Empleado:
    def __init__(self, nombre, apellido, salario, programacion):
        self._nombre = nombre
        self._apellido = apellido
        self.salario = salario
        self.programacion = programacion
    def get_nombre_completo(self):
        return self._nombre + " " + self._apellido    

class Gerente(Empleado):
    puesto = "Gerente General"

class Tecnico(Empleado):
    puesto = "Técnico"

class Gestora(Empleado):
    puesto = "Gestora de Cobranza"

class Administrador(Empleado):
    puesto = "Administrador de Servicios de Cable"

