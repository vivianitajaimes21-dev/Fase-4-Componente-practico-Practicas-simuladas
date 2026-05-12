Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
"""
Servicio abstracto y tres servicios concretos: Sala, Equipo, Asesoria.
"""
from abc import abstractmethod
from entidades import Entidad
from excepciones import ServicioInvalidoError, ServicioNoDisponibleError
from logger import registrar_log

class Servicio(Entidad):
    """
    Clase abstracta para todos los servicios ofrecidos.
    """
    def __init__(self, identificador: str, nombre: str, costo_base: float, **kwargs):
        super().__init__(identificador, nombre)
        self.costo_base = costo_base
        self.disponible = True
        self.parametros_extra = kwargs  # atributos específicos (capacidad, marca, nivel, etc.)

    @abstractmethod
    def calcular_costo(self, duracion: int, **opciones) -> float:
        """
        Calcula el costo del servicio. Admite parámetros opcionales:
        - impuesto (float): porcentaje de impuesto a aplicar (por defecto 0)
        - descuento (float): descuento fijo o porcentaje según implementación
        """
        pass

    @abstractmethod
    def describir_servicio(self) -> str:
        """Retorna una descripción textual del servicio."""
        pass

    @abstractmethod
    def validar_parametros(self, **kwargs) -> bool:
        """
        Verifica que los parámetros necesarios para usar el servicio sean válidos.
        Ej: capacidad de la sala, stock de equipos, etc.
        """
...         pass
... 
...     def __str__(self):
...         return f"{self.nombre} (ID {self.identificador}) - Disponible: {self.disponible}"
... 
... 
... class Sala(Servicio):
...     """
...     Reserva de salas con capacidad máxima.
...     costo_base: precio por hora.
...     kwargs: capacidad (int)
...     """
...     def __init__(self, identificador: str, nombre: str, costo_base: float, capacidad: int):
...         super().__init__(identificador, nombre, costo_base, capacidad=capacidad)
... 
...     @property
...     def capacidad(self):
...         return self.parametros_extra.get("capacidad", 0)
... 
...     def calcular_costo(self, duracion: int, impuesto: float = 0.0, descuento: float = 0.0, personas: int = 1) -> float:
...         """
...         Costo = (costo_base * duracion) + extra por persona si excede la mitad de capacidad.
...         Luego se aplica impuesto y descuento.
...         """
...         if duracion <= 0:
...             raise ServicioInvalidoError("La duración debe ser mayor a cero.")
...         costo = self.costo_base * duracion
...         if personas > self.capacidad / 2:
...             costo += (personas - self.capacidad // 2) * 5.0  # extra
...         # aplicamos impuesto y descuento
...         costo_con_impuesto = costo * (1 + impuesto / 100)
...         costo_final = costo_con_impuesto - descuento
...         return max(costo_final, 0.0)
... 
...     def describir_servicio(self) -> str:
...         return f"Sala {self.nombre}: capacidad {self.capacidad} personas, costo base ${self.costo_base}/hora."

    def validar_parametros(self, **kwargs) -> bool:
        personas = kwargs.get("personas", 1)
        if personas > self.capacidad:
            raise ServicioNoDisponibleError(f"La sala solo admite {self.capacidad} personas. Solicitadas: {personas}")
        if not self.disponible:
            raise ServicioNoDisponibleError(f"La sala {self.nombre} no está disponible en este momento.")
        registrar_log(f"Sala {self.identificador} validada: {personas} personas.")
        return True


class Equipo(Servicio):
    """
    Alquiler de equipos. costo_base: precio por día.
    kwargs: deposito (float), marca (str)
    """
    def __init__(self, identificador: str, nombre: str, costo_base: float, deposito: float, marca: str = ""):
        super().__init__(identificador, nombre, costo_base, deposito=deposito, marca=marca)

    def calcular_costo(self, duracion: int, impuesto: float = 0.0, descuento: float = 0.0, seguro: bool = False) -> float:
        """
        Costo diario * duración + depósito. Si seguro=True, añade 10% del costo.
        """
        if duracion <= 0:
            raise ServicioInvalidoError("La duración (días) debe ser positiva.")
        costo = self.costo_base * duracion + self.parametros_extra["deposito"]
        if seguro:
            costo += 0.1 * self.costo_base * duracion
        costo *= (1 + impuesto / 100)
        costo -= descuento
        return max(costo, 0.0)

    def describir_servicio(self) -> str:
        return f"Equipo {self.nombre} ({self.parametros_extra.get('marca','')}), costo ${self.costo_base}/día, depósito ${self.parametros_extra['deposito']}."

    def validar_parametros(self, **kwargs) -> bool:
        if not self.disponible:
            raise ServicioNoDisponibleError(f"El equipo {self.nombre} no está disponible.")
        registrar_log(f"Equipo {self.identificador} validado correctamente.")
        return True


class Asesoria(Servicio):
    """
    Asesorías especializadas. costo_base: tarifa por sesión.
    kwargs: nivel (junior, senior, experto)
    """
    def __init__(self, identificador: str, nombre: str, costo_base: float, nivel: str = "junior"):
        super().__init__(identificador, nombre, costo_base, nivel=nivel)

    def calcular_costo(self, duracion: int, impuesto: float = 0.0, descuento: float = 0.0, complejidad: str = "media") -> float:
        """
        Costo = costo_base * duracion. Si complejidad='alta', añade 25%.
        """
        if duracion <= 0:
            raise ServicioInvalidoError("La duración (horas) debe ser positiva.")
        costo = self.costo_base * duracion
        if complejidad == "alta":
            costo *= 1.25
        costo *= (1 + impuesto / 100)
        costo -= descuento
        return max(costo, 0.0)

    def describir_servicio(self) -> str:
        return f"Asesoría {self.nombre} (nivel {self.parametros_extra['nivel']}), costo ${self.costo_base}/hora."

    def validar_parametros(self, **kwargs) -> bool:
        if not self.disponible:
            raise ServicioNoDisponibleError(f"La asesoría {self.nombre} no está disponible.")
        registrar_log(f"Asesoría {self.identificador} validada.")
