import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def conexion():
    try:
        global conn
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password='',
            database='empresavirtual'
        )
        print("Conexión exitosa")
    except mysql.connector.Error as err:
        print("Error de conexion: {}".format(err))

def guardar():
    primario = name.get()
    secundario = appe.get()
    seccion = sexobox.get()

    if not name.get() or not appe.get() or not sexobox.get():
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    try:
        cursor = conn.cursor()
        query = "INSERT INTO personas (nombre, apellido, sexo) VALUES (%s, %s, %s)"
        cursor.execute(query, (primario, secundario, seccion))
        conn.commit()
        messagebox.showinfo("Exito", "Registro exitoso")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"No se pudo realizar el registro: {err}")
    finally:
        if conn:
            conn.close()

conexion()

#ventana de tkinter
root = tk.Tk()
root.geometry("400x400")
root.title("Gestions de clientes")

#widgets
nombre = tk.Label(root,text="nombre del cliente").grid(column=0,row=0,padx=10,pady=5)
name = tk.Entry(root)
name.grid(row=0,column=1,padx=10,pady=5)

appellido = tk.Label(root,text="apellido del cliente").grid(column=0,row=1,padx=10,pady=5)
appe = tk.Entry(root)
appe.grid(column=1,row=1,padx=10,pady=5)

sexo = tk.Label(root,text="sexo del cliente").grid(column=0,row=2,padx=10,pady=5)
sexobox = ttk.Combobox(root, values=["Masculino", "Femenino"],state="readonly")
sexobox.grid(column=1, row=2, padx=10, pady=5)
        
btn_guardar = ttk.Button(root, text="Guardar",command=guardar)
btn_guardar.grid(column=0, row=3, columnspan=2)
        

        
root.mainloop()
 
