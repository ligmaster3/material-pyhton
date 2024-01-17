from customtkinter import * 

app = CTk()
app.title("pruebas de ctk")
app.geometry("500x400")

frame = CTkFrame(master=app , bg_color="white", border_color="#FFCC70", border_width=4)
frame.pack(expand=True,pady=30,padx=50)
frame.place()

label = CTkLabel(master=frame, text="This escripint..").pack(pady=10,padx=30)

entry = CTkEntry(master=frame, placeholder_text="nombe..").pack(pady=20,padx=39)

btm = CTkButton(master=frame, text="clck 1 ").pack(pady=20,padx=40)


app.mainloop()
