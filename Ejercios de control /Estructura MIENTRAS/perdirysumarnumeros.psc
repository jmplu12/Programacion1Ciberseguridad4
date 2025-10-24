//16.1. Pedir números y sumarlos hasta que el usuario ingrese 0.

Algoritmo perdirysumarnumeros
	Definir numero, suma Como Entero
	suma <- 0
	
	Repetir
		Escribir "Introduzca un Nimero(si introduce 0 se suman y finaliza)"
		Leer numero
		suma <- suma + numero
	Hasta Que numero = 0
	
	Escribir "LA SUMA TOTAL DE LOS NUMEROS ES = ", suma
	
FinAlgoritmo
