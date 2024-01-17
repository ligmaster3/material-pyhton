import mysql.connector
import tkinter as tk
from tkinter import messagebox, ttk, PhotoImage
from PIL import ImageTk, Image
from customtkinter import CTkButton, CTkFrame

class Registro:
    def __init__(self, ventana):
        # Crear la ventana principal
        self.wind = ventana
        self.wind.title("Formulario de Registro con tkinter y Python")
        self.wind.geometry("1000x640+100+50")
        self.wind.resizable(0,0)
        self.wind.iconbitmap("imagen\iconos-computadora.ico")
        
        #fondo++
        image = PhotoImage(file = "imagen\Patch-Notes.png")
        fondo=tk.Label(self.wind,image=image).place(x=0,y=0,relwidth=1,relheight=1)
                
        # Crear un contenedor        
        marco = CTkFrame(ventana,width=100,height=2,fg_color="#E5E7E9")
        titulo = tk.Label(ventana, text="REGISTRO DE USUARIO", bg="#6c757d",font=('Arial',14), fg="white", width="100", height=3)
        titulo.pack(side="top")
        marco.pack(side="top")

        self.titulo = tk.Label(marco, text="LOGIN",bg="#E5E7E9",width=35,height=3)
        self.titulo.pack(side="top")
        # Caja de texto para ingresar el nombre
        self.name_label = tk.Label(marco, text="Nombre",bg="#E5E7E9")
        self.name_label.pack(padx=6, pady=6)
        self.name_entry = tk.Entry(marco)
        self.name_entry.pack(padx=5, pady=5)

        # Caja de texto para ingresar el apellido
        self.appe_label = tk.Label(marco, text="Apellido",bg="#E5E7E9")
        self.appe_label.pack(padx=6, pady=6)
        self.appe_entry = tk.Entry(marco)
        self.appe_entry.pack(padx=5, pady=5)


        # Caja de texto para ingresar la genero
        self.genero_label = tk.Label(marco, text="Genero",bg="#E5E7E9")
        self.genero_label.pack(padx=6, pady=6)
        self.genero_entry = tk.StringVar()
        genero = ["Masculino", "Femenino"]
        self.genero_combobox = ttk.Combobox(marco, textvariable=self.genero_entry, values=genero, state="readonly")
        self.genero_combobox.current(0)
        self.genero_combobox.pack(padx=5, pady=5)
        
        
        
        # Caja de texto para ingresar la direccion
        self.direccion_label = tk.Label(marco, text="Direccion",bg="#E5E7E9")
        self.direccion_label.pack(padx=6, pady=6)
        self.direccion_entry = tk.Entry(marco)
        self.direccion_entry.pack(padx=5, pady=5)

        # Caja de texto para ingresar el celular
        self.celular_label = tk.Label(marco, text="Celular",bg="#E5E7E9")
        self.celular_label.pack(padx=6, pady=6)
        self.celular_entry = tk.Entry(marco)
        self.celular_entry.pack(padx=5, pady=5)

        
        # boton de guardar los registrosS
        self.reg_button = CTkButton(marco, text="REGISTRAR", command=self.registrar, 
                                    height=20,width=12,fg_color="green",corner_radius=10)
        self.reg_button.pack(padx=3, pady=3)


        # Botón para cerrar
        self.boton_cancelar=CTkButton(marco, text="CERRAR", command=self.cerrar,
                                      height=20,width=12,fg_color="green",corner_radius=10)
        self.boton_cancelar.pack(padx=3, pady=3)
        #boton invisble no tocar ni borrar
        btn = tk.Button(ventana)
        btn.grid(row=0,column=1)
        #---------------------------------
        

    def conexion(self):
        try:
            conn = mysql.connector.connect(
                host="localhost", 
                user="root", 
                password="",
                database="comercial"
                )
            print("Conexion a la base de datos exitosa")
            return conn
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            return None

    def registrar(self):
        nombre = self.name_entry.get()
        apellido = self.appe_entry.get()
        genero = self.genero_entry.get()
        direccion = self.direccion_entry.get()
        celular = self.celular_entry.get()
      

        if not nombre or not apellido or not genero or not direccion or not celular:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        conn = self.conexion()
        if conn:
            try:
               cursor = conn.cursor()
               query = "INSERT INTO cliente (nombre, apellido, genero, direccion, celular) VALUES (%s, %s, %s, %s, %s)"
               cursor.execute(query, (nombre, apellido, genero, direccion, celular))
               conn.commit()
               messagebox.showinfo("Exito", "Registro exitoso")
            except mysql.connector.Error as err:
               messagebox.showerror("Error", f"No se pudo realizar el registro: {err}")
            finally:
                conn.close()

                
    def cerrar(self):
        self.wind.destroy()


if __name__ == "__main__":
    ventana = tk.Tk()
    mi_app = Registro(ventana)
    ventana.mainloop()
