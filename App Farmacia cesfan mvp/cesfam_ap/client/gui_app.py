import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from model.conexion import guardar_med, getConnection, listar_medicamentos, editar ,eliminar, listar_pacientes, crear_prescripcion
import json, requests

import cx_Oracle

getConnection()

lista_id=[]

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=300, height = 300)


    menu_inicio = tk.Menu(barra_menu, tearoff= 0)
    barra_menu.add_cascade(label='Inicio', menu= menu_inicio)

    menu_inicio.add_command(label= 'Añadir medicamento en DB')
    menu_inicio.add_command(label= 'Eliminar medicamento en DB')
    menu_inicio.add_command(label= 'Salir', command= root.destroy)

    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Configuraion')
    barra_menu.add_cascade(label='Ayuda')

class Frame(tk.Frame):
    def __init__(self, root =  None):
        super().__init__(root, width= 480, height=320)
        self.root = root
        self.pack()
        #self.config(bg = 'green')
        self.id_medi= None

        self.campos_medicamentos()
        self.desabilitar_campos()
        self.tabla_medicamentos()

    def campos_medicamentos(self):
        self.label_nombre = tk.Label(self, text = 'Nombre Medicamento: ')
        self.label_nombre.config(font= ('Arial', 12, 'bold'))
        self.label_nombre.grid(row= 0 , column= 0, padx= 10, pady= 10)

        self.label_formato = tk.Label(self, text = 'Formato: ')
        self.label_formato.config(font= ('Arial', 12, 'bold'))
        self.label_formato.grid(row= 1 , column= 0, padx= 10, pady= 10)

        self.label_fech_elav= tk.Label(self, text = 'Fecha Elab: ')
        self.label_fech_elav.config(font= ('Arial', 12, 'bold'))
        self.label_fech_elav.grid(row= 2 , column= 0, padx= 10, pady= 10)

        self.label_fech_venc= tk.Label(self, text = 'Fecha Venc: ')
        self.label_fech_venc.config(font= ('Arial', 12, 'bold'))
        self.label_fech_venc.grid(row= 3 , column= 0, padx= 10, pady= 10)

        self.label_unidad = tk.Label(self, text = 'Unidad: ')
        self.label_unidad.config(font= ('Arial', 12, 'bold'))
        self.label_unidad.grid(row= 4 , column= 0, padx= 10, pady= 10)

        self.label_componente = tk.Label(self, text = 'Componente: ')
        self.label_componente.config(font= ('Arial', 12, 'bold'))
        self.label_componente.grid(row= 5 , column= 0, padx= 10, pady= 10)

        self.label_stock = tk.Label(self, text = 'Stock: ')
        self.label_stock.config(font= ('Arial', 12, 'bold'))
        self.label_stock.grid(row= 6 , column= 0, padx= 10, pady= 10)


#---------------------------------------------------------------------------------------------------------
    #Entrys de cada campo
        self.mi_nombre = tk.StringVar()

        self.entry_nombre = tk.Entry(self, textvariable= self.mi_nombre)
        self.entry_nombre.config(width= 50, font=('Arial', 12))
        self.entry_nombre.grid(row= 0, column=1, padx=10, pady=10)

    #---------------------------------------
        self.mi_formato = tk.StringVar()

        self.entry_formato = tk.Entry(self, textvariable= self.mi_formato)
        self.entry_formato.config(width= 50, font=('Arial', 12))
        self.entry_formato.grid(row= 1, column=1, padx=10, pady=10)

     #---------------------------------------
        self.mi_fecha_elav = tk.StringVar()

        self.entry_fech_elav = tk.Entry(self, textvariable= self.mi_fecha_elav)
        self.entry_fech_elav.config(width= 50, font=('Arial', 12))
        self.entry_fech_elav.grid(row= 2, column=1, padx=10, pady=10)
