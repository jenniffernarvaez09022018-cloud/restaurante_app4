# Sistema de Gestión - Restaurante App (Semana 8)

**Asignatura:** Programación Orientada a Objetos 

**Estudiante:** Jenniffer Elizabeth Achina Narvaez

## Descripción del Proyecto
Este sistema interactivo por consola permite registrar y listar productos, bebidas y clientes para un restaurante, desarrollado bajo un enfoque modular aplicando los principios SOLID.

## Principios SOLID Aplicados
* **S — Responsabilidad Única (SRP):** Las clases en `modelos` representan datos. La lógica de colecciones está en `servicios/restaurante.py`. La interfaz está en `main.py`.
* **O — Abierto/Cerrado (OCP):** El sistema permite expandir sus tipos de productos agregando subclases (como `Bebida`) sin modificar el servicio `Restaurante`.
* **L — Sustitución de Liskov (LSP):** `Bebida` puede sustituir a `Producto` en las listas y flujos del sistema de manera transparente y polimórfica a través de `mostrar_informacion()`.

