Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> """
... Funciones para registro de eventos y errores en archivo log.txt.
... """
... from datetime import datetime
... 
... ARCHIVO_LOG = "log.txt"
... 
... def registrar_log(mensaje: str, nivel: str = "INFO") -> None:
...     """
...     Añade una entrada al archivo de log con timestamp y nivel.
...     """
...     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
...     linea = f"[{timestamp}] [{nivel}] {mensaje}\n"
...     with open(ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
