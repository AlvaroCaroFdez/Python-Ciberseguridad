# Escribir un programa que pida al usuario una palabra y
# muestre por pantalla el número de veces que contiene cada vocal.

def contar_vocales(palabra):
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    palabra = palabra.lower()
    
    for letra in palabra:
        if letra in vocales:
            vocales[letra] += 1
    
    for vocal, cantidad in vocales.items():
        print(f"La vocal '{vocal}' aparece {cantidad} veces.")
        
palabra = input("Introduce una palabra: ")

contar_vocales(palabra)