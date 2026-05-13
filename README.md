# Sistema Integral de Gestión de Clientes, Servicios y Reservas

Proyecto desarrollado como parte del componente práctico (Fase 4) del curso **Programación (213023)** de la Universidad Nacional Abierta y a Distancia (UNAD).

Se trata de una aplicación orientada a objetos en Python que permite gestionar clientes, servicios (reservas de salas, alquiler de equipos y asesorías especializadas) y reservas, aplicando principios de herencia, polimorfismo, encapsulación y manejo avanzado de excepciones. **No utiliza ningún motor de base de datos**; toda la información se maneja en objetos y listas, y el registro de eventos y errores se guarda únicamente en un archivo de log.

## Características principales

- 🧱 **Arquitectura orientada a objetos** con clases abstractas (`Entidad`, `Servicio`) y derivadas (`Cliente`, `Sala`, `Equipo`, `Asesoria`).
- 🔐 **Validaciones robustas** en datos de clientes, parámetros de servicios y estados de reservas.
- 📦 **Métodos sobrecargados** para el cálculo de costos, permitiendo incluir impuestos, descuentos, seguros u otros parámetros opcionales según el tipo de servicio.
- ⚠️ **Manejo avanzado de excepciones**: excepciones personalizadas, bloques `try/except/else/finally` y encadenamiento de excepciones (`raise ... from`).
- 📝 **Registro de eventos y errores** en `log.txt`, manteniendo la aplicación estable y en ejecución continua ante fallos.
- 🧪 **Simulación de 10 operaciones** completas que demuestran casos exitosos y erróneos (clientes inválidos, servicios no disponibles, reservas canceladas, etc.).

## Requisitos

- Python 3.8 o superior.
- No se requieren librerías externas (solo módulos estándar: `abc`, `re`, `datetime`).

## Cómo ejecutar

1. Clona este repositorio:
   ```bash
   git clone https://github.com/vivianitajaimes21-dev/Fase-4-Componente-practico-Practicas-simuladas.git
   cd Fase-4-Componente-practico-Practicas-simuladas
