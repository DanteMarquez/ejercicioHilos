class Reporte:
    def __init__(self, lista_empleados):
        self._lista_empleados = lista_empleados

class ReporteContabilidad(Reporte):
    def print_reporte(self):
        print("-------------------------------------")
        print("...::: Reporte de Contabilidad :::...")
        print("-------------------------------------")
        for e in self._lista_empleados:
            print("Nombre: ", e.get_nombre_completo(), ",", "Salario: ", e.salario)

class ReporteEmpleados(Reporte):
    def print_reporte(self):
        print("-------------------------------------")
        print("...::: Reporte de Empleados :::...")
        print("-------------------------------------")
        for e in self._lista_empleados:
            print("Nombre: ", e.get_nombre_completo(), ",", "Puesto: ", e.puesto)

class ReporteProgramacion(Reporte):
    def print_reporte(self):
        print("-------------------------------------")
        print("...::: Reporte de Programación :::...")
        print("-------------------------------------")
        for e in self._lista_empleados:
            print("Nombre: ", e.get_nombre_completo(), ",", "Horario: ", e.programacion.get_programacion_info(), "Hrs.")