#-----------------------------------------------------------------------------------------------------------
        self.mi_fecha = tk.StringVar()

        self.entry_fech_venc = tk.Entry(self, textvariable= self.mi_fecha)
        self.entry_fech_venc.config(width= 50, font=('Arial', 12))
        self.entry_fech_venc.grid(row= 3, column=1, padx=10, pady=10)
#-----------------------------------------------------------------------------------------------------------
    #---------------------------------------
        self.mi_unidad = tk.StringVar()

        self.entry_unidad= tk.Entry(self, textvariable= self.mi_unidad)
        self.entry_unidad.config(width= 50, font=('Arial', 12))
        self.entry_unidad.grid(row= 4, column=1, padx=10, pady=10)

    #---------------------------------------
        self.mi_componente = tk.StringVar()

        self.entry_componente= tk.Entry(self, textvariable= self.mi_componente)
        self.entry_componente.config(width= 50, font=('Arial', 12))
        self.entry_componente.grid(row= 5, column=1, padx=10, pady=10)

    #---------------------------------------
        self.mi_stock = tk.StringVar()

        self.entry_stock= tk.Entry(self, textvariable= self.mi_stock)
        self.entry_stock.config(width= 50, font=('Arial', 12))
        self.entry_stock.grid(row= 6, column=1, padx=10, pady=10)

    #---------------------------------------
    #BOTONES

        self.boton_nuevo = tk.Button(self, text="Nuevo", command= self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg= '#158645', cursor= 'hand2', activebackground= '#35BD6F')
        self.boton_nuevo.grid(row=7, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text="Guardar", command= self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg= '#1658A2', cursor= 'hand2', activebackground= '#3586DF')
        self.boton_guardar.grid(row=7, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text="Cancelar", command= self.desabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg= '#BD152E', cursor= 'hand2', activebackground= '#E15370')
        self.boton_cancelar.grid(row=7, column=3, padx=10, pady=10)
#------------------------------------------------------------------------------------------------------------------------------------------------------------



#funciones

    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_formato.set('')
        self.mi_fecha_elav.set('')
        self.mi_fecha.set('')
        self.mi_unidad.set('')
        self.mi_componente.set('')
        self.mi_stock.set('')


        self.entry_nombre.config(state='normal')
        self.entry_formato.config(state='normal')
        self.entry_fech_elav.config(state='normal')
        self.entry_fech_venc.config(state='normal')
        self.entry_unidad.config(state='normal')
        self.entry_componente.config(state='normal')
        self.entry_stock.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    def desabilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_formato.set('')
        self.mi_fecha_elav.set('')
        self.mi_fecha.set('')
        self.mi_unidad.set('')
        self.mi_componente.set('')
        self.mi_stock.set('')


        self.entry_nombre.config(state='disabled')
        self.entry_formato.config(state='disabled')
        self.entry_fech_elav.config(state='disabled')
        self.entry_fech_venc.config(state='disabled')
        self.entry_unidad.config(state='disabled')
        self.entry_componente.config(state='disabled')
        self.entry_stock.config(state='disabled')

        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')

    def guardar_datos(self):

        guardar_med(
        self.mi_nombre.get(),
        self.mi_formato.get(),
        self.mi_fecha_elav.get(),
        self.mi_fecha.get(),
        self.mi_unidad.get(),
        self.mi_componente.get(),
        self.mi_stock.get())

        self.tabla_medicamentos()

        self.desabilitar_campos()
   

    def tabla_medicamentos(self):

        self.lista_medicamentos = listar_medicamentos()


        self.tabla = ttk.Treeview(self,
        columns= ('Nombre', 'Formato', 'Fecha_Elav', 'Fecha_Venc', 'Unidad', 'Componente', 'Stock'))
        self.tabla.grid(row= 8, column=-0, columnspan= 8, sticky = 'nse')

        
