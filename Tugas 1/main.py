from flask import Flask 
from connectdb import Database

app = Flask(__name__)

@app.route("/")
def index() :
    return "hello world"


@app.route("/dbpgproxy")
def dbpgproxy():
    conn = Database('ksb-2022')
    result = conn.select("select current_date")
    return str(result)

@app.route("/select")
def select():
    conn = Database('ksb-2022')
    result = conn.select("select * from alfend_672019222")
    return str(result)

@app.route("/insert")
def insert():
    conn = Database('ksb-2022')
    result = conn.execute("INSERT INTO alfend_672019222 (NIM, NAMA, PEMINATAN, TAHUN, ASAL)  VALUES (%s, %s, %s, %s, %s)",('672019121', 'Meyyy Irawati', 'Data Science', '2022-02-20', 'Pati'))
    return str(result)

@app.route("/update")
def update():
    conn = Database('ksb-2022')
    result = conn.execute("UPDATE alfend_672019222 SET NAMA=%s, PEMINATAN=%s, TAHUN=%s, ASAL=%s" + "WHERE NIM=%s" % ('672019121'), ('Mei Irawati', 'Data Science', '2022-02-20', 'Pati'))
    return str(result)

@app.route("/delete")
def delete():
    conn = Database('ksb-2022')
    result = conn.execute("DELETE FROM alfend_672019222 WHERE NIM = %s ", [672019121])
    return str(result)

if __name__ =="__main__" :
    app.run(debug=True)