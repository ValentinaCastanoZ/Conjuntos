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

        # Obtener los objetos de las áreas
        area_100 = venn_diagram.get_patch_by_id('100')
        area_010 = venn_diagram.get_patch_by_id('010')
        area_110 = venn_diagram.get_patch_by_id('110')

        # Verificar si los objetos de área son válidos y asignar las etiquetas
        if area_100 is not None:
            label_100 = ', '.join(map(str, diferencia(conjunto_a, conjunto_b)))
            area_100.set_label(label_100 if label_100 else 'No elements')

        if area_010 is not None:
            label_010 = ', '.join(map(str, diferencia(conjunto_b, conjunto_a)))
            area_010.set_label(label_010 if label_010 else 'No elements')

        if area_110 is not None:
            label_110 = ', '.join(map(str, interseccion(conjunto_a, conjunto_b)))
            area_110.set_label(label_110 if label_110 else 'No elements')

        # Agregar leyenda
        plt.legend(loc="lower left", bbox_to_anchor=(1.5, 0), title="Valores")

    # Diagrama de Venn para 3 conjuntos
    elif len(conjuntos) == 3:
        conjunto_a, conjunto_b, conjunto_c = conjuntos
        venn_diagram = venn3([set(conjunto_a), set(conjunto_b), set(conjunto_c)], set_labels=('A', 'B', 'C'), ax=axes)

        # Obtener los objetos de las áreas
        area_100 = venn_diagram.get_patch_by_id('100')
        area_010 = venn_diagram.get_patch_by_id('010')
        area_001 = venn_diagram.get_patch_by_id('001')
        area_110 = venn_diagram.get_patch_by_id('110')
        area_101 = venn_diagram.get_patch_by_id('101')
        area_011 = venn_diagram.get_patch_by_id('011')
        area_111 = venn_diagram.get_patch_by_id('111')

        # Etiquetar las áreas con los elementos correspondientes
        if area_100 is not None:
            label_100 = ', '.join(map(str, diferencia(conjunto_a, conjunto_b, conjunto_c)))
            area_100.set_label(label_100 if label_100 else 'No elements')
        
        if area_010 is not None:
            label_010 = ', '.join(map(str, diferencia(conjunto_b, conjunto_a, conjunto_c)))
            area_010.set_label(label_010 if label_010 else 'No elements')
        
        if area_001 is not None:
            label_001 = ', '.join(map(str, diferencia(conjunto_c, conjunto_a, conjunto_b)))
            area_001.set_label(label_001 if label_001 else 'No elements')
        
        if area_110 is not None:
            label_110 = ', '.join(map(str, interseccion(conjunto_a, conjunto_b)))
            area_110.set_label(label_110 if label_110 else 'No elements')

        if area_101 is not None:
            label_101 = ', '.join(map(str, interseccion(conjunto_a, conjunto_c)))
            area_101.set_label(label_101 if label_101 else 'No elements')

        if area_011 is not None:
            label_011 = ', '.join(map(str, interseccion(conjunto_b, conjunto_c)))
            area_011.set_label(label_011 if label_011 else 'No elements')

        if area_111 is not None:
            label_111 = ', '.join(map(str, union(conjunto_a, conjunto_b, conjunto_c)))
            area_111.set_label(label_111 if label_111 else 'No elements')

        # Agregar leyenda
        plt.legend(loc="lower left", bbox_to_anchor=(1.5, 0), title="Valores")

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