//18.	3. Calcular el factorial de un número usando un ciclo repetir.

Proceso factorialNumero
	Definir num, factorial, contador Como Entero
	
	Escribir "Ingrese un número entero positivo:"
	Leer num
	
	Si num < 0 Entonces
		Escribir "El número ingresado no es válido. Debe ser positivo."
	Sino
		factorial <- 1
		contador <- 1
		
		Mientras contador <= num Hacer
			factorial <- factorial * contador
			contador <- contador + 1
		FinMientras
		
		Escribir "El factorial de ", num, " es ", factorial
	FinSi
FinProceso

