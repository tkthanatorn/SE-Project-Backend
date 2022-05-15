from .database import Database

db_instance = Database()
db = db_instance.connection()
