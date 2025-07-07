# ---------- OPERACIONES DE EXPORTACIÓN ----------

from fpdf import FPDF
import sqlite3
from db.base_datos_db import RUTA_DB
from interfaz.mensajes import mostrar_error, mostrar_exito

import os
RUTA_FACTURAS = "./recursos/documentos/facturas"

def generar_pdf_factura(id_factura: int) -> str:
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()

    # Obtener datos de factura
    cursor.execute("""
        SELECT fecha, cliente_id, total FROM facturas WHERE id_factura = ?
    """, (id_factura,))
    factura = cursor.fetchone()
    if not factura:
        conexion.close()
        mostrar_error("La factura no existe.")

    fecha, cliente_id, total = factura

    cursor.execute("""
        SELECT nombre, telefono, email, dni FROM clientes WHERE id_cliente = ?
    """, (cliente_id,))
    cliente = cursor.fetchone()

    cursor.execute("""
        SELECT fd.producto_id, fd.cantidad, fd.precio_unitario, fd.total_linea, c.nombre
        FROM factura_detalle fd
        JOIN productos p ON fd.producto_id = p.id_producto
        JOIN categorias c ON p.categoria_id = c.id_categoria
        WHERE fd.factura_id = ?
    """, (id_factura,))
    detalles = cursor.fetchall()

    conexion.close()

    # Crear PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Factura Nº {id_factura}", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Fecha: {fecha}", ln=True)
    pdf.cell(200, 10, txt=f"Cliente: {cliente[0]} - {cliente[1]} - {cliente[2]} - DNI: {cliente[3]}", ln=True)
    pdf.ln(5)
    pdf.cell(200, 10, txt="Detalle de productos:", ln=True)

    for prod_id, cantidad, precio, total_linea, categoria in detalles:
        pdf.cell(200, 10, txt=f"- ID {prod_id} | {categoria} | {cantidad} unidades | ${precio:.2f} c/u | Total: ${total_linea:.2f}", ln=True)

    pdf.cell(200, 10, txt=f"\nTOTAL FACTURA: ${total:.2f}", ln=True)

    os.makedirs(RUTA_FACTURAS, exist_ok=True)
    ruta = os.path.join(RUTA_FACTURAS, f"factura_{id_factura}.pdf")

    pdf.output(ruta)
    mostrar_exito(f"📄 Factura guardada en: {ruta}")