Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> """
... Excepciones personalizadas para el sistema de gestión.
... Todas heredan de Exception y permiten encadenamiento.
... """
... 
... class ErrorSistema(Exception):
...     """Clase base para excepciones del sistema."""
...     pass
... 
... class DatosClienteInvalidosError(ErrorSistema):
...     """Se lanza cuando los datos del cliente no son válidos."""
...     pass
... 
... class ServicioInvalidoError(ErrorSistema):
...     """Se lanza al crear o validar un servicio incorrectamente."""
...     pass
... 
... class ServicioNoDisponibleError(ErrorSistema):
...     """El servicio solicitado no está disponible (p.e. sala llena)."""
...     pass
... 
... class ReservaError(ErrorSistema):
...     """Errores relacionados con la manipulación de reservas."""