# Scrollbars 

        self.scroll = ttk.Scrollbar(self,
        orient= 'vertical', command= self.tabla.yview)
        self.scroll.grid(row = 8, column=8, sticky = 'nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)

                


        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre Medicamento')
        self.tabla.heading('#2', text='Formato Medicamento')
        self.tabla.heading('#3', text='Fecha Elav')
        self.tabla.heading('#4', text='Fecha Venc')
        self.tabla.heading('#5', text='Unidad')
        self.tabla.heading('#6', text='Componente')
        self.tabla.heading('#7', text='Stock')


        for result in self.lista_medicamentos:
            self.tabla.insert('',0, text=result[0], values= (result[1], result[2], result[3], result[4], result[5], result[6], result[7]))




        #BOTON EDITAR
        self.boton_editar = tk.Button(self, text="Editar", command = self.editar_medicamento)
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg= '#158645', cursor= 'hand2', activebackground= '#35BD6F')
        self.boton_editar.grid(row=9, column=0, padx=10, pady=10)

        #BOTON ELIMINAR
        self.boton_eliminar = tk.Button(self, text="Eliminar", command= self.eliminar_medicamento)
        self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg= '#BD152E', cursor= 'hand2', activebackground= '#E15370')
        self.boton_eliminar.grid(row=9, column=2, padx=10, pady=10)

        #BOTON GUARDAR EDITAR
        self.boton_guardar_editar = tk.Button(self, text="Guardar Cambio", command= self.guardar_cambios)
        self.boton_guardar_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg= '#1658A2', cursor= 'hand2', activebackground= '#3586DF')
        self.boton_guardar_editar.grid(row=9, column=1, padx=10, pady=10)

        self.boton_consultar_datos = tk.Button(self, text="Consultar stock",command=VentanaSecundaria)
        self.boton_consultar_datos.config(width=20, font=('Arial', 12, 'bold'), fg='#DAf5D9', bg= '#BD152E', cursor= 'hand2', activebackground= '#E15370')
        self.boton_consultar_datos.grid(row=9, column=3, padx=10, pady=10)


        #Consultar datos BOTON CON SU FUNCION DE ABRIR UNA VEENTANA NUEVA
        self.boton_retirar = tk.Button(self, text="Retirar",command=Ventana3)
        self.boton_retirar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAf5D9', bg= '#BD152E', cursor= 'hand2', activebackground= '#E15370')
        self.boton_retirar.grid(row=3, column=3, padx=10, pady=10)

        

    def guardar_cambios(self):

        id_almacenar = self.id_medicamento = self.tabla.item(self.tabla.selection())['text']

        

        editar(id_almacenar ,self.mi_stock.get())
        
        self.tabla_medicamentos()

        self.desabilitar_campos()



    def eliminar_medicamento(self):

        id_medicamento_eliminarr = self.id_medicamento = self.tabla.item(self.tabla.selection())['text']

        eliminar(id_medicamento_eliminarr)
        
        self.tabla_medicamentos()

        self.desabilitar_campos()





    def editar_medicamento(self):
        try:
            self.nom_medicamento= self.tabla.item(self.tabla.selection())['values'][0]
            self.stock= self.tabla.item(self.tabla.selection())['values'][6]



            self.habilitar_campos()

            self.entry_nombre.insert(0,self.nom_medicamento)
            self.entry_stock.insert(0,self.stock)

        

        except:
            titulo= 'Edición de datos'
            mensaje='No ha seleccionado ningun registro'
            messagebox.showerror(titulo,mensaje)



