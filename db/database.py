from psycopg2 import connect
from utils import get_config


class Database:
    def __init__(self) -> None:
        db_configs = get_config(['db', 'dev'])
        dns = f"host={db_configs['host']} port={db_configs['port']} user={db_configs['user']} password={db_configs['password']} dbname={db_configs['dbname']}"
        try:
            self.connection = connect(dns)
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print('Database connected...')
        except:
            print('Cannot connect to database...')
