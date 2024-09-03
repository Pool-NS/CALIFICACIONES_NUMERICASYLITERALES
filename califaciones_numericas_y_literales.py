import tkinter as tk
from tkinter import messagebox


def calcular_calificacion():
    try:
        calificacion = float(entrada_calificacion.get())
        if calificacion > 10 or calificacion < 0:
            raise ValueError("La calificación debe estar entre 0 y 10")

        if calificacion > 9.0:
            resultado = "A"
        elif calificacion > 8.0:
            resultado = "B"
        elif calificacion >= 7.5:
            resultado = "C"
        else:
            resultado = "R"

        etiqueta_resultado.config(text=f"La calificación es {resultado}.")
    except ValueError as e:
        messagebox.showerror("Error", str(e))


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Calificación")
ventana.geometry("300x200")

# Crear y colocar widgets
tk.Label(ventana, text="Ingrese la calificación:").pack(pady=10)
entrada_calificacion = tk.Entry(ventana)
entrada_calificacion.pack()

tk.Button(ventana, text="Calcular Calificación", command=calcular_calificacion).pack(pady=10)

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

# Iniciar el loop de la interfaz gráfica
ventana.mainloop()