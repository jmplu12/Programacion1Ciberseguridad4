//19.4. Leer números hasta que se ingrese un número negativo, mostrando la cantidad de positivos.

Algoritmo contarPositivos
	Definir num, contador Como Real
	contador <- 0
	
	Repetir
		Escribir "Ingrese un número (negativo para terminar):"
		Leer num
		si numero > 0 Entonces
			contador <- contador + 1
		FinSi
	Hasta Que num < 0
	Escribir "La cantidad de números positivos ingresados es: ", contador
FinAlgoritmo
