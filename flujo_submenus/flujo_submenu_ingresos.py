from interfaz.entrada import pedir_input_con_cancelacion
from interfaz.mensajes import mostrar_exito, mostrar_error
from interfaz.mostrar_resumen import mostrar_remitos
from interfaz.menus import menu_ingresos
from gestor.ingresos import registrar_ingreso, obtener_remitos
from gestor.busqueda import buscar_remito

def flujo_ingresos():
    while True:
        opcion = menu_ingresos()

        if opcion == "1":  # Registrar ingreso
            resultado = registrar_ingreso()
            if resultado.startswith("ok:"):
                mostrar_exito("📥 Ingreso registrado correctamente.")
            else:
                mostrar_error(resultado)

        elif opcion == "2":  # Buscar remito
            valor = pedir_input_con_cancelacion("🔍 Ingresá un ID o fecha (aaaa-mm-dd) para buscar (C para cancelar): ")
            if valor == "c":
                continue

            resultados = buscar_remito(valor)
            if resultados:
                mostrar_remitos(resultados)
            else:
                mostrar_error("No se encontraron remitos que coincidan con la búsqueda.")

        elif opcion == "3":  # Ver todos los remitos
            remitos = obtener_remitos()
            if remitos:
                mostrar_remitos(remitos)
            else:
                mostrar_error("No hay remitos registrados.")

        elif opcion == "0":
            break

        else:
            mostrar_error("Opción inválida.")