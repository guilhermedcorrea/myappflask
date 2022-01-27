import pyodbc
from urllib.parse import quote_plus

parametros = (
"Driver={SQL Server Native Client 11.0};"
"Server=GUILHERME-PC\DEVMSSQLSERVER;"
"Database=marketplacesellers;"
"UID=sa;"
"PWD=Mudar@123"

)

url_db = quote_plus(parametros)
SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc:///?odbc_connect=%s' %url_db
SQLALCHEMY_TRACK_MODIFICATIONS = False
