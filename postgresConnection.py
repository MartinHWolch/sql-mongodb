import psycopg2

class PostgresDBConnection:
    def __init__(self, dbname, user, password, host="localhost", port="5432"):
        self.connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        self.cursor = self.connection.cursor()

class Gerente:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor

    def set_data(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def insertar(self):
        self.cursor.execute(
            "INSERT INTO gerentes (nombre, edad, ciudad) VALUES (%s, %s, %s) RETURNING id",
            (self.nombre, self.edad, self.ciudad)
        )
        self.connection.connection.commit()
        return self.cursor.fetchone()[0]

class Empresa:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor

    def set_data(self, nombre, ubicacion, gerente_id):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.gerente_id = gerente_id

    def insertar(self):
        self.cursor.execute(
            "INSERT INTO empresas (nombre, ubicacion, gerente_id) VALUES (%s, %s, %s) RETURNING id",
            (self.nombre, self.ubicacion, self.gerente_id)
        )
        self.connection.connection.commit()
        return self.cursor.fetchone()[0]

class Boleta:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor

    def set_data(self, empresa_id, monto, fecha):
        self.empresa_id = empresa_id
        self.monto = monto
        self.fecha = fecha

    def insertar(self):
        self.cursor.execute(
            "INSERT INTO boletas (empresa_id, monto, fecha) VALUES (%s, %s, %s) RETURNING id",
            (self.empresa_id, self.monto, self.fecha)
        )
        self.connection.connection.commit()
        return self.cursor.fetchone()[0]