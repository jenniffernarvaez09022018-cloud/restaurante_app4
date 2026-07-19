class Cliente:
    def __init__(self, identificacion: str, nombre: str, correo: str):
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def mostrar_informacion(self) -> str:
        return f"[CLIENTE] Identificación: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"