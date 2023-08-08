import os
from urllib.parse import quote_plus
import sqlalchemy

basedir = os.path.abspath(os.path.dirname(__file__))


# see : https://cloud.google.com/sql/docs/mysql/connect-app-engine-standard?hl=zh-cn#python
class Config(object):
    db_user = 'bdat1004finalproject'
    db_pass = quote_plus('yPy@3_8sR8=lEU*7')
    db_host = '34.23.80.10'
    db_name = 'default'
    db_conn = 'boxwood-atom-364017:us-east1:bdat1004finalproject'
    unix_socket_path = '/cloudsql/{}'.format(db_conn)  # e.g. '/cloudsql/project:region:instance'

    # see : https://docs.sqlalchemy.org/en/20/core/pooling.html#pool-disconnects
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}/{db_name}"
