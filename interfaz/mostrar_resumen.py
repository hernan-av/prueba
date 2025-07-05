from db.productos_db import listar_productos
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def mostrar_productos(productos: list):
    tabla = Table(title="📦 Productos disponibles", header_style="bold magenta", show_lines=True)
    tabla.add_column("ID", justify="center")
    tabla.add_column("Nombre")
    tabla.add_column("Categoría ID", justify="center")
    tabla.add_column("Stock", justify="right")
    tabla.add_column("Precio Venta", justify="right")

    for prod in productos:
        tabla.add_row(
            str(prod[0]),
            prod[1],
            str(prod[2]),
            str(prod[4]),
            f"${prod[5]:.2f}"
        )

    console.print(tabla)

def mostrar_proveedores(proveedores: list):
    tabla = Table(title="🏢 Proveedores registrados", header_style="bold blue", show_lines=True)
    tabla.add_column("ID", justify="center")
    tabla.add_column("Nombre")
    tabla.add_column("CUIT")

    for prov in proveedores:
        tabla.add_row(
            str(prov[0]),
            prov[1],
            prov[2]
        )

    console.print(tabla)

def mostrar_categorias(categorias: list):
    tabla = Table(title="🏷️ Categorías existentes", header_style="bold yellow", show_lines=True)
    tabla.add_column("ID", justify="center")
    tabla.add_column("Nombre")

    for cat in categorias:
        tabla.add_row(str(cat[0]), cat[1])

    console.print(tabla)

def mostrar_clientes(clientes: list):
    tabla = Table(title="👤 Clientes registrados", header_style="bold green", show_lines=True)
    tabla.add_column("ID", justify="center")
    tabla.add_column("Nombre")
    tabla.add_column("DNI")

    for cli in clientes:
        tabla.add_row(str(cli[0]), cli[1], cli[2])

    console.print(tabla)

def mostrar_remitos(remitos: list):
    tabla = Table(title="📄 Remitos generados", header_style="bold cyan", show_lines=True)
    tabla.add_column("ID", justify="center")
    tabla.add_column("Fecha")
    tabla.add_column("Proveedor ID", justify="center")

    for rem in remitos:
        tabla.add_row(str(rem[0]), rem[1], str(rem[2]))

    console.print(tabla)

def mostrar_facturas(facturas: list):
    tabla = Table(title="🧾 Facturas generadas", header_style="bold cyan", show_lines=True)
    tabla.add_column("ID", justify="center")
    tabla.add_column("Fecha")
    tabla.add_column("Cliente ID", justify="center")
    tabla.add_column("Total", justify="right")

    for fac in facturas:
        tabla.add_row(
            str(fac[0]),
            fac[1],
            str(fac[2]),
            f"${fac[3]:.2f}"
        )

    console.print(tabla)

def mostrar_resumen_venta(resumen: dict):
    encabezado = Panel.fit(
        f"[bold white]🧾 FACTURA GENERADA[/bold white]\n"
        f"[cyan]ID:[/] {resumen['id_factura']}    "
        f"[green]Fecha:[/] {resumen['fecha']}    "
        f"[magenta]Cliente ID:[/] {resumen['cliente_id']}    "
        f"[bold yellow]Total:[/] ${resumen['total']:.2f}",
        title="✅ Venta registrada", border_style="green"
    )
    console.print(encabezado)

    tabla = Table(title="Detalle de productos vendidos", show_lines=True, header_style="bold cyan")
    tabla.add_column("Producto ID", justify="center")
    tabla.add_column("Cantidad", justify="right")
    tabla.add_column("Precio Unitario", justify="right")
    tabla.add_column("Total línea", justify="right")

    for item in resumen["productos_vendidos"]:
        tabla.add_row(
            str(item["producto_id"]),
            str(item["cantidad"]),
            f"${item['precio_unitario']:.2f}",
            f"${item['total_linea']:.2f}"
        )

    console.print(tabla)

def mostrar_resumen_ingreso(resumen: dict):
    encabezado = Panel.fit(
        f"[bold white]📄 REMITO GENERADO[/bold white]\n"
        f"[cyan]ID:[/] {resumen['id_remito']}    "
        f"[green]Fecha:[/] {resumen['fecha']}    "
        f"[magenta]Proveedor ID:[/] {resumen['proveedor_id']}",
        title="✅ Ingreso registrado", border_style="blue"
    )
    console.print(encabezado)

    tabla = Table(title="Detalle de productos ingresados", show_lines=True, header_style="bold cyan")
    tabla.add_column("Producto ID", justify="center")
    tabla.add_column("Cantidad", justify="right")
    tabla.add_column("Precio Unitario", justify="right")

    for item in resumen["productos_recibidos"]:
        tabla.add_row(
            str(item["producto_id"]),
            str(item["cantidad"]),
            f"${item['precio_unitario']:.2f}"
        )

    console.print(tabla)