# ---------- GESTIÓN DE EXPORTACIÓN ----------

from fpdf import FPDF
import os
from db.facturas_db import obtener_detalle_venta
from db.facturas_db import listar_facturas
from interfaz.mostrar_resumen import mostrar_facturas
from interfaz.entrada import pedir_input_con_cancelacion
from interfaz.mensajes import mostrar_error, mostrar_cancelado, mostrar_exito

RUTA_FACTURAS = "./facturas_exportadas"

def generar_pdf_factura(id_factura: int) -> str:
    detalle = obtener_detalle_venta(id_factura)

    # Extraer info de cabecera desde la primera fila
    (
        _, fecha, cliente_id, nombre_cliente, email, dni,
        _, _, _, _, _, _, total_factura
    ) = detalle[0]

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Encabezado de factura
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(190, 10, f"FACTURA Nº {id_factura}", ln=True, align="C")

    pdf.set_font("Arial", size=11)
    pdf.cell(190, 8, f"Fecha: {fecha}", ln=True)
    pdf.cell(190, 8, f"Cliente: {nombre_cliente} (ID: {cliente_id})", ln=True)
    pdf.cell(190, 8, f"Email: {email}", ln=True)
    pdf.cell(190, 8, f"DNI: {dni}", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 8, "Detalle de Productos", ln=True)

    # Encabezado de tabla
    pdf.set_fill_color(230, 230, 230)
    pdf.set_font("Arial", style="B", size=10)
    pdf.cell(50, 8, "Producto", border=1, fill=1)
    pdf.cell(40, 8, "Categoría", border=1, fill=1)
    pdf.cell(25, 8, "Cantidad", border=1, fill=1, align="C")
    pdf.cell(35, 8, "Precio Unit.", border=1, fill=1, align="R")
    pdf.cell(40, 8, "Subtotal", border=1, ln=True, fill=1, align="R")

    # Filas
    pdf.set_font("Arial", size=10)
    for row in detalle:
        _, _, _, _, _, _, _, producto, categoria, cantidad, precio_unitario, total_linea, _ = row
        pdf.cell(50, 8, producto, border=1)
        pdf.cell(40, 8, categoria, border=1)
        pdf.cell(25, 8, str(cantidad), border=1, align="C")
        pdf.cell(35, 8, f"${precio_unitario:.2f}", border=1, align="R")
        pdf.cell(40, 8, f"${total_linea:.2f}", border=1, ln=True, align="R")

    # Total
    pdf.ln(4)
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(150, 8, "TOTAL FACTURA:", align="R")
    pdf.set_font("Arial", style="", size=12)
    pdf.cell(40, 8, f"${total_factura:.2f}", ln=True, align="R")

    # Guardado
    os.makedirs(RUTA_FACTURAS, exist_ok=True)
    ruta = os.path.join(RUTA_FACTURAS, f"factura_{id_factura}.pdf")
    pdf.output(ruta)

    return ruta

def exportar_factura_interactivamente():
    facturas = listar_facturas()
    if not facturas:
        mostrar_error("No hay facturas registradas.")
        return

    mostrar_facturas(facturas)

    while True:
        entrada = pedir_input_con_cancelacion("Ingresá el ID de la factura a exportar (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Exportación de facturas")
            return
        try:
            id_factura = int(entrada)
        except ValueError:
            mostrar_error("El ID debe ser un número.")
            continue
        ids = []
        for factura in facturas:
            ids.append(factura[0])
        if id_factura not in ids:
            mostrar_error("El ID de factura no existe.")
            continue
        break

    resultado = generar_pdf_factura(id_factura)
    mostrar_exito(f"Factura guardada en: {resultado}")
