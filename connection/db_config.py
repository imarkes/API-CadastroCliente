class Conect_postgress:
    """ Configura a conexao com o banco de dados"""
    def __init__(self):
        """ Recebe os parametros de conexão com o banco de dados"""
        self.config = {
            'postgres':{
                'host': 'localhost',
                'database': 'clientes_db',
                'user': 'postgres',
                'password': 'henet',
                'port': 5432
            }
    }
