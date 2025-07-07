from db.facturas_db import listar_facturas
from interfaz.mostrar_resumen import mostrar_facturas
from interfaz.entrada import pedir_input_con_cancelacion
from interfaz.mensajes import mostrar_error, mostrar_cancelado, mostrar_exito
from db.generador_pdf import generar_pdf_factura

def exportar_factura_interactivamente():
    facturas = listar_facturas()
    if not facturas:
        mostrar_error("No hay facturas registradas.")
        return

    mostrar_facturas(facturas)

    while True:
        entrada = pedir_input_con_cancelacion("🧾 Ingresá el ID de la factura a exportar (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Exportación de facturas")
            return
        try:
            id_factura = int(entrada)
        except ValueError:
            mostrar_error("El ID debe ser un número.")
            continue
        ids = [f[0] for f in facturas]
        if id_factura not in ids:
            mostrar_error("El ID de factura no existe.")
            continue
        break

    resultado = generar_pdf_factura(id_factura)
    mostrar_exito(resultado)