from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="mi_base_de_datos"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

class Gerente:
    def __init__(self, db):
        self.collection = db["gerentes"]

    def set_data(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def insertar(self):
        gerente = {"nombre": self.nombre, "edad": self.edad, "ciudad": self.ciudad}
        resultado = self.collection.insert_one(gerente)
        return resultado.inserted_id

    def insertar(self):
        gerente = {"nombre": self.nombre, "edad": self.edad, "ciudad": self.ciudad}
        resultado = self.collection.insert_one(gerente)
        return resultado.inserted_id

class Empresa:
    def __init__(self, db):
        self.collection = db["empresas"]

    def set_data(self, nombre, ubicacion, gerente_id):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.gerente_id = gerente_id

    def insertar(self):
        empresa = {"nombre": self.nombre, "ubicacion": self.ubicacion, "gerente_id": self.gerente_id}
        resultado = self.collection.insert_one(empresa)
        return resultado.inserted_id

class Boleta:
    def __init__(self, db):
        self.collection = db["boletas"]

    def set_data(self, empresa_id, monto, fecha):
        self.empresa_id = empresa_id
        self.monto = monto
        self.fecha = fecha

    def insertar(self):
        boleta = {"empresa_id": self.empresa_id, "monto": self.monto, "fecha": self.fecha}
        resultado = self.collection.insert_one(boleta)
        return resultado.inserted_id