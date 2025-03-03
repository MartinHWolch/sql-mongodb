from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.exceptions import CouchbaseException

# Configuración de la conexión
connection_string = 'couchbases://cb.yuvxi7yi-rhwbveh.cloud.couchbase.com'
username = 'Martinhw'  # Reemplaza con tu nombre de usuario
password = 'Monitores:Monitor1'  # Reemplaza con tu contraseña

cluster = Cluster(connection_string, ClusterOptions(
    PasswordAuthenticator(username, password)
))

# Seleccionar el bucket
bucket_name = 'travel-sample'  # Reemplaza con el nombre de tu bucket
bucket = cluster.bucket(bucket_name)

# Seleccionar la colección (si estás usando Couchbase 7.0 o superior)
collection = bucket.default_collection()

# Hacer un ping para verificar la conexión
try:
    ping_result = cluster.ping()
    print("Ping exitoso:")
    for service, results in ping_result.endpoints.items():
        print(f"Servicio: {service}")
        for result in results:
            print(f"  - {result.id}: {result.state} en {result.latency}")
except CouchbaseException as e:
    print(f"Error al hacer ping: {e}")