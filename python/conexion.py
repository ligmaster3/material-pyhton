

import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import messagebox, Button, Frame, ttk

def connect_db():
    try:
        global cnx
        cnx = mysql.connector.connect(user='root', 
                                      password='',
                                     host='localhost', 
                                      database='db_personas')
        print("Conexión exitosa")
    except mysql.connector.Error as error:
        print("Error de conexión: {}".format(error))

# Función para desconectar de la base de datos
def disconnect_db():
    if cnx:
        cnx.close()
        print("Conexión cerrada")

# Función para agregar una persona a la base de datos
def add_person():
    cursor = cnx.cursor()
    query = "INSERT INTO personas (nombre, apellido, Género) VALUES (%s, %s, %s)"
    values = (nombre.get(), apellido.get(), Género.get())
    cursor.execute(query, values)
    cnx.commit()
    messagebox.showinfo("Success", "Person added successfully")

# Función para realizar consultas según el género
def search_by_gender():
    cursor = cnx.cursor()
    query = "SELECT * FROM personas WHERE gender = %s"
    values = (Género.get(),)
    cursor.execute(query, values)
    result = cursor.fetchall()
    if result:
        for row in result:
            print(row)
    else:
        messagebox.showinfo("Error", "No results found")
        

# Interfaz gráfica
connect_db()
root = Tk()
root.title("Python Login")

nombre_label = Label(root, text="Nombre")
nombre_label.grid(row=0, column=0)
nombre = Entry(root)
nombre.grid(row=0, column=1)

apellido_label = Label(root, text="apellido")
apellido_label.grid(row=1, column=0)
apellido = Entry(root)
apellido.grid(row=1, column=1)

Género_label = Label(root, text="Género")
Género_label.grid(row=2, column=0)
Género = Entry(root)
Género.grid(row=2, column=1)

add_button = Button(root, text="Add Person", command=add_person)
add_button.grid(row=3, column=0)

search_button = Button(root, text="Search  la grafica de ells y lss msyedordby Gender", command=search_by_gender)
search_button.grid(row=3, column=1)

root.mainloop()
disconnect_db()
