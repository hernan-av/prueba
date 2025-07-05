from db.base_datos_db import inicializar_base
from interfaz.mensajes import mostrar_bienvenida
from interfaz.menus import mostrar_menu_principal
from interfaz.mensajes import mostrar_error, mostrar_exito
from flujo_submenus.flujo_submenu_categoria import flujo_categorias
from flujo_submenus.flujo_submenu_productos import flujo_productos
from flujo_submenus.flujo_submenu_proveedores import flujo_proveedores

def main():
    inicializar_base()
    mostrar_bienvenida()

    while True:
        opcion = mostrar_menu_principal()

        if opcion == "4":
            flujo_proveedores()
        elif opcion == "5":
            flujo_productos()
        elif opcion == "6":  
            flujo_categorias()
        elif opcion == "0":
            mostrar_exito("Hasta pronto.")
            break
        else:
            mostrar_error("Opción inválida.")



if __name__ == "__main__":
    main()