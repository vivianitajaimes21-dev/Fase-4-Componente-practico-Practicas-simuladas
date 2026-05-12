Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> """
... Clase abstracta Entidad y su subclase Cliente.
... """
... from abc import ABC, abstractmethod
... import re
... from excepciones import DatosClienteInvalidosError
... from logger import registrar_log
... 
... class Entidad(ABC):
...     """Clase abstracta que define la interfaz común para todas las entidades del sistema."""
...     
...     def __init__(self, identificador: str, nombre: str):
...         self.identificador = identificador
...         self.nombre = nombre
... 
...     @abstractmethod
...     def validar(self) -> bool:
...         """
...         Método abstracto para validar los datos de la entidad.
...         Retorna True si es válida, lanza excepción en caso contrario.
...         """
...         pass
... 
...     def __str__(self):
...         return f"{self.__class__.__name__}(ID: {self.identificador}, Nombre: {self.nombre})"
... 
... 
... class Cliente(Entidad):
...     """
...     Representa un cliente con validación estricta de datos personales.
...     """
...     def __init__(self, identificador: str, nombre: str, email: str, telefono: str):
...         super().__init__(identificador, nombre)
...         self._email = email        # encapsulado
        self._telefono = telefono  # encapsulado

    # Propiedades para acceso controlado
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, nuevo_email):
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", nuevo_email):
            raise DatosClienteInvalidosError(f"Email inválido: {nuevo_email}")
        self._email = nuevo_email

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        if not re.match(r"^\+?\d{7,15}$", nuevo_telefono):
            raise DatosClienteInvalidosError(f"Teléfono inválido: {nuevo_telefono}")
        self._telefono = nuevo_telefono

    def validar(self) -> bool:
        """
        Valida todos los campos del cliente. Lanza DatosClienteInvalidosError si falla.
        """
        if not self.identificador or not self.nombre:
            raise DatosClienteInvalidosError("Identificador y nombre son obligatorios.")
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", self._email):
            raise DatosClienteInvalidosError(f"Formato de email incorrecto: {self._email}")
        if not re.match(r"^\+?\d{7,15}$", self._telefono):
            raise DatosClienteInvalidosError(f"Formato de teléfono incorrecto: {self._telefono}")
        registrar_log(f"Cliente validado correctamente: {self.identificador}")
        return True

    def __str__(self):
