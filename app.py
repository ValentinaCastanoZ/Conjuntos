from tkinter import ttk
from tkinter import simpledialog
from diagramasVenn import *
from metodos import *

def realizar_operacion():
    # Leer todos los conjuntos ingresados dinámicamente
    conjuntos = [set(map(str.strip, entry.get().split(','))) for entry in entradas_conjuntos]

    # Obtener la operación deseada del usuario
    operacion = entry_operacion.get()

    # Realizar la operación
    if operacion == 'u':
        # Unión de todos los conjuntos
        resultado = union(*conjuntos)
    elif operacion == '&':
        # Intersección de todos los conjuntos
        resultado = interseccion(*conjuntos)
    elif operacion == '-':
        # Diferencia: Se toma el primer conjunto como base
        resultado = diferencia(conjuntos[0], *conjuntos[1:])
    elif operacion == '^':
        # Diferencia simétrica entre todos los conjuntos
        resultado = diferencia_simetrica(*conjuntos)
    elif operacion == 'sub':
        # Verificar si el primer conjunto es subconjunto de los demás
        resultado = es_subconjunto(conjuntos[0], *conjuntos[1:])
    elif operacion == 'sup':
        # Verificar si el primer conjunto es superconjunto de los demás
        resultado = es_superconjunto(conjuntos[0], *conjuntos[1:])
    else:
        # Operación no válida
        resultado = []

    # Mostrar los resultados en las etiquetas
    label_resultado.config(text=f"Resultado ({operacion}): {resultado}")

    # Mostrar los gráficos de Venn (hasta 3 conjuntos)
    if len(conjuntos) == 2:
        mostrar_venn(conjuntos, resultado, operacion)
    elif len(conjuntos) == 3:
        mostrar_venn(conjuntos, resultado, operacion)
    else:
        # Mostrar mensaje si hay más de 3 conjuntos
        label_resultado.config(text=f"Operación completada, pero no se puede graficar más de 3 conjuntos.")

def agregar_conjuntos():
    """
    Permite al usuario especificar cuántos conjuntos desea agregar
    y genera dinámicamente las entradas necesarias.
    """
    global entradas_conjuntos

    # Limpiar el frame actual de entradas
    for widget in frame_entradas.winfo_children():
        widget.destroy()

    # Pedir el número de conjuntos
    num_conjuntos = simpledialog.askinteger("Número de Conjuntos", "¿Cuántos conjuntos deseas ingresar?", minvalue=2)

    # Crear entradas dinámicas para los conjuntos
    entradas_conjuntos = []
    for i in range(num_conjuntos):
        label = ttk.Label(frame_entradas, text=f"Conjunto {chr(65 + i)}:")
        label.grid(row=i, column=0, padx=10, pady=5)
        entry = ttk.Entry(frame_entradas)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entradas_conjuntos.append(entry)

    # Entrada de texto para la operación
    label_operacion = ttk.Label(frame_entradas, text="Operación:")
    label_operacion.grid(row=num_conjuntos, column=0, padx=10, pady=5)
    global entry_operacion
    entry_operacion = ttk.Entry(frame_entradas)
    entry_operacion.grid(row=num_conjuntos, column=1, padx=10, pady=5)


# Frames para organizar la interfaz
frame_entradas = ttk.Frame(ventana, padding="10")
frame_entradas.grid(row=0, column=0, columnspan=2, pady=10)

frame_resultado = ttk.Frame(ventana, padding="10")
frame_resultado.grid(row=2, column=0, columnspan=2, pady=5)

# Frame para mostrar el diagrama de Venn a la derecha
frame_venn = ttk.Frame(ventana, padding="10")
frame_venn.grid(row=0, column=2, rowspan=3, padx=20, pady=10)

# Botón para agregar conjuntos
boton_agregar_conjuntos = ttk.Button(ventana, text="Agregar Conjuntos", command=agregar_conjuntos)
boton_agregar_conjuntos.grid(row=1, column=0, columnspan=2, pady=10)

# Botón para realizar las operaciones
boton_operar = ttk.Button(ventana, text="Realizar Operación", command=realizar_operacion)
boton_operar.grid(row=3, column=0, columnspan=2, pady=10)

# Etiqueta para mostrar el resultado
label_resultado = ttk.Label(frame_resultado, text="")
label_resultado.grid(row=0, column=0, pady=5)

# Configuración inicial de entradas
entradas_conjuntos = []
agregar_conjuntos()

# Ajustar ventana
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
x_pos = (ancho_pantalla - ventana.winfo_reqwidth()) // 2
y_pos = (alto_pantalla - ventana.winfo_reqheight()) // 2
ventana.geometry(f"+{x_pos-80}+{y_pos-100}")

# Iniciar el bucle principal
ventana.mainloop()
