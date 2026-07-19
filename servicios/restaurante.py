from typing import List
from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self):
        # Una sola lista para productos y bebidas juntos, como pide la tarea
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []

    def registrar_producto(self, producto: Producto) -> bool:
        for p in self._productos:
            if p.codigo == producto.codigo:
                return False
        self._productos.append(producto)
        return True

    def registrar_cliente(self, cliente: Cliente) -> bool:
        for c in self._clientes:
            if c.identificacion == cliente.identificacion:
                return False
        self._clientes.append(cliente)
        return True

    def listar_productos(self) -> List[Producto]:
        return self._productos

    def listar_clientes(self) -> List[Cliente]:
        return self._clientes