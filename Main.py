Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
"""
Simulación de 10 operaciones para demostrar la robustez del sistema.
"""
from entidades import Cliente
from servicios import Sala, Equipo, Asesoria
from reservas import Reserva
from excepciones import DatosClienteInvalidosError, ServicioInvalidoError, ServicioNoDisponibleError, ReservaError
from logger import registrar_log

def simular():
    registrar_log("=== INICIO DE SIMULACIÓN ===")
    
    # 1. Registro correcto de cliente
    try:
        c1 = Cliente("C001", "Laura Gómez", "laura@example.com", "3001234567")
        c1.validar()
        print("1. Cliente válido creado:", c1)
    except Exception as e:
        print(f"1. Error inesperado: {e}")
        registrar_log(f"Op1 falló: {e}", "ERROR")

    # 2. Registro inválido (email incorrecto)
    try:
        c2 = Cliente("C002", "Carlos Pérez", "carlos@@com", "3109876543")
        c2.validar()
        print("2. Este mensaje no debería verse.")
    except DatosClienteInvalidosError as e:
        print("2. Cliente inválido capturado:", e)
        registrar_log(f"Op2: cliente inválido: {e}", "ERROR")

    # 3. Otro cliente válido
    try:
        c3 = Cliente("C003", "Ana Ruiz", "ana.ruiz@mail.co", "+573001112233")
        c3.validar()
        print("3. Cliente válido creado:", c3)
    except Exception as e:
        print(f"3. Error: {e}")

    # 4. Creación correcta de un servicio (Sala)
    try:
        s1 = Sala("S001", "Sala Magna", 100.0, capacidad=30)
        s1.validar_parametros(personas=10)
        print("4. Servicio de sala creado:", s1)
    except Exception as e:
        print(f"4. Error: {e}")

    # 5. Creación incorrecta de servicio (Equipo sin datos completos – omitiendo intento de crear Equipo sin parámetros obligatorios)
    # Simulamos omisión de un campo obligatorio: capacidad = -5 (debe ser positiva)
...     try:
...         s2 = Sala("S002", "Sala Chica", 50.0, capacidad=-5)  # inválido
...         s2.validar_parametros(personas=2)
...         print("5. Esto no debería aparecer.")
...     except ServicioInvalidoError as e:
...         print("5. Servicio inválido detectado:", e)
...         registrar_log(f"Op5: {e}", "ERROR")
... 
...     # 6. Reserva exitosa
...     try:
...         r1 = Reserva(c1, s1, duracion=3)
...         r1.confirmar(personas=10)
...         costo = r1.procesar(impuesto=16, descuento=5)
...         print(f"6. Reserva exitosa. Costo: ${costo:.2f}")
...     except Exception as e:
...         print(f"6. Falló la reserva: {e}")
... 
...     # 7. Reserva fallida: sala no disponible (marcamos como no disponible)
...     s1.disponible = False
...     try:
...         r2 = Reserva(c3, s1, duracion=2)
...         r2.confirmar(personas=5)
...         print("7. Esto no debería verse.")
...     except ReservaError as e:
...         print("7. Reserva fallida correctamente:", e)
...         registrar_log(f"Op7: reserva fallida: {e}", "ERROR")
... 
...     # Volver a poner disponible la sala
...     s1.disponible = True
... 
...     # 8. Cancelar reserva existente
...     try:
...         r1.cancelar()
...         print("8. Reserva cancelada:", r1)
...     except Exception as e:
...         print(f"8. Error al cancelar: {e}")
... 
...     # 9. Intentar confirmar una reserva ya cancelada (manejo con try/except/else)
    try:
        r1.confirmar(personas=5)
    except ReservaError as e:
        print("9. No se puede confirmar reserva cancelada:", e)
        registrar_log(f"Op9: {e}", "ERROR")
    else:
        print("9. Confirmación inesperada.")

    # 10. Uso de try/except/finally con servicio de tipo Asesoria
    a1 = Asesoria("A001", "Consultoría TI", 150.0, nivel="senior")
    try:
        r3 = Reserva(c3, a1, duracion=4)
        r3.confirmar(complejidad="alta")
        costo = r3.procesar(impuesto=19)
        print(f"10. Asesoría procesada. Costo: ${costo:.2f}")
    except Exception as e:
        print(f"10. Error: {e}")
        registrar_log(f"Op10: {e}", "ERROR")
    finally:
        registrar_log("=== FIN DE SIMULACIÓN ===")
        print("Simulación terminada. Revisa log.txt para el registro de eventos.")

if __name__ == "__main__":
