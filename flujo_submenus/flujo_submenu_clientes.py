from interfaz.entrada import pedir_input_con_cancelacion
from interfaz.mensajes import mostrar_exito, mostrar_error
from interfaz.mostrar_resumen import mostrar_clientes
from interfaz.menus import menu_clientes
from gestor.clientes import agregar_cliente, editar_cliente, borrar_cliente,obtener_clientes
from gestor.busqueda import buscar_cliente

def flujo_clientes():
    while True:
        opcion = menu_clientes()

        if opcion == "1":  # Agregar cliente
            nombre = pedir_input_con_cancelacion("Nombre del cliente (C para cancelar): ")
            if nombre == "c":
                continue

            telefono = pedir_input_con_cancelacion("Teléfono del cliente (C para cancelar): ")
            if telefono == "c":
                continue

            email = pedir_input_con_cancelacion("Email del cliente (C para cancelar): ")
            if email == "c":
                continue

            dni = pedir_input_con_cancelacion("DNI del cliente (C para cancelar): ")
            if dni == "c":
                continue
            if not dni.isdigit():
                mostrar_error("El DNI debe contener solo números.")
                continue

            resultado = agregar_cliente(nombre, telefono, email, dni)
            if resultado.startswith("ok:"):
                mostrar_exito(f"Cliente agregado: {nombre.strip()}")
            else:
                mostrar_error(resultado)

        elif opcion == "2":  # Buscar cliente
            valor = pedir_input_con_cancelacion("Ingresá un nombre o ID para buscar (C para cancelar): ")
            if valor == "c":
                continue

            resultados = buscar_cliente(valor)
            if resultados:
                mostrar_clientes(resultados)
            else:
                mostrar_error("No se encontraron clientes que coincidan con la búsqueda.")

        elif opcion == "3":  # Ver todos
            clientes = obtener_clientes()
            if clientes:
                mostrar_clientes(clientes)
            else:
                mostrar_error("No hay clientes registrados.")

        elif opcion == "4":  # Editar cliente
            clientes = obtener_clientes()
            if not clientes:
                mostrar_error("No hay clientes para editar.")
                continue
            mostrar_clientes(clientes)

            entrada_id = pedir_input_con_cancelacion("Ingresá el ID del cliente a editar (C para cancelar): ")
            if entrada_id == "c":
                continue
            try:
                id_cliente = int(entrada_id)
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

            nuevo_dni = pedir_input_con_cancelacion("Nuevo DNI (C para cancelar): ")
            if nuevo_dni == "c":
                continue
            if not nuevo_dni.isdigit():
                mostrar_error("El DNI debe contener solo números.")
                continue

            resultado = editar_cliente(id_cliente, nuevo_nombre, nuevo_telefono, nuevo_email, nuevo_dni)
            if resultado.startswith("ok:"):
                mostrar_exito(f"Cliente {id_cliente} actualizado correctamente.")
            else:
                mostrar_error(resultado)

        elif opcion == "5":  # Eliminar cliente
            clientes = obtener_clientes()
            if not clientes:
                mostrar_error("No hay clientes para eliminar.")
                continue
            mostrar_clientes(clientes)

            entrada_id = pedir_input_con_cancelacion("Ingresá el ID del cliente a eliminar (C para cancelar): ")
            if entrada_id == "c":
                continue
            try:
                id_cliente = int(entrada_id)
            except ValueError:
                mostrar_error("El ID debe ser numérico.")
                continue

            resultado = borrar_cliente(id_cliente)
            if resultado.startswith("ok:"):
                mostrar_exito(f"Cliente ID {id_cliente} eliminado correctamente.")
            else:
                mostrar_error(resultado)

        elif opcion == "0":
            break

        else:
            mostrar_error("Opción inválida.")