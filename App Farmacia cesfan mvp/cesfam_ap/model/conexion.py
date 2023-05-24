import cx_Oracle
from tkinter import messagebox


def getConnection():
    connection=cx_Oracle.connect(
    user='farmacia',
    password='123',
    dsn='localhost:1521/XE',
    encoding='UTF-8')
    return connection   


def listar_medicamentos():
    lista_medicamentos = []
    sql_select_medi = "select * from medicamento"

    try:
        connection = getConnection()
        cursor = connection.cursor()
        lista_medicamentos = cursor.execute(sql_select_medi)
        connection.commit()

        messagebox.showwarning
        titulo = 'Conexion al Registro'
        mensaje = 'Datos ingresados correctamente'
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Error al ingresar los datos.'
        messagebox.showerror(titulo, mensaje)
    
    return lista_medicamentos
        
def guardar_med( nom_medicamento, formato, fecha_elav, fecha_venc, unidad, componente, stock):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.callproc("SP_AGREGAR_MEDICAMENTO",[nom_medicamento, formato, fecha_elav, fecha_venc, unidad, componente, stock])



def editar(id_medicamento, stock ):
    connection = getConnection()
    cursor = connection.cursor()

    cursor.callproc("SP_UPDATE_STOCK",[id_medicamento,stock])



def eliminar(id_medicamento):
    connection = getConnection()
    cursor = connection.cursor()

    cursor.callproc("SP_DELETE_MEDICAMENTO",[id_medicamento])




    def __str__(self):
        return f'Medicamento[{self.nom_medi}, {self.forma}, {self.fecha_ela}, {self.fecha_ven}, {self.uni}, {self.compo}, {self.stoc}]'



def listar_pacientes():
           
    listar_pacientes = []
    sql_select_paciente = "select * from paciente"

    try:
        connection = getConnection()
        cursor = connection.cursor()
        listar_pacientes = cursor.execute(sql_select_paciente)
        connection.commit()

        messagebox.showwarning
        titulo = 'Conexion al Registro'
        mensaje = 'Datos ingresados correctamente'
    except:
        titulo = 'Conexion al Registro'
        mensaje = 'Error al ingresar los datos.'
        messagebox.showerror(titulo, mensaje)
    
    return listar_pacientes






def crear_prescripcion(id_medicamento_obtenible, id_paciente,stock):
        


        connection = getConnection()
        cursor = connection.cursor()

        cursor.callproc("SP_CREAR_PRESCRIP",[id_medicamento_obtenible, id_paciente ,stock])   


