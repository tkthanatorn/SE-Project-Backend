from utils import get_config
from psycopg2 import connect


class Database:
    def __init__(self) -> None:
        db_configs = get_config(['db', 'dev'])
        self._dsn = f"host={db_configs['host']} port={db_configs['port']} user={db_configs['user']} password={db_configs['password']} dbname={db_configs['dbname']}"

    def connection(self):
        try:
            conn = connect(self._dsn)
            print("Database connected...")
            return conn
        except Exception as e:
            print(e)