class VentanaSecundaria(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=1000, height=700)
        self.title("Ventana secundaria")
        

        self.campo_stock()

        self.boton_cerrar = ttk.Button(
            self,
            text="Cerrar ventana",
            command=self.destroy
        )
        self.boton_cerrar.place(x=50, y=150)
        self.focus()
        self.grab_set()


    def guardar_stock_webservice(self):
        
        self.clave_stock.get()


        



    def campo_stock(self):
        self.label_stock = tk.Label(self, text = 'Stock: ')
        self.label_stock.config(font= ('Arial', 12, 'bold'))
        self.label_stock.grid(row= 1 , column= 0, padx= 10, pady= 10)


        self.clave_stock = tk.StringVar()

        self.tock= tk.Entry(self, textvariable= self.clave_stock)
        self.tock.config(width= 50, font=('Arial', 12))
        self.tock.grid(row= 1, column=1, padx=10, pady=10)



        self.campo_buscar = tk.Button(self, text="Buscar",command= self.obt_stock_web_servise)
        self.campo_buscar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg= '#1658A2', cursor= 'hand2', activebackground= '#3586DF')
        self.campo_buscar.grid(row=3, column=1, padx=10, pady=10)



    def obt_stock_web_servise(self):
        clave_stock = self.clave_stock.get()
        resp = requests.get("http://127.0.0.1:5000/cursos/"+ clave_stock)
        data = json.loads(resp.content)
        titulo= 'Consulta exitosa'
        mensaje= ("Stock: ", data["stock"], "Id_medicamento: ", data["id_medicamento"])
        messagebox.showinfo(titulo,mensaje)




class Ventana3(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=1000, height=700)
        self.title("Ventana paciente")

    
        self.tabla_pacientes()
        self.campos_medicamentos4()
        self.tabla_listaStock()
        self.desabilitar_campos()

        
        self.focus()
        self.grab_set()

    def tabla_pacientes(self):

        self.lista_paciente= listar_pacientes()

        self.tabla = ttk.Treeview(self,
        columns= ('Rut', 'Nombre_Paciente'))
        self.tabla.grid(row= 2, column=0, columnspan= 2)

        self.tabla.heading('#0', text='ID_Paciente')
        self.tabla.heading('#1', text='Rut')
        self.tabla.heading('#2', text='Nombre Paciente')

        
        for result in self.lista_paciente:

            self.tabla.insert('',0, text=result[0], values= (result[1], result[2]))


        self.boton_siguiente = tk.Button(self, text="Seleccionar paciente", command= self.guardar_id_1)
        self.boton_siguiente.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg= '#158645', cursor= 'hand2', activebackground= '#35BD6F')
        self.boton_siguiente.grid(row=9, column=2, padx=10, pady=10)


    # def ir_a_Ventana4(self):
            
    #     Ventana4()

    def guardar_id_1(self):
        
        self.id_paciente_obtenible = self.tabla.item(self.tabla.selection())['text']
        return self.id_paciente_obtenible        






# class Ventana4(tk.Toplevel):
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.config(width=1000, height=700)
#         self.title("Ventana 4")

#         self.campos_medicamentos4()
#         self.tabla_listaStock()
#         self.desabilitar_campos()
        
