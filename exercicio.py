from typing import List

def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado

print(filtrar_acima_de([1, 2, 3, 4, 5], 3.1))

#####

def contar_valores_unicos(valores: List[int]) -> int:
    print(len(set(valores)))
    return print(set(valores))
    
contar_valores_unicos([1, 2, 2, 3, 4, 6, 6])