from postgresConnection import *

# Conectar a PostgreSQL
conexion = PostgresDBConnection(dbname="postgres", user="postgres", password="tabla1")

# Crear instancias de las clases y asignar datos
gerente_model = Gerente(conexion)
gerente_model.set_data("Juan Perez", 45, "Madrid")

empresa_model = Empresa(conexion)
empresa_model.set_data("Empresa SII", "Barcelona", None)  # gerente_id se asignará después

boleta_model = Boleta(conexion)
boleta_model.set_data(None, 1000, "2025-02-20")  # empresa_id se asignará después

# Insertar un gerente
gerente_id = gerente_model.insertar()

# Asignar el gerente_id a la empresa y boleta
empresa_model.set_data(empresa_model.nombre, empresa_model.ubicacion, gerente_id)

# Insertar una empresa gestionada por el gerente
empresa_id = empresa_model.insertar()

# Asignar el empresa_id a la boleta
boleta_model.set_data(empresa_id, boleta_model.monto, boleta_model.fecha)

# Insertar una boleta o factura para la empresa
boleta_id = boleta_model.insertar()

# Imprimir los IDs de los documentos insertados
print("Gerente insertado con ID:", gerente_id)
print("Empresa insertada con ID:", empresa_id)
print("Boleta insertada con ID:", boleta_id)