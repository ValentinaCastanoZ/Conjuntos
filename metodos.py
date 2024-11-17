# Función de unión para tres o más conjuntos
def union(*conjuntos):
    """
    Calcula la unión de múltiples conjuntos.
    
    Args:
        *conjuntos: Secuencia de iterables representando conjuntos.
    
    Returns:
        list: Lista con todos los elementos únicos de los conjuntos dados.
    """
    resultado = []
    for conjunto in conjuntos:
        for elemento in conjunto:
            if elemento not in resultado:
                resultado.append(elemento)
    return resultado


# Función de intersección para tres o más conjuntos
def interseccion(*conjuntos):
    """
    Calcula la intersección de múltiples conjuntos.
    
    Args:
        *conjuntos: Secuencia de iterables representando conjuntos.
    
    Returns:
        list: Lista con los elementos comunes a todos los conjuntos dados.
    """
    if not conjuntos:
        return []
    resultado = list(conjuntos[0])  # Inicializar con el primer conjunto
    for conjunto in conjuntos[1:]:
        resultado = [elemento for elemento in resultado if elemento in conjunto]
    return resultado


# Función de diferencia para un conjunto base y dos o más conjuntos
def diferencia(conjunto_base, *otros_conjuntos):
    """
    Calcula la diferencia entre un conjunto base y otros conjuntos.
    
    Args:
        conjunto_base: Iterable representando el conjunto base.
        *otros_conjuntos: Secuencia de iterables con los conjuntos a comparar.
    
    Returns:
        list: Lista con los elementos del conjunto base que no están en los otros conjuntos.
    """
    resultado = list(conjunto_base)
    for conjunto in otros_conjuntos:
        resultado = [elemento for elemento in resultado if elemento not in conjunto]
    return resultado


# Función de diferencia simétrica para múltiples conjuntos
def diferencia_simetrica(*conjuntos):
    """
    Calcula la diferencia simétrica entre dos o más conjuntos.
    
    Args:
        *conjuntos: Secuencia de iterables representando conjuntos.
    
    Returns:
        list: Lista con los elementos que están en un conjunto pero no en todos.
    """
    if not conjuntos:
        return []
    
    resultado = list(conjuntos[0])  # Inicializar con el primer conjunto
    for conjunto in conjuntos[1:]:
        resultado = [elemento for elemento in union(resultado, conjunto) 
                     if elemento not in interseccion(resultado, conjunto)]
    return resultado


# Función para verificar si un conjunto es subconjunto en un contexto de múltiples conjuntos
def es_subconjunto(conjunto_base, *otros_conjuntos):
    """
    Verifica si un conjunto base es subconjunto de la intersección de otros conjuntos.
    
    Args:
        conjunto_base: Iterable representando el conjunto base.
        *otros_conjuntos: Secuencia de iterables con los conjuntos a comparar.
    
    Returns:
        bool: Verdadero si conjunto_base es subconjunto de la intersección de otros conjuntos.
    """
    if not otros_conjuntos:
        return False
    interseccion_conjuntos = interseccion(*otros_conjuntos)
    return all(elemento in interseccion_conjuntos for elemento in conjunto_base)


# Función para verificar si un conjunto es superconjunto en un contexto de múltiples conjuntos
def es_superconjunto(conjunto_base, *otros_conjuntos):
    """
    Verifica si un conjunto base es superconjunto de la unión de otros conjuntos.
    
    Args:
        conjunto_base: Iterable representando el conjunto base.
        *otros_conjuntos: Secuencia de iterables con los conjuntos a comparar.
    
    Returns:
        bool: Verdadero si conjunto_base es superconjunto de la unión de otros conjuntos.
    """
    if not otros_conjuntos:
        return False
    union_conjuntos = union(*otros_conjuntos)
    return all(elemento in conjunto_base for elemento in union_conjuntos)
