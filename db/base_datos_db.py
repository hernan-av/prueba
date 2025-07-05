import sqlite3
import os

RUTA_DB = "data/inventario.db"

# ---------- OPERACIONES CREACIÓN Y CONEXIÓN DB  ----------

def existe_base_datos():
    """Verifica si la base de datos ya fue creada"""
    return os.path.exists(RUTA_DB)

def crear_tablas():
    """Crea todas las tablas necesarias en la base de datos"""
    try:
        conexion = sqlite3.connect(RUTA_DB)
        cursor = conexion.cursor()

        # Tabla categorias
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categorias (
                id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL UNIQUE
            );
        """)

        # Tabla proveedores
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS proveedores (
                id_proveedor INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                telefono TEXT,
                email TEXT,
                cuit TEXT NOT NULL UNIQUE
            );
        """)

        # Tabla productos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                categoria_id INTEGER,
                proveedor_id INTEGER,
                stock INTEGER DEFAULT 0,
                precio_unitario REAL,
                FOREIGN KEY (categoria_id) REFERENCES categorias(id_categoria),
                FOREIGN KEY (proveedor_id) REFERENCES proveedores(id_proveedor)
            );
        """)

        # Tabla clientes
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                telefono TEXT,
                email TEXT,
                dni TEXT NOT NULL UNIQUE
            );
        """)

        # Tabla remitos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS remitos (
                id_remito INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT NOT NULL,
                proveedor_id INTEGER,
                FOREIGN KEY (proveedor_id) REFERENCES proveedores(id_proveedor)
            );
        """)

        # Detalle de remitos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS remito_detalle (
                id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,
                remito_id INTEGER,
                producto_id INTEGER,
                cantidad INTEGER,
                precio_unitario REAL,
                FOREIGN KEY (remito_id) REFERENCES remitos(id_remito),
                FOREIGN KEY (producto_id) REFERENCES productos(id_producto)
            );
        """)

        # Tabla facturas
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS facturas (
                id_factura INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT NOT NULL,
                cliente_id INTEGER,
                total REAL,
                FOREIGN KEY (cliente_id) REFERENCES clientes(id_cliente)
            );
        """)

        # Detalle de facturas
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS factura_detalle (
                id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,
                factura_id INTEGER,
                producto_id INTEGER,
                cantidad INTEGER,
                precio_unitario REAL,
                total_linea REAL,
                FOREIGN KEY (factura_id) REFERENCES facturas(id_factura),
                FOREIGN KEY (producto_id) REFERENCES productos(id_producto)
            );
        """)

        conexion.commit()
        print("Base de datos creada correctamente.")
    except Exception as e:
        print(f"❌ Error al crear la base de datos: {e}")
    finally:
        conexion.close()
    

def obtener_conexion():
    """Devuelve una conexión activa a la base de datos SQLite."""
    return sqlite3.connect(RUTA_DB)

def inicializar_base():
    if not existe_base_datos():
        crear_tablas()
    else:
        print("🔄 Base de datos ya existente. No se requieren cambios.")