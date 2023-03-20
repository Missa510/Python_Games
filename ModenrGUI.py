import customtkinter
#import tkinter

"""root = tkinter.Tk()
label = tkinter.Label(root, )
label.pack()"""

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("600x350")

def login():
    print("\t * * Su usuario ha sido registrado exitosamente :D * *")

frame = customtkinter.CTkFrame(master = root)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

label = customtkinter.CTkLabel(master = frame, text = "Sistema de login", text_font = ("Roboto", 24))

label.pack(pady = 12, padx = 10)

enrty1 = customtkinter.CTkEntry(master = frame, placeholder_text = "Usuario")
enrty1.pack(pady = 12, padx = 8)
enrty2 = customtkinter.CTkEntry(master = frame, placeholder_text = "Password", show = "*")
enrty2.pack(pady = 12, padx = 8)

button = customtkinter.CTkButton(master = frame, text = "Entrar", command = login)
button.pack(pady = 12, padx = 8)

"""
prueba = customtkinter.CTkProgressBar(master = frame, range = 10)
prueba.pack(pady = 12, padx = 8)
"""
checkBox = customtkinter.CTkCheckBox(master = frame, text = "Holanda, por aca")
checkBox.pack(pady = 12, padx = 8)

root.mainloop()