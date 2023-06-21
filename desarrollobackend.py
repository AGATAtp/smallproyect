from tkinter import Tk, Frame, Entry, Label, Button, Checkbutton, StringVar
from PIL import ImageTk, Image

# Colores
c_negro = "#010101"
c_morado = "#7f5af0"
c_verde = "#2cb67d"

def iniciar_sesion():
    # Obtener el valor del campo de entrada de usuario
    usuario = correo_var.get()

    # Cerrar la primera ventana
    root.destroy()

    # Crear nueva ventana
    new_window = Tk()
    new_window.geometry("500x600+350+120")
    new_window.config(bg=c_negro)
    new_window.title("TecOn")

    # Crear frame con fondo morado en la parte superior
    top_frame = Frame(new_window, bg=c_morado)
    top_frame.pack(side="top", fill="x")

    # Agregar texto "TecOn"
    tecon_label = Label(top_frame, text="TecOn", fg="white", font=("Arial", 24), bg=c_morado)
    tecon_label.pack(pady=10)

    # Cargar imagen del buitre
    buitre_image = Image.open("logo.png")
    buitre_image_resized = buitre_image.resize((200,200))
    buitre_photo = ImageTk.PhotoImage(buitre_image_resized)

    # Agregar etiqueta de imagen del buitre
    buitre_label = Label(new_window, image=buitre_photo, bg=c_negro)
    buitre_label.image = buitre_photo
    buitre_label.pack(side="left", padx=10, pady=(0, 10))

    # Crear frame con letras verdes dependiendo del valor de usuario
    user_frame = Frame(new_window, bg=c_negro)
    user_frame.pack(pady=20)

    # Agregar etiqueta con el valor del usuario en letras verdes
    user_label = Label(user_frame, text=usuario, fg=c_verde, bg=c_negro, font=("Arial", 18))
    user_label.pack(side="left", padx=(20, 10))

    # Agregar etiqueta de bienvenida
    bienvenida_text = "Bienvenido pequeño a una nueva manera de aprender junto a la tecnología"
    bienvenida_label = Label(user_frame, text=bienvenida_text, fg=c_verde, bg=c_negro, font=("Arial", 14),
                             wraplength=400, justify="center")
    bienvenida_label.pack(padx=(20, 10), pady=(5, 0))

    def cerrar_ventana():
        new_window.destroy()

    # Botón para cerrar la segunda ventana
    cerrar_button = Button(new_window, text="Cerrar", bg=c_verde, fg=c_negro, command=cerrar_ventana)
    cerrar_button.pack(pady=10)

    def iniciar_recorrido():
        # Aquí puedes agregar la lógica para iniciar el recorrido
        pass

    # Botón para iniciar el recorrido
    recorrido_button = Button(new_window, text="Iniciar recorrido", bg=c_verde, fg=c_negro, command=iniciar_recorrido)
    recorrido_button.pack(pady=10)

    new_window.mainloop()


root = Tk()
root.geometry("500x600+350+120")
root.minsize(480, 500)
root.config(bg=c_negro)
root.title("Inicio de sesión")

frame = Frame(root, bg=c_negro)
frame.pack(padx=50, pady=50)

imagen_original = Image.open("buitre.png")
imagen_redimensionada = imagen_original.resize((150, 200))
imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
label1 = Label(frame, image=imagen_tk, bg=c_negro)
label1.image = imagen_tk
label1.grid(row=0, column=0, columnspan=2)

correo_var = StringVar()  # Variable para almacenar el valor del campo de entrada de usuario
correo = Entry(frame, font=('sans serif', 12), bg=c_negro, fg=c_verde, textvariable=correo_var)
correo.insert(0, 'Usuario')
correo.grid(columnspan=2, row=1, padx=4, pady=4)

contraseña = Entry(frame, font=('sans serif', 12), bg=c_negro, fg=c_verde)
contraseña.insert(0, 'Contraseña')
contraseña.grid(columnspan=2, row=2, padx=4, pady=4)

checkbox = Checkbutton(frame, text='Recordarme', bg=c_negro, fg=c_verde, activebackground=c_morado)
checkbox.grid(columnspan=2, row=3, padx=4, pady=4)

secionbt = Button(frame, text='Inicio de sesión', font=('sans serif', 12), bg=c_verde, fg=c_negro,
                  command=iniciar_sesion)
secionbt.grid(columnspan=2, row=4, pady=4, padx=4)

root.mainloop()
