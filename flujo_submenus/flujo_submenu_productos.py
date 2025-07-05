from gestor.productos import agregar_producto, editar_producto, borrar_producto, obtener_productos
from gestor.proveedores import obtener_proveedores
from gestor.categorias import obtener_categorias
from interfaz.entrada import pedir_input_con_cancelacion
from interfaz.mostrar_resumen import mostrar_productos, mostrar_categorias, mostrar_proveedores
from interfaz.mensajes import mostrar_error, mostrar_exito
from interfaz.menus import menu_productos
from gestor.busqueda import buscar_producto

def flujo_productos():
    while True:
        opcion = menu_productos()

        if opcion == "1":  # Agregar producto
            nombre = pedir_input_con_cancelacion("Nombre del producto (C para cancelar): ")
            if nombre == "c":
                continue

            categorias = obtener_categorias()
            if not categorias:
                mostrar_error("Primero debes cargar categorías.")
                continue
            mostrar_categorias(categorias)
            entrada_cat = pedir_input_con_cancelacion("ID de categoría (C para cancelar): ")
            if entrada_cat == "c":
                continue
            try:
                categoria_id = int(entrada_cat)
            except ValueError:
                mostrar_error("El ID de categoría debe ser numérico.")
                continue

            proveedores = obtener_proveedores()
            if not proveedores:
                mostrar_error("Primero debes cargar proveedores.")
                continue
            mostrar_proveedores(proveedores)
            entrada_prov = pedir_input_con_cancelacion("ID del proveedor (C para cancelar): ")
            if entrada_prov == "c":
                continue
            try:
                proveedor_id = int(entrada_prov)
            except ValueError:
                mostrar_error("El ID del proveedor debe ser numérico.")
                continue

            entrada_stock = pedir_input_con_cancelacion("Stock inicial (C para cancelar): ")
            if entrada_stock == "c":
                continue
            try:
                stock = int(entrada_stock)
            except ValueError:
                mostrar_error("El stock debe ser un número entero.")
                continue

            entrada_precio = pedir_input_con_cancelacion("Precio unitario (C para cancelar): ")
            if entrada_precio == "c":
                continue
            try:
                precio_unitario = float(entrada_precio)
            except ValueError:
                mostrar_error("El precio debe ser un número válido.")
                continue

            resultado = agregar_producto(nombre, categoria_id, proveedor_id, stock, precio_unitario)
            if resultado.startswith("ok:"):
                mostrar_exito(f"✔️ Producto agregado: {nombre.strip()}")
            else:
                mostrar_error(resultado)

        elif opcion == "2":  # Buscar producto
            valor = pedir_input_con_cancelacion("Ingresá un nombre o ID para buscar (C para cancelar): ")
            if valor == "c":
                continue

            resultados = buscar_producto(valor)
            if resultados:
                mostrar_productos(resultados)
            else:
                mostrar_error("No se encontraron productos que coincidan con la búsqueda.")

        elif opcion == "3":  # Ver todos los productos
            productos = obtener_productos()
            if productos:
                mostrar_productos(productos)
            else:
                mostrar_error("No hay productos registrados.")

        elif opcion == "4":  # Editar producto
            productos = obtener_productos()
            if not productos:
                mostrar_error("No hay productos para editar.")
                continue
            mostrar_productos(productos)

            entrada_id = pedir_input_con_cancelacion("ID del producto a editar (C para cancelar): ")
            if entrada_id == "c":
                continue
            try:
                id_producto = int(entrada_id)
            except ValueError:
                mostrar_error("El ID debe ser numérico.")
                continue

            nuevo_nombre = pedir_input_con_cancelacion("Nuevo nombre (C para cancelar): ")
            if nuevo_nombre == "c":
                continue

            resultado = editar_producto(id_producto, nuevo_nombre.strip())
            if resultado.startswith("ok:"):
                mostrar_exito(f"Producto {id_producto} renombrado a: {nuevo_nombre.strip()}")
            else:
                mostrar_error(resultado)

        elif opcion == "5":  # Eliminar producto
            productos = obtener_productos()
            if not productos:
                mostrar_error("No hay productos para eliminar.")
                continue
            mostrar_productos(productos)

            entrada_id = pedir_input_con_cancelacion("ID del producto a eliminar (C para cancelar): ")
            if entrada_id == "c":
                continue
            try:
                id_producto = int(entrada_id)
            except ValueError:
                mostrar_error("El ID debe ser numérico.")
                continue

            resultado = borrar_producto(id_producto)
            if resultado.startswith("ok:"):
                mostrar_exito(f"Producto ID {id_producto} eliminado correctamente.")
            else:
                mostrar_error(resultado)

        elif opcion == "0":
            break

        else:
            mostrar_error("Opción inválida.")