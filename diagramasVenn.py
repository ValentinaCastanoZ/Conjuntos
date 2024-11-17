from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import StringVar
from matplotlib_venn import venn2, venn3
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from metodos import union, interseccion, diferencia, diferencia_simetrica


def mostrar_venn(conjuntos, resultado, operacion):
    """
    Muestra un diagrama de Venn para 2 o 3 conjuntos, dependiendo de los datos proporcionados.
    
    Args:
        conjuntos: Lista de conjuntos a visualizar.
        resultado: Resultado de la operación de conjuntos.
        operacion: Nombre de la operación realizada (para mostrar en el título).
    """
    plt.clf()  # Limpiar el gráfico anterior

    # Crear la figura y los ejes
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 5))
    fig.suptitle(f'Operaciones de Conjuntos ({len(conjuntos)} Conjuntos)')

    # Diagrama de Venn para 2 conjuntos
    if len(conjuntos) == 2:
        conjunto_a, conjunto_b = conjuntos
        venn_diagram = venn2([set(conjunto_a), set(conjunto_b)], set_labels=('A', 'B'), ax=axes)

        # Etiquetas personalizadas
        venn_diagram.get_label_by_id('100').set_text(', '.join(diferencia(conjunto_a, conjunto_b)) or 'Ø')
        venn_diagram.get_label_by_id('010').set_text(', '.join(diferencia(conjunto_b, conjunto_a)) or 'Ø')
        venn_diagram.get_label_by_id('110').set_text(', '.join(interseccion(conjunto_a, conjunto_b)) or 'Ø')

    # Diagrama de Venn para 3 conjuntos
    elif len(conjuntos) == 3:
        conjunto_a, conjunto_b, conjunto_c = conjuntos
        venn_diagram = venn3([set(conjunto_a), set(conjunto_b), set(conjunto_c)], set_labels=('A', 'B', 'C'), ax=axes)

        # Etiquetas personalizadas
        venn_diagram.get_label_by_id('100').set_text(', '.join(diferencia(conjunto_a, union(conjunto_b, conjunto_c))) or 'Ø')
        venn_diagram.get_label_by_id('010').set_text(', '.join(diferencia(conjunto_b, union(conjunto_a, conjunto_c))) or 'Ø')
        venn_diagram.get_label_by_id('001').set_text(', '.join(diferencia(conjunto_c, union(conjunto_a, conjunto_b))) or 'Ø')
        venn_diagram.get_label_by_id('110').set_text(', '.join(interseccion(conjunto_a, conjunto_b)) or 'Ø')
        venn_diagram.get_label_by_id('101').set_text(', '.join(interseccion(conjunto_a, conjunto_c)) or 'Ø')
        venn_diagram.get_label_by_id('011').set_text(', '.join(interseccion(conjunto_b, conjunto_c)) or 'Ø')
        venn_diagram.get_label_by_id('111').set_text(', '.join(interseccion(conjunto_a, interseccion(conjunto_b, conjunto_c))) or 'Ø')

    else:
        axes.set_title('No se pueden visualizar más de 3 conjuntos en un diagrama de Venn')
        return

    # Título del gráfico
    axes.set_title(f'Resultado ({operacion}): {resultado}')

    # Ajustar el diseño
    plt.tight_layout(rect=[0, 0, 1, 0.96])

    # Mostrar en la interfaz Tkinter
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=8, column=0, columnspan=2, pady=10)

    ventana.update_idletasks()  # Actualizar la ventana después de mostrar el gráfico


# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("Operaciones de Conjuntos")