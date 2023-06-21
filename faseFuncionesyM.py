import tkinter as tk
import random

# Colores
c_negro = "#010101"
c_verde = "#2cb67d"
c_blanco = "#ffffff"

# Mensajes aleatorios
mensajes = [
    "Las matemáticas son como un juego de acertijos. ¡Descubre los secretos que esconden los números!",
    "Con las matemáticas, puedes resolver problemas y encontrar soluciones creativas. ¡Sé un superhéroe matemático!",
    "Las matemáticas son como una aventura emocionante. Explora nuevas ideas y desafía tu mente",
    "¡Cada error en matemáticas te acerca más a la respuesta correcta! No tengas miedo de equivocarte",
    "Las matemáticas te ayudan a entender el mundo que te rodea. ¡Descubre cómo funcionan las cosas!",
    "¡Tú puedes ser un maestro de los números! Las matemáticas te ayudarán a brillar en todo lo que hagas",
    "Las matemáticas son divertidas y te dan poder. ¡Descubre el asombroso universo de los cálculos y las operaciones!"
]

def generar_mensaje_aleatorio():
    mensaje = random.choice(mensajes)
    mensaje_label.config(text=mensaje)
    

def suma():
    for widget in root.winfo_children():
        if widget != mensaje_label:
            widget.destroy()
    generar_mensaje_aleatorio()
    preguntast = 10
    dificultad = 100
    preguntas_dificultad = [(random.randint(1, dificultad), random.randint(1, dificultad)) for _ in range(preguntast)]
    pregunta_actual = 0
    respuestascorrectas = 0

    def pregunta_sucesiva5():
        nonlocal pregunta_actual
        if pregunta_actual < preguntast:
            num1, num2 = preguntas_dificultad[pregunta_actual]
            question_label.config(text=f"Cual es la suma de {num1} y {num2}?")
        else:
            question_label.config(text=f"Has finalizado el quiz. Tus respuestas correctas fueron {respuestascorrectas} de {preguntast}.")

    def verificador5():
        nonlocal pregunta_actual, respuestascorrectas
        respuesta_usuario = int(answer_entry.get())
        num1, num2 = preguntas_dificultad[pregunta_actual]
        correct_answer = num1 + num2

        if respuesta_usuario == correct_answer:
            result_label.config(text="¡Respuesta correcta!", fg="green")
            respuestascorrectas += 1
        else:
            result_label.config(text=f"Respuesta incorrecta. La respuesta correcta era {correct_answer}.", fg="red")

        answer_entry.delete(0, 'end')
        pregunta_actual += 1
        pregunta_sucesiva5()

    question_label = tk.Label(root, fg=c_verde, bg=c_negro)
    question_label.pack(pady=10)

    answer_entry = tk.Entry(root)
    answer_entry.pack(pady=10)

    submit_button = tk.Button(root, text="Aceptar", command=verificador5)
    submit_button.pack(pady=10)

    result_label = tk.Label(root, fg=c_verde, bg=c_negro)
    result_label.pack(pady=10)

    pregunta_sucesiva5()

def resta():
    for widget in root.winfo_children():
        if widget != mensaje_label:
            widget.destroy()
    generar_mensaje_aleatorio()
    preguntast = 10
    dificultad = 100
    preguntas_dificultad = [(random.randint(1, dificultad), random.randint(1, dificultad)) for _ in range(preguntast)]
    pregunta_actual = 0
    respuestascorrectas = 0

    def pregunta_sucesiva6():
        nonlocal pregunta_actual
        if pregunta_actual < preguntast:
            num1, num2 = preguntas_dificultad[pregunta_actual]
            question_label.config(text=f"Cual es la resta de {num1} - {num2}?")
        else:
            question_label.config(text=f"Has finalizado el quiz. Tus respuestas correctas fueron {respuestascorrectas} de {preguntast}.")

    def verificador6():
        nonlocal pregunta_actual, respuestascorrectas
        respuesta_usuario = int(answer_entry.get())
        num1, num2 = preguntas_dificultad[pregunta_actual]
        correct_answer = num1 - num2

        if respuesta_usuario == correct_answer:
            result_label.config(text="¡Respuesta correcta!", fg="green")
            respuestascorrectas += 1
        else:
            result_label.config(text=f"Respuesta incorrecta. La respuesta correcta era {correct_answer}.", fg="red")

        answer_entry.delete(0, 'end')
        pregunta_actual += 1
        pregunta_sucesiva6()

    question_label = tk.Label(root, fg=c_verde, bg=c_negro)
    question_label.pack(pady=10)

    answer_entry = tk.Entry(root)
    answer_entry.pack(pady=10)

    submit_button = tk.Button(root, text="Aceptar", command=verificador6)
    submit_button.pack(pady=10)

    result_label = tk.Label(root, fg=c_verde, bg=c_negro)
    result_label.pack(pady=10)

    pregunta_sucesiva6()

