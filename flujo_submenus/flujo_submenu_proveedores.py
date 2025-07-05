from interfaz.entrada import pedir_input_con_cancelacion
from interfaz.mensajes import mostrar_error, mostrar_exito
from interfaz.mostrar_resumen import mostrar_proveedores
from interfaz.menus import menu_proveedores
from gestor.proveedores import agregar_proveedor, editar_proveedor, borrar_proveedor, obtener_proveedores
from gestor.busqueda import buscar_proveedor

def flujo_proveedores():
    while True:
        opcion = menu_proveedores()

        if opcion == "1":  # Agregar proveedor
            nombre = pedir_input_con_cancelacion("Nombre del proveedor (C para cancelar): ")
            if nombre == "c":
                continue

            telefono = pedir_input_con_cancelacion("Teléfono del proveedor (C para cancelar): ")
            if telefono == "c":
                continue

            email = pedir_input_con_cancelacion("Email del proveedor (C para cancelar): ")
            if email == "c":
                continue

            cuit = pedir_input_con_cancelacion("CUIT del proveedor (C para cancelar): ")
            if cuit == "c":
                continue
            if not cuit.isdigit():
                mostrar_error("El CUIT debe contener solo números.")
                continue

            resultado = agregar_proveedor(nombre, telefono, email, cuit)
            if resultado.startswith("ok:"):
                mostrar_exito(f"Proveedor agregado: {nombre.strip()}")
            else:
                mostrar_error(resultado)

        elif opcion == "2":  # Buscar proveedor
            termino = pedir_input_con_cancelacion("🔍 Ingresá un nombre o ID para buscar (C para cancelar): ")
            if termino == "c":
                continue

            resultados = buscar_proveedor(termino)
            if resultados:
                mostrar_proveedores(resultados)
            else:
                mostrar_error("No se encontraron proveedores que coincidan con la búsqueda.")

        elif opcion == "3":  # Ver todos
            proveedores = obtener_proveedores()
            if proveedores:
                mostrar_proveedores(proveedores)
            else:
                mostrar_error("No hay proveedores registrados.")

        elif opcion == "4":  # Editar proveedor
            proveedores = obtener_proveedores()
            if not proveedores:
                mostrar_error("No hay proveedores para editar.")
                continue
            mostrar_proveedores(proveedores)

            entrada_id = pedir_input_con_cancelacion("ID del proveedor a editar (C para cancelar): ")
            if entrada_id == "c":
                continue
            try:
                id_proveedor = int(entrada_id)
            except ValueError:
                mostrar_error("El ID debe ser numérico.")
                continue

            nuevo_nombre = pedir_input_con_cancelacion("Nuevo nombre (C para cancelar): ")
            if nuevo_nombre == "c":
                continue

            nuevo_telefono = pedir_input_con_cancelacion("Nuevo teléfono (C para cancelar): ")
            if nuevo_telefono == "c":
                continue

            nuevo_email = pedir_input_con_cancelacion("Nuevo email (C para cancelar): ")
            if nuevo_email == "c":
                continue

            nuevo_cuit = pedir_input_con_cancelacion("Nuevo CUIT (C para cancelar): ")
            if nuevo_cuit == "c":
                continue
            if not nuevo_cuit.isdigit():
                mostrar_error("El CUIT debe contener solo números.")
                continue

            resultado = editar_proveedor(id_proveedor, nuevo_nombre, nuevo_telefono, nuevo_email, nuevo_cuit)
            if resultado.startswith("ok:"):
                mostrar_exito(f"Proveedor {id_proveedor} actualizado correctamente.")
            else:
                mostrar_error(resultado)

        elif opcion == "5":  # Eliminar
            proveedores = obtener_proveedores()
            if not proveedores:
                mostrar_error("No hay proveedores para eliminar.")
                continue
            mostrar_proveedores(proveedores)

            entrada_id = pedir_input_con_cancelacion("ID del proveedor a eliminar (C para cancelar): ")
            if entrada_id == "c":
                continue
            try:
                id_proveedor = int(entrada_id)
            except ValueError:
                mostrar_error("El ID debe ser numérico.")
                continue

            resultado = borrar_proveedor(id_proveedor)
            if resultado.startswith("ok:"):
                mostrar_exito(f"🗑️ Proveedor {id_proveedor} eliminado correctamente.")
            else:
                mostrar_error(resultado)

        elif opcion == "0":
            break

        else:
            mostrar_error("Opción inválida.")