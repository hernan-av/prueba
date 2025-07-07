from db.facturas_db import listar_facturas
from db.remitos_db import listar_remitos
from interfaz.mostrar_resumen import mostrar_facturas, mostrar_remitos
from interfaz.entrada import pedir_input_con_cancelacion
from interfaz.mensajes import mostrar_error, mostrar_cancelado, mostrar_exito
from db.generador_pdf import generar_pdf_factura, generar_pdf_remito

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



def exportar_remito_interactivamente():
    remitos = listar_remitos()
    if not remitos:
        mostrar_error("No hay remitos registrados.")
        return

    mostrar_remitos(remitos)

    while True:
        entrada = pedir_input_con_cancelacion("📄 Ingresá el ID del remito a exportar (C para cancelar): ")
        if entrada.lower() == "c":
            mostrar_cancelado("Exportación de remitos")
            return
        try:
            id_remito = int(entrada)
        except ValueError:
            mostrar_error("El ID debe ser un número.")
            continue
        ids = [r[0] for r in remitos]
        if id_remito not in ids:
            mostrar_error("El ID de remito no existe.")
            continue
        break

    resultado = generar_pdf_remito(id_remito)
    mostrar_exito(resultado)