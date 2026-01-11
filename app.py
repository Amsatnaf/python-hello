import os
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_db_connection():
    # Pega as variáveis que o OpenShift vai injetar
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST'),
        database=os.environ.get('DB_NAME'),
        user=os.environ.get('DB_USER'),
        password=os.environ.get('DB_PASSWORD')
    )
    return conn

@app.route('/')
def hello():
    db_status = "Desconectado..."
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        db_status = f"Conectado com Sucesso! Versão: {db_version}"
    except Exception as e:
        db_status = f"Erro ao conectar no banco: {str(e)}"

    ##return f"""
    ##<h1>Aplicação Python no OpenShift</h1>
    ##<p>Status do Banco: <b>{db_status}</b></p>
    ##<p>Versão do App: 1.0 (Azul)</p>
    ##"""
    return f"""
    <h1 style="color: green;">Aplicação Python 2.0</h1>
    <p>Status do Banco: <b>{db_status}</b></p>
    <p>Novidade: <b>Agora com CI/CD Automatizado! 🚀</b></p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
