import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
# Conexión a MongoDB Atlas
uri = os.getenv('MONGODB_URI')
client = MongoClient(uri)

# Crear la base de datos 'clasificados-los-tiempos' si no existe
db = client['clasificados-los-tiempos']

# Crear la colección 'inmuebles' con un índice numérico
db['inmuebles'].create_index([('id', 1)], unique=True)
