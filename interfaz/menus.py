from db.productos_db import listar_productos
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def mostrar_menu_principal() -> str:
    print("\n[bold cyan]=== MENÚ PRINCIPAL ===[/bold cyan]")
    print("1. Ventas")
    print("2. Ingresos")
    print("3. Clientes")
    print("4. Proveedores")
    print("5. Productos")
    print("6. Categorías")
    print("7. Exportación")
    print("0. Salir")
    return input("Seleccioná una opción: ").strip()

def menu_ventas() -> str:
    print("\n[bold green]--- MENÚ DE VENTAS ---[/bold green]")
    print("1. Registrar venta")
    print("2. Buscar facturas")
    print("3. Ver todas las facturas")
    print("0. Volver al menú principal")
    return input("Seleccioná una opción: ").strip()

def menu_ingresos() -> str:
    print("\n[bold blue]--- MENÚ DE INGRESOS ---[/bold blue]")
    print("1. Registrar ingreso")
    print("2. Buscar remitos")
    print("3. Ver todos los remitos")
    print("0. Volver al menú principal")
    return input("Seleccioná una opción: ").strip()

def menu_clientes() -> str:
    print("\n[bold magenta]--- CLIENTES ---[/bold magenta]")
    print("1. Agregar cliente")
    print("2. Buscar cliente")
    print("3. Ver todos los clientes")
    print("4. Editar cliente")
    print("5. Eliminar cliente")
    print("0. Volver")
    return input("Opción: ").strip()

def menu_proveedores() -> str:
    print("\n[bold cyan]--- PROVEEDORES ---[/bold cyan]")
    print("1. Agregar proveedor")
    print("2. Buscar proveedor")
    print("3. Ver todos los proveedores")
    print("4. Editar proveedor")
    print("5. Eliminar proveedor")
    print("0. Volver")
    return input("Opción: ").strip()

def menu_productos() -> str:
    print("\n[bold white]--- PRODUCTOS ---[/bold white]")
    print("1. Agregar producto")
    print("2. Buscar producto")
    print("3. Ver todos los productos")
    print("4. Editar producto")
    print("5. Eliminar producto")
    print("0. Volver")
    return input("Opción: ").strip()

def menu_categorias() -> str:
    print("\n[bold cyan]--- CATEGORÍAS ---[/bold cyan]")
    print("1. Agregar categoría")
    print("2. Ver categorías")
    print("3. Editar categoría")
    print("4. Eliminar categoría")
    print("0. Volver")
    return input("Opción: ").strip()

def menu_exportacion() -> str:
    print("\n[bold green]--- EXPORTACIÓN ---[/bold green]")
    print("1. Exportar remito por ID")
    print("2. Exportar factura por ID")
    print("0. Volver")
    return input("Seleccioná una opción: ").strip()
