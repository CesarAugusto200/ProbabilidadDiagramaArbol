#Realizar una implementacion en Python de un diagrama de Árbol De la siguente actividad:

##En Software hay 5 aulas: el aula roja, el aula azul, el aula negra, el aula verde y el aula amarillo. 
#El aula roja tiene al 25 % de los estudiantes de la academia, el aula azul al 30 %,
#el aula negra al 10 %, el verde 25% y el amarillo 10%. Además, en cada aula hay un 75 % de hombres. 
#Si se selecciona un estudiante al azar, ¿cuál es la probabilidad de que sea un estudiante hombre del aula azul?


probabilidades_aulas = {
    'Roja': 0.25,
    'Azul': 0.30,
    'Negra': 0.10,
    'Verde': 0.25,
    'Amarilla': 0.10
}


probabilidad_hombre_dado_aula = 0.75
probabilidad_mujer_dado_aula = 0.25


def crear_diagrama(probabilidades_aulas, prob_hombre, prob_mujer):
    diagrama = "Estudiantes\n"
    for aula, prob_aula in probabilidades_aulas.items():
        prob_hombre_aula = prob_aula * prob_hombre
        prob_mujer_aula = prob_aula * prob_mujer
        diagrama += f"├─ {aula} (P={prob_aula})\n"
        diagrama += f"│  ├─ Hombre (P={prob_hombre_aula:.2f})\n"
        diagrama += f"│  └─ Mujer (P={prob_mujer_aula:.2f})\n"
    return diagrama


probabilidad_hombre_aula_azul = probabilidades_aulas['Azul'] * probabilidad_hombre_dado_aula


diagrama = crear_diagrama(probabilidades_aulas, probabilidad_hombre_dado_aula, probabilidad_mujer_dado_aula)
print("Diagrama de Árbol de Probabilidades:")
print(diagrama)
print(f"La probabilidad de que un estudiante sea un hombre del aula azul es: {probabilidad_hombre_aula_azul:.4f}")
