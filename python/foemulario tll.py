
import tkinter as tk
from tkinter import messagebox

def mostrar_datos():
    #obtine los datos de los campos de entradad(entry)
    cedula = cedula_entry.get()
    apellido = apellido_entry.get()
    nombre = nombre_entry.get()
    edad = edad_entry.get()
    
    #muestra los datos en cuadro de mensaje
    messagebox.showinfo("Datos ingresados",f"cedula: {cedula}\nApellido: {apellido}\nNombre: {nombre}\Edad: {edad}")
    
    #creacion de la venana principal
    root = tk.Tk()
    root.title("ingrese de  datos ")
    
    #etiquea y campos de entrada para cedula.apellido,nombre y edad
    tk.Label(root,text="Cedula:").grid(row=0,column=0,sticky="w",padx=10,pady=5)
    cedula_entry = tk.ENTRY(root)
    cedula_entry.grid(row=0,column=0,padx=5,pady=5)
    
    tk.Label(root,text="Apellido:").grid(row=0,column=0,sticky="w",padx=10,pady=5)
    cedula_entry = tk.ENTRY(root)
    cedula_entry.grid(row=0,column=0,padx=5,pady=5)
        
    tk.Label(root,text="Nombre:").grid(row=0,column=0,sticky="w",padx=10,pady=5)
    cedula_entry = tk.ENTRY(root)
    cedula_entry.grid(row=0,column=0,padx=5,pady=5)    
    
    tk.Label(root,text="Edad:").grid(row=0,column=0,sticky="w",padx=10,pady=5)
    cedula_entry = tk.ENTRY(root)
    cedula_entry.grid(row=0,column=0,padx=5,pady=5)
    
    #boton de mostrar los datos
    tk.Button(root,text="Mostrar Datos",command=mostrar_datos).grid(row=4,column=0,padx=10,pady=20)
    
    #boton del programa salir
    tk.button(root,text="Salir",command=root.quit).grid(row=4,column=1,padx=10,pady=20)
    
    root.mainloop()