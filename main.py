from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def mostrar_menu() -> None:
    print("\n=================================")
    print("      SISTEMA DE RESTAURANTE     ")
    print("=================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("---------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("---------------------------------")
    print("6. Salir")

def ejecutar_sistema() -> None:
    servicio_restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- REGISTRAR PRODUCTO ---")
            codigo = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría: ").strip()
            try:
                precio = float(input("Precio: "))
            except ValueError:
                print("Error: El precio debe ser un número válido.")
                continue

            nuevo_producto = Producto(codigo, nombre, categoria, precio)
            exito = servicio_restaurante.registrar_producto(nuevo_producto)
            if exito:
                print("¡Producto registrado con éxito!")
            else:
                print("Error: Ya existe un producto con ese código.")

        elif opcion == "2":
            print("\n--- REGISTRAR BEBIDA ---")
            codigo = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría: ").strip()
            try:
                precio = float(input("Precio: "))
            except ValueError:
                print("Error: El precio debe ser un número válido.")
                continue
            tipo_envase = input("Tipo de envase (ej. Vidrio): ").strip()

            nueva_bebida = Bebida(codigo, nombre, categoria, precio, tipo_envase)
            exito = servicio_restaurante.registrar_producto(nueva_bebida)
            if exito:
                print("¡Bebida registrada con éxito!")
            else:
                print("Error: Ya existe un producto con ese código.")

        elif opcion == "3":
            print("\n--- REGISTRAR CLIENTE ---")
            identificacion = input("Identificación: ").strip()
            nombre = input("Nombre completo: ").strip()
            correo = input("Correo electrónico: ").strip()

            nuevo_cliente = Cliente(identificacion, nombre, correo)
            exito = servicio_restaurante.registrar_cliente(nuevo_cliente)
            if exito:
                print("¡Cliente registrado con éxito!")
            else:
                print("Error: Ya existe un cliente con esa identificación.")

        elif opcion == "4":
            print("\n--- LISTADO DE PRODUCTOS ---")
            productos = servicio_restaurante.listar_productos()
            if not productos:
                print("No hay productos ni bebidas registrados.")
            else:
                # Aquí ocurre la magia del polimorfismo (Liskov) sin ifs repetidos
                for prod in productos:
                    print(prod.mostrar_informacion())

        elif opcion == "5":
            print("\n--- LISTADO DE CLIENTES ---")
            clientes = servicio_restaurante.listar_clientes()
            if not clientes:
                print("No hay clientes registrados.")
            else:
                for cli in clientes:
                    print(cli.mostrar_informacion())

        elif opcion == "6":
            print("\nSaliendo del sistema... ¡Gracias!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    ejecutar_sistema()