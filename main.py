"""
Equipo: Ronald Alvarez, Ivan Andres, Nelsy Madera, Samuel Pai
"""

# Funcion : Suma
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

if __name__ == "__main__":
    x = 10
    y = 5
    
    print(f"Suma de {x} + {y} = {sumar(x, y)}")
    print(f"Resta de {x} - {y} = {restar(x, y)}")

#Función : Multiplicar 
def multiplicar(a, b):
    return a*b
if __name__ == "__name__":
    print("Multiplicar: 6*7=", multiplicar(6, 7))

# Funcion : Division
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division entre cero"
    
if __name__ == "__main__":
    print("División:", dividir(10, 2))
    
    
# Funcion : Potencia
def potencia(base, exponente):
    return base ** exponente

if __name__ == "__main__":
    print(f"Potencia = {potencia(x,y)}")
    
# Función : Módulo
def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: División entre cero"

if __name__ == "__main__":
    print(f"Módulo: 10 % 3 = {modulo(10, 3)}")
