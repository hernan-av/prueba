from interfaz.entrada import pedir_input_con_cancelacion
from interfaz.mensajes import mostrar_exito, mostrar_error
from interfaz.mostrar_resumen import mostrar_facturas
from interfaz.menus import menu_ventas
from gestor.ventas import registrar_venta, obtener_facturas
from gestor.busqueda import buscar_factura

def flujo_ventas():
    while True:
        opcion = menu_ventas()

        if opcion == "1":  # Registrar venta
            resultado = registrar_venta()
            if resultado.startswith("ok:"):
                mostrar_exito("✔️ Venta registrada con éxito.")
            else:
                mostrar_error(resultado)

        elif opcion == "2":  # Buscar factura
            valor = pedir_input_con_cancelacion("🔍 Ingresá un ID o fecha (aaaa-mm-dd) para buscar (C para cancelar): ")
            if valor == "c":
                continue

            resultados = buscar_factura(valor)
            if resultados:
                mostrar_facturas(resultados)
            else:
                mostrar_error("No se encontraron facturas que coincidan con la búsqueda.")

        elif opcion == "3":  # Ver todas las facturas
            facturas = obtener_facturas()
            if facturas:
                mostrar_facturas(facturas)
            else:
                mostrar_error("No hay facturas registradas.")

        elif opcion == "0":
            break

        else:
            mostrar_error("Opción inválida.")