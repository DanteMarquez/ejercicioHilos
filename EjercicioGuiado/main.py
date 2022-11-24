from empleado import Gerente
from empleado import Tecnico
from empleado import Gestora
from empleado import Administrador
from reportes import ReporteContabilidad
from reportes import ReporteEmpleados
from reportes import ReporteProgramacion
from programacion import Matutino
from programacion import Vespertino

empleados = [
    Gerente("Roberto", "Figueroa", "$20,000.00", Matutino()),
    Gestora("Alejandra", "Millan", "$8,000.00", Matutino()),
    Gestora("Selene", "Sánchez", "$8,000.00", Matutino()),
    Tecnico("Artemio", "Velazco", "$9,000.00", Vespertino()),
    Tecnico("Salvador", "Infante", "$9,000.00", Vespertino()),
    Tecnico("Rolando", "Casas", "$9,000.00", Matutino()),
    Administrador("Marco", "Blanco", "$9,000.00", Matutino()),
]

reportes = [
    ReporteContabilidad(empleados),
    ReporteEmpleados(empleados),
    ReporteProgramacion(empleados)
]

for r in reportes:
    r.print_reporte()

