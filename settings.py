MYSQL_HOST = ''
MYSQL_USER = ''
MYSQL_PASS = ''
POSTGRES_HOST = ''
POSTGRES_USER = ''
POSTGRES_PASS = ''

try:
    from local_settings import *
except:
    pass
