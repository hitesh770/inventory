database_name = 'inventory'
database_host = 'localhost'
database_user = 'postgres'
database_password = '1234'
connection = 'postgres://{0}:{1}@{2}/{3}'.format(database_user,
                                                 database_password,
                                                 database_host,
                                                 database_name)