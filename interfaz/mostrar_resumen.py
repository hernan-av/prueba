from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from interfaz.mensajes import mostrar_error
from db.facturas_db import obtener_detalle_venta

console = Console()

def mostrar_productos(productos: list):
    tabla = Table(title="Productos disponibles", header_style="bold magenta", show_lines=True)
    tabla.add_column("ID")
    tabla.add_column("Nombre")
    tabla.add_column("Categoría")
    tabla.add_column("Proveedor")
    tabla.add_column("Stock")
    tabla.add_column("Precio Venta")

    for prod in productos:
        tabla.add_row(
            str(prod[0]),
            str(prod[1]),
            str(prod[2]),
            str(prod[3]),
            str(prod[4]),
            f"${prod[5]:.2f}"
        )        
    console.print(tabla)

def mostrar_proveedores(proveedores: list):
    tabla = Table(title="Proveedores registrados", header_style="bold blue", show_lines=True)
    tabla.add_column("ID")
    tabla.add_column("Nombre")
    tabla.add_column("Teléfono")
    tabla.add_column("Email")
    tabla.add_column("CUIT")

    for prov in proveedores:
        tabla.add_row(
            str(prov[0]),
            prov[1],
            prov[2],
            prov[3],
            prov[4]
        )

    console.print(tabla)

def mostrar_categorias(categorias: list):
    tabla = Table(title="Categorías existentes", header_style="bold yellow", show_lines=True)
    tabla.add_column("ID")
    tabla.add_column("Nombre")

    for cat in categorias:
        tabla.add_row(str(cat[0]), cat[1])

    console.print(tabla)

def mostrar_clientes(clientes: list):
    tabla = Table(title="Clientes registrados", header_style="bold green", show_lines=True)
    tabla.add_column("ID")
    tabla.add_column("Nombre")
    tabla.add_column("Teléfono")
    tabla.add_column("Email")
    tabla.add_column("DNI")

    for cli in clientes:
        tabla.add_row(str(cli[0]), cli[1], cli[2], cli[3], cli[4])

    console.print(tabla)

def mostrar_facturas(facturas: list):
    if not facturas:
        mostrar_error("No hay facturas registradas.")
        return

    tabla = Table(title="Facturas generadas", header_style="bold cyan", show_lines=True)
    tabla.add_column("ID", justify="center")
    tabla.add_column("Fecha")
    tabla.add_column("Cliente", justify="center")
    tabla.add_column("Total", justify="right")

    for fac in facturas:
        tabla.add_row(
            str(fac[0]),
            fac[1],
            str(fac[2]),
            f"${fac[3]:.2f}"
        )

    console.print(tabla)

def mostrar_resumen_venta(id_factura: int):
    detalle = obtener_detalle_venta(id_factura)
    if not detalle:
        mostrar_error("No se encontró la factura especificada.")
        return

    # Extraer datos generales desde la primera fila
    (
        _, fecha, cliente_id, cliente_nombre, email, dni,
        _, _, _, _, _, _, total_factura
    ) = detalle[0]

    encabezado = Panel.fit(
        f"[bold white]🧾 FACTURA GENERADA[/bold white]\n"
        f"[cyan]ID:[/] {id_factura}    "
        f"[green]Fecha:[/] {fecha}\n"
        f"[magenta]Cliente:[/] {cliente_nombre} (ID: {cliente_id})\n"
        f"[blue]Email:[/] {email}    [yellow]DNI:[/] {dni}\n"
        f"[bold yellow]TOTAL:[/] ${total_factura:.2f}",
        title="✅ Venta registrada",
        border_style="green"
    )
    console.print(encabezado)

    tabla = Table(title="📦 Detalle de productos vendidos", show_lines=True, header_style="bold cyan")
    tabla.add_column("Producto", style="white", justify="left")
    tabla.add_column("Categoría", style="dim", justify="left")
    tabla.add_column("Cantidad", justify="center")
    tabla.add_column("Precio Unitario", justify="right")
    tabla.add_column("Total Línea", justify="right")

    for fila in detalle:
        producto = fila[7]
        categoria = fila[8]
        cantidad = fila[9]
        precio_unitario = fila[10]
        total_linea = fila[11]

        tabla.add_row(
            producto,
            categoria,
            str(cantidad),
            f"${precio_unitario:.2f}",
            f"${total_linea:.2f}"
        )

    console.print(tabla)

