//23.	3. Sumar los números del 1 al 50 usando un acumulador.

Proceso suma1a50
	Definir suma Como Entero
	suma <- 0
	
	Para i <- 1 Hasta 50 Con Paso 1 Hacer
		suma <- suma + i
	FinPara
	
	Escribir "La suma de los números del 1 al 50 es: ", suma
FinProceso