def multiplicacion():
    for widget in root.winfo_children():
        if widget != mensaje_label:
            widget.destroy()
    generar_mensaje_aleatorio()

    # Generamos las preguntas
    preguntast = 10
    dificultad = 10
    preguntas_dificultad = [(random.randint(1, dificultad), random.randint(1, dificultad)) for _ in range(preguntast)]
    pregunta_actual = 0
    respuestascorrectas = 0

    def pregunta_sucesiva3():
        nonlocal pregunta_actual
        if pregunta_actual < preguntast:
            num1, num2 = preguntas_dificultad[pregunta_actual]
            question_label.config(text=f"Cual es la multiplicación de {num1} y {num2}?")
        else:
            question_label.config(text=f"Has finalizado el quiz. Tus respuestas correctas fueron {respuestascorrectas} de {preguntast}.")

    def verificador3():
        nonlocal pregunta_actual, respuestascorrectas
        respuesta_usuario = int(answer_entry.get())
        num1, num2 = preguntas_dificultad[pregunta_actual]
        correct_answer = num1 * num2

        if respuesta_usuario == correct_answer:
            result_label.config(text="¡Respuesta correcta!", fg="green")
            respuestascorrectas += 1
        else:
            result_label.config(text=f"Respuesta incorrecta. La respuesta correcta era {correct_answer}.", fg="red")

        answer_entry.delete(0, 'end')
        pregunta_actual += 1
        pregunta_sucesiva3()

    question_label = tk.Label(root, fg=c_verde, bg=c_negro)
    question_label.pack(pady=10)

    answer_entry = tk.Entry(root)
    answer_entry.pack(pady=10)

    submit_button = tk.Button(root, text="Aceptar", command=verificador3)
    submit_button.pack(pady=10)

    result_label = tk.Label(root, fg=c_verde, bg=c_negro)
    result_label.pack(pady=10)

    pregunta_sucesiva3()
def division():
    for widget in root.winfo_children():
        if widget != mensaje_label:
            widget.destroy()
    generar_mensaje_aleatorio()

    preguntast = 10
    Dificulatad = 999
    banco_preguntas = [(random.randint(1, Dificulatad), random.randint(1, 11)) for _ in range(preguntast)]
    preg_actual = 0
    resp_corrects = 0

    def pregunta_sucesiva4():
        nonlocal preg_actual
        if preg_actual < preguntast:
            num1, num2 = banco_preguntas[preg_actual]
            question_label.config(text=f"Cual es la división de {num1} / {num2}?")
        else:
            question_label.config(text=f"Has finalizado el quiz. Tus respuestas correctas fueron {resp_corrects} de {preguntast}.")

    def verificador4():
        nonlocal preg_actual, resp_corrects
        respuesta_usuario = int(answer_entry.get())
        num1, num2 = banco_preguntas[preg_actual]
        correct_answer = num1 // num2

        if respuesta_usuario == correct_answer:
            result_label.config(text="¡Felicidades, es correcto!", fg="green")
            resp_corrects += 1
        else:
            result_label.config(text=f"Respuesta incorrecta. La respuesta correcta era {correct_answer}.", fg="red")

        answer_entry.delete(0, "end")
        preg_actual += 1
        pregunta_sucesiva4()

    question_label = tk.Label(root, fg=c_verde, bg=c_negro)
    question_label.pack(pady=10)

    answer_entry = tk.Entry(root)
    answer_entry.pack(pady=10)

    submit_button = tk.Button(root, text="Aceptar", command=verificador4)
    submit_button.pack(pady=10)

    result_label = tk.Label(root, fg=c_verde, bg=c_negro)
    result_label.pack(pady=10)

    pregunta_sucesiva4()

root = tk.Tk()
root.configure(bg=c_negro)
root.title("Operaciones Matemáticas")

# Calcular las posiciones de los botones para que estén centrados
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
button_width = 200
button_height = 50
x = (screen_width - button_width) / 2
y = (screen_height - 4 * button_height - 3 * 20) / 2

suma_button = tk.Button(root, text="Suma", bg=c_verde, fg=c_negro, command=suma, font=("Arial", 24))
suma_button.place(x=x, y=y, width=button_width, height=button_height)

resta_button = tk.Button(root, text="Resta", bg=c_verde, fg=c_negro, command=resta, font=("Arial", 24))
resta_button.place(x=x, y=y + button_height + 20, width=button_width, height=button_height)

multiplicacion_button = tk.Button(root, text="Multiplicación", bg=c_verde, fg=c_negro, command=multiplicacion, font=("Arial", 24))
multiplicacion_button.place(x=x, y=y + 2 * (button_height + 20), width=button_width, height=button_height)

division_button = tk.Button(root, text="División", bg=c_verde, fg=c_negro, command=division, font=("Arial", 24))
division_button.place(x=x, y=y + 3 * (button_height + 20), width=button_width, height=button_height)

# Mensaje aleatorio en la parte inferior derecha
mensaje_label = tk.Label(root, text="", bg=c_negro, fg=c_blanco, anchor="se", font=("Arial", 18))
mensaje_label.pack(side="bottom", pady=10, padx=10, anchor="se")

root.mainloop()