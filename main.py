from interfaz.menus import (
    mostrar_menu_principal,
    menu_ventas,
    menu_clientes,
    menu_proveedores,
    menu_productos,
    menu_categorias,
)

from gestor.ventas import procesar_venta_interactiva, imprimir_detalle_venta
from gestor.clientes import (
    agregar_cliente,
    mostrar_todos_los_clientes,
    editar_cliente,
    borrar_cliente,
)
from gestor.proveedores import (
    agregar_proveedor,
    mostrar_todos_los_proveedores,
    editar_proveedor,
    borrar_proveedor,
)
from gestor.productos import (
    agregar_producto,
    mostrar_todos_los_productos,
    editar_producto,
    borrar_producto,
)
from gestor.categorias import (
    agregar_categoria,
    mostrar_todas_las_categorias,
    editar_categoria,
    borrar_categoria,
)

from gestor.exportador_pdf import exportar_factura_interactivamente
from db.base_datos_db import inicializar_base
from interfaz.mensajes import mostrar_error
from interfaz.mensajes import mostrar_bienvenida

def main():
    inicializar_base()
    mostrar_bienvenida()
    while True:
        opcion_principal = mostrar_menu_principal()

        if opcion_principal == "1":  # Ventas
            while True:
                opcion = menu_ventas()
                if opcion == "1":
                    procesar_venta_interactiva()
                elif opcion == "2":
                    #mostrar_facturas(listar_facturas())
                    imprimir_detalle_venta()
                elif opcion == "3":
                    exportar_factura_interactivamente()
                elif opcion == "0":
                    break
                else:
                    mostrar_error("Opción inválida.")

        elif opcion_principal == "3":  # Clientes
            while True:
                opcion = menu_clientes()
                if opcion == "1":
                    agregar_cliente()
                elif opcion == "2":
                    mostrar_todos_los_clientes()
                elif opcion == "3":
                    editar_cliente()
                elif opcion == "4":
                    borrar_cliente()
                elif opcion == "0":
                    break
                else:
                    mostrar_error("Opción inválida.")

        elif opcion_principal == "3":  # Proveedores
            while True:
                opcion = menu_proveedores()
                if opcion == "1":
                    agregar_proveedor()
                elif opcion == "2":
                    mostrar_todos_los_proveedores()
                elif opcion == "3":
                    editar_proveedor()
                elif opcion == "4":
                    borrar_proveedor()
                elif opcion == "0":
                    break
                else:
                    mostrar_error("Opción inválida.")

        elif opcion_principal == "4":  # Productos
            while True:
                opcion = menu_productos()
                if opcion == "1":
                    agregar_producto()
                elif opcion == "2":
                    mostrar_todos_los_productos()
                elif opcion == "3":
                    editar_producto()
                elif opcion == "4":
                    borrar_producto()
                elif opcion == "0":
                    break
                else:
                    mostrar_error("Opción inválida.")

        elif opcion_principal == "5":  # Categorías
            while True:
                opcion = menu_categorias()
                if opcion == "1":
                    agregar_categoria()
                elif opcion == "2":
                    mostrar_todas_las_categorias()
                elif opcion == "3":
                    editar_categoria()
                elif opcion == "4":
                    borrar_categoria()
                elif opcion == "0":
                    break
                else:
                    mostrar_error("Opción inválida.")

        elif opcion_principal == "0":
            print("\n[bold green]👋 ¡Gracias por usar el sistema de gestión![/bold green]")
            break
        else:
            mostrar_error("Opción inválida.")

if __name__ == "__main__":
    main()