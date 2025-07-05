
from gestor.categorias import agregar_categoria, editar_categoria, borrar_categoria, obtener_categorias
from interfaz.entrada import pedir_input_con_cancelacion
from interfaz.mensajes import mostrar_error, mostrar_exito
from interfaz.mostrar_resumen import mostrar_categorias
from interfaz.menus import menu_categorias

def flujo_categorias():
    while True:
        opcion = menu_categorias()

        if opcion == "1":
            nombre = pedir_input_con_cancelacion("Ingresá el nombre de la nueva categoría (c para cancelar): ")
            if nombre == "c":
                continue

            resultado = agregar_categoria(nombre)
            if resultado.startswith("ok:"):
                mostrar_exito("Categoría agregada: " + nombre.strip())
            else:
                mostrar_error(resultado)

        elif opcion == "2":
            categorias = obtener_categorias()
            if categorias:
                mostrar_categorias(categorias)
            else:
                mostrar_error("No hay categorías registradas.")

        elif opcion == "3":
            categorias = obtener_categorias()
            if not categorias:
                mostrar_error("No hay categorías para editar.")
                continue

            mostrar_categorias(categorias)

            entrada = pedir_input_con_cancelacion("Ingresá el ID de la categoría a editar (c para cancelar): ")
            if entrada == "c":
                continue

            try:
                id_categoria = int(entrada)
            except ValueError:
                mostrar_error("El ID debe ser un número.")
                continue

            nuevo_nombre = pedir_input_con_cancelacion("Ingresá el nuevo nombre (c para cancelar): ")
            if nuevo_nombre == "c":
                continue

            resultado = editar_categoria(id_categoria, nuevo_nombre)
            if resultado.startswith("ok:"):
                mostrar_exito(f"Categoría {id_categoria} modificada a: {nuevo_nombre.strip()}")
            else:
                mostrar_error(resultado)

        elif opcion == "4":
            categorias = obtener_categorias()
            if not categorias:
                mostrar_error("No hay categorías para eliminar.")
                continue

            mostrar_categorias(categorias)

            entrada = pedir_input_con_cancelacion("Ingresá el ID de la categoría a eliminar (c para cancelar): ")
            if entrada == "c":
                continue

            try:
                id_categoria = int(entrada)
            except ValueError:
                mostrar_error("El ID debe ser un número.")
                continue

            resultado = borrar_categoria(id_categoria)
            if resultado.startswith("ok:"):
                mostrar_exito(f"Categoría con ID {id_categoria} eliminada correctamente.")
            else:
                mostrar_error(resultado)

        elif opcion == "0":
            break

        else:
            mostrar_error("Opción inválida.")