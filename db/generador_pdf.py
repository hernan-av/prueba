# ---------- OPERACIONES DE EXPORTACIÓN ----------

from fpdf import FPDF
import sqlite3
from db.base_datos_db import RUTA_DB
from interfaz.mensajes import mostrar_error, mostrar_exito

import os
RUTA_FACTURAS = "./recursos/documentos/facturas"
RUTA_REMITOS = "./recursos/documentos/remitos"

def generar_pdf_remito(id_remito: int) -> str:
    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()

    # Obtener datos del remito
    cursor.execute("""
        SELECT fecha, proveedor_id FROM remitos WHERE id_remito = ?
    """, (id_remito,))
    remito = cursor.fetchone()
    if not remito:
        conexion.close()
        mostrar_error("El remito no existe.")

    fecha, proveedor_id = remito

    cursor.execute("""
        SELECT nombre, telefono, email, cuit FROM proveedores WHERE id_proveedor = ?
    """, (proveedor_id,))
    proveedor = cursor.fetchone()

    cursor.execute("""
        SELECT rd.producto_id, rd.cantidad, rd.precio_unitario, c.nombre
        FROM remito_detalle rd
        JOIN productos p ON rd.producto_id = p.id_producto
        JOIN categorias c ON p.categoria_id = c.id_categoria
        WHERE rd.remito_id = ?
    """, (id_remito,))
    detalles = cursor.fetchall()

    conexion.close()

    # Crear PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Remito Nº {id_remito}", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Fecha: {fecha}", ln=True)
    pdf.cell(200, 10, txt=f"Proveedor: {proveedor[0]} - {proveedor[1]} - {proveedor[2]} - CUIT: {proveedor[3]}", ln=True)
    pdf.ln(5)
    pdf.cell(200, 10, txt="Detalle de productos:", ln=True)

    for prod_id, cantidad, precio, categoria in detalles:
        pdf.cell(200, 10, txt=f"- ID {prod_id} | {categoria} | {cantidad} unidades | ${precio:.2f} c/u", ln=True)

    os.makedirs(RUTA_REMITOS, exist_ok=True)
    ruta = os.path.join(RUTA_REMITOS, f"remito_{id_remito}.pdf")
    pdf.output(ruta)
    mostrar_exito(f"📄 Remito guardado en: {ruta}")

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