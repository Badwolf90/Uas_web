from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# Konfigurasi database
app.config['MYSQL_HOST'] = '1y1zj.h.filess.io'
app.config['MYSQL_USER'] = 'uaspemograman_choicesent'
app.config['MYSQL_PASSWORD'] = '4f04f5222a63dc3a5d2aa9cbc1042bf5fd7d8930'
app.config['MYSQL_DB'] = 'uaspemograman_choicesent'
app.config['MYSQL_PORT'] = 3306

mysql = MySQL(app)

@app.route('/')
def home():
    return "Selamat datang di aplikasi Flask dengan MySQL!"

@app.route('/test_db')
def test_db():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()
        cur.close()
        return jsonify({"message": "Koneksi berhasil!", "MySQL_Version": version[0]})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
