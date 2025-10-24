//8.	3. Según la calificación (A, B, C, D, F),
//mostrar el mensaje de rendimiento del estudiante.
Algoritmo MostralRendimiento
	Escribir "Mostral rendimiento del Alumno"
	Definir Calificacion Como Caracter
	Escribir "Introduzca (A, B, C, D, F) para saber la calificacion"
	Leer Calificacion
	Calificacion <- Mayusculas(Calificacion)
	Segun Calificacion Hacer
		"A": Escribir "Excelente Rendimiento"
		"B": Escribir "Buen Rendimiento"
		"C": Escribir "Rendimiento Aceptable"
		"D": Escribir "Bajo Rendimiento"
		"F": Escribir "Rendimiento Insuficiente"
		De Otro Modo:
		Escribir "Calificacion Invalidad. Usa A,B,C,D o F"
	FinSegun
FinAlgoritmo
