from mongoConnection import *
from bson import ObjectId

conexion = MongoDBConnection()


gerente_model = Gerente(conexion.db)
gerente_model.set_data("Juan Perez", 45, "Madrid")

empresa_model = Empresa(conexion.db)
empresa_model.set_data("Empresa SII", "Barcelona", None) 

boleta_model = Boleta(conexion.db)
boleta_model.set_data(None, 1000, "2025-02-20") 

gerente_id = gerente_model.insertar()

# Insertar gerente especifico
""" gerente_id = ObjectId("67b77c66796bc9b2a72c19de") """


empresa_model.set_data(empresa_model.nombre, empresa_model.ubicacion, gerente_id)

empresa_id = empresa_model.insertar()

boleta_model.set_data(empresa_id, boleta_model.monto, boleta_model.fecha)

boleta_id = boleta_model.insertar()

""" # Imprimir los IDs de los documentos insertados
print("Gerente insertado con ID:", gerente_id)
print("Empresa insertada con ID:", empresa_id)
print("Boleta insertada con ID:", boleta_id)

# Verificar las relaciones
print("\nVerificando relaciones:")
print("Gerente:", gerente_model.collection.find_one({"_id": gerente_id}))
print("Empresa:", empresa_model.collection.find_one({"_id": empresa_id}))
print("Boleta:", boleta_model.collection.find_one({"_id": boleta_id})) """