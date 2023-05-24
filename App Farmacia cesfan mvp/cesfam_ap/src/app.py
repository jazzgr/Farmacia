from flask import Flask, jsonify
import cx_Oracle



from config import config

app=Flask(__name__)


def getConnection():
    connection=cx_Oracle.connect(
    user='Farmacia',
    password='123',
    dsn='localhost:1522/XE',
    encoding='UTF-8')
    return connection   





@app.route('/cursos/<codigo>', methods=['GET'])
def listar_cursos(codigo):
    lista_medicamentos = []

    try:
        connection = getConnection()
        cursor = connection.cursor()
        stock = cursor.var(cx_Oracle.NUMBER)
        cursor.callproc("SP_OBTENER_STOCK",[codigo,stock])
        medicamentos = stock.getvalue()
        connection.commit()

        return jsonify({'stock':medicamentos,'id_medicamento':codigo,'mensaje': "stock medicamento" })   

    except Exception as ex:
        return jsonify({'mensaje': "Error" })   


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()