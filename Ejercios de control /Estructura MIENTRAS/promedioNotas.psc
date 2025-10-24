//20.	5. Ingresar notas hasta que el usuario ingrese -1, y luego mostrar el promedio.

Proceso promedioNotas
	Definir nota, suma, contador, promedio Como Real
	suma <- 0
	contador <- 0
	
	Repetir
		Escribir "Ingrese una nota (-1 para terminar):"
		Leer nota
		
		Si nota <> -1 Entonces
			suma <- suma + nota
			contador <- contador + 1
		FinSi
	Hasta Que nota = -1
	
	Si contador > 0 Entonces
		promedio <- suma / contador
		Escribir "El promedio de las notas es: ", promedio
	Sino
		Escribir "No se ingresaron notas válidas."
	FinSi
FinProceso
