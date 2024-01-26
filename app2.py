from flask import Flask
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)

def connect_to_postgresql():
    try:
        # Configura la conexión a PostgreSQL usando la información proporcionada
        # en el servicio de Dokku.
        conn = psycopg2.connect(
            host="198.251.66.139",
            user="postgres",
            password="d22a5660ec8eb7f39123ca572ffba76f",
            database="bradexpenses",
            port="5432"
        )

        # Si la conexión se estableció con éxito, retorna un objeto de conexión.
        return conn

    except OperationalError as e:
        # Si hay un error de conexión, captura la excepción y retorna None.
        return None

@app.route('/')
def check_postgresql_connection():
    # Intenta conectarse a PostgreSQL.
    db_connection = connect_to_postgresql()

    if db_connection:
        # La conexión fue exitosa, imprime un mensaje en la página.
        return "Conexión exitosa a PostgreSQL"

    else:
        # No se pudo establecer la conexión, muestra un mensaje de error.
        return "Error al conectar a PostgreSQL. Detalles: {}"

if __name__ == '__main__':
    app.run(debug=True)
