otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
este_curso = 1.5
crudo_promedio = 5
curdo_este = 3.5

#diferencias con los otros cursos

diferencia_min = 100 -(este_curso/otros_cursos_min)*100
diferencia_max = 100 -(este_curso*1000//otros_cursos_max)/10
diferencia_prom = 100 -(este_curso/otros_cursos_prom)*100

print(f"el curso este dura un {diferencia_min}% menos que el mas rapido")
print(f"el curso este dura un {diferencia_max}% menos que el menos rapido")
print(f"el curso este dura un {diferencia_prom}% menos que el promedio")

diferencia_crudo = 100 -(este_curso/otros_cursos_min)*100
