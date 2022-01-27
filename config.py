import pyodbc
from urllib.parse import quote_plus
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())
string_conexao = os.getenv("parametros")



url_db = quote_plus(string_conexao)
SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect=%s' %url_db
SQLALCHEMY_TRACK_MODIFICATIONS = False
