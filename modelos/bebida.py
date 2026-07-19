from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tipo_envase: str):
        # Hereda de Producto cumpliendo Sustitución de Liskov
        super().__init__(codigo, nombre, categoria, precio)
        self.tipo_envase: str = tipo_envase

    # Sobrescribe aplicando polimorfismo puro
    def mostrar_informacion(self) -> str:
        base_info = super().mostrar_informacion()
        return f"{base_info} | Envase: {self.tipo_envase}"