#         self.focus()
#         self.grab_set()

    def campos_medicamentos4(self):
        self.label_id = tk.Label(self, text = 'Id_medicamento ')
        self.label_id.config(font= ('Arial', 12, 'bold'))
        self.label_id.grid(row= 3 , column= 0, padx= 10, pady= 10)

        self.label_medicamento4 = tk.Label(self, text = 'Medicamento')
        self.label_medicamento4.config(font= ('Arial', 12, 'bold'))
        self.label_medicamento4.grid(row= 4 , column= 0, padx= 10, pady= 10)

        self.label_stock_= tk.Label(self, text = 'Stock ')
        self.label_stock_.config(font= ('Arial', 12, 'bold'))
        self.label_stock_.grid(row= 5 , column= 0, padx= 10, pady= 10)

        self.label_retiro= tk.Label(self, text = 'Cantidad a retirar')
        self.label_retiro.config(font= ('Arial', 12, 'bold'))
        self.label_retiro.grid(row= 6 , column= 0, padx= 10, pady= 10)

        self.mi_id4 = tk.StringVar()

        self.entry_id4 = tk.Entry(self, textvariable= self.mi_id4)
        self.entry_id4.config(width= 50, font=('Arial', 12))
        self.entry_id4.grid(row= 3, column=1, padx=10, pady=10)

    #---------------------------------------
        self.mi_medicamento4 = tk.StringVar()

        self.entry_medicamento4 = tk.Entry(self, textvariable= self.mi_medicamento4)
        self.entry_medicamento4.config(width= 50, font=('Arial', 12))
        self.entry_medicamento4.grid(row= 4, column=1, padx=10, pady=10)

     #---------------------------------------
        self.mi_stock4 = tk.StringVar()

        self.entry_stock4 = tk.Entry(self, textvariable= self.mi_stock4)
        self.entry_stock4.config(width= 50, font=('Arial', 12))
        self.entry_stock4.grid(row= 5, column=1, padx=10, pady=10)

        self.retiro_stock = tk.StringVar()

        self.entry_retiro = tk.Entry(self, textvariable= self.retiro_stock)
        self.entry_retiro.config(width= 50, font=('Arial', 12))
        self.entry_retiro.grid(row= 6, column=1, padx=10, pady=10)


    def desabilitar_campos(self):
        self.mi_id4.set('')
        self.mi_medicamento4.set('')
        self.mi_stock4.set('')
        self.retiro_stock.set('')


        self.entry_id4.config(state='disabled')
        self.entry_medicamento4.config(state='disabled')
        self.entry_stock4.config(state='disabled')
        self.entry_retiro.config(state='disabled')


        self.boton_retirar.config(state='disabled')
        # self.boton_seleccionar.config(state='disabled')

    # def desabilitar_campos_medi(self):
        
    #      self.boton_retirar.config(state='normal')

    def habilitar_campos(self):

        self.mi_id4.set(self.tabla1.item(self.tabla1.selection())['text'])
        self.mi_medicamento4.set(self.tabla1.item(self.tabla1.selection())['values'][0])
        self.mi_stock4.set(self.tabla1.item(self.tabla1.selection())['values'][1])
        self.retiro_stock.set('')



        self.entry_id4.config(state='disabled')
        self.entry_medicamento4.config(state='disabled')
        self.entry_stock4.config(state='disabled')
        self.entry_retiro.config(state='normal')

        self.boton_seleccionar.config(state='normal')
        self.boton_retirar.config(state='normal')
        

        self.guardar_id()


    def tabla_listaStock(self):

        self.lista_medicamentos = listar_medicamentos()


        self.tabla1 = ttk.Treeview(self,
        columns= ('Nombre','Stock'))
        self.tabla1.grid(row= 7,  column=0, columnspan= 2)

        self.tabla1.heading('#0', text='Id')
        self.tabla1.heading('#1', text='Nombres')
        self.tabla1.heading('#2', text='Stock')

        for result in self.lista_medicamentos:

            self.tabla1.insert('',0, text=result[0], values= (result[1], result[7]))


        self.boton_seleccionar = tk.Button(self, text="Seleccionar Medicamento", command=self.habilitar_campos)
        self.boton_seleccionar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg= '#158645', cursor= 'hand2', activebackground= '#35BD6F')
        self.boton_seleccionar.grid(row=9, column=0, padx=10, pady=10)

        self.boton_retirar = tk.Button(self, text="Retirar", command= self.guardar_id)
        self.boton_retirar.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', bg= '#158645', cursor= 'hand2', activebackground= '#35BD6F')
        self.boton_retirar.grid(row=9, column=1, padx=10, pady=10)

    def guardar_id(self):

        self.id_medicamento_obtenible = self.tabla1.item(self.tabla1.selection())['text']
        id_paci =    self.guardar_id_1()
        print(id_paci)
        print(self.id_medicamento_obtenible)
        crear_prescripcion(self.id_medicamento_obtenible,id_paci, self.retiro_stock.get())

 
        titulo= 'Retiro éxitoso'
        mensaje= ("id_Paciente: ", id_paci , "Id_medicamento: ",self.id_medicamento_obtenible)
        messagebox.showinfo(titulo,mensaje)
        
        


        
