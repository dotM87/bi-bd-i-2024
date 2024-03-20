from pymongo import MongoClient

# Conexión a MongoDB Atlas
uri = "mongodb+srv://mbenjaminzr:51fS6hMejs8fInPx@m87-bi-bd.crrwcre.mongodb.net/?retryWrites=true&w=majority&appName=m87-bi-bd"
client = MongoClient(uri)

# Crear la base de datos 'clasificados-los-tiempos' si no existe
db = client['clasificados-los-tiempos']

# Crear la colección 'inmuebles' con un índice numérico
db['inmuebles'].create_index([('id', 1)], unique=True